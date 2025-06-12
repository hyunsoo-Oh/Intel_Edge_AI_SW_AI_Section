import sys
import os
import shutil
from PySide6.QtWidgets import (
    QApplication, QDialog, QWidget, QFileDialog, QInputDialog,
    QMessageBox, QPushButton, QListWidgetItem, QMenu
)
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QSize, Qt
from gui.mp3_player_ui import Ui_Form
from gui.downloadDialog import DownloadDialog   # 직접 만들 파일
from gui.constants import icon, fpath, MUSIC_DIR

class MP3Player(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.path = ['', '']
        # 초기 상태: 반복 모드 꺼짐 (loop)
        self.loop_mode = False

        # 타이틀 바 텍스트 및 아이콘 설정
        self.setWindowTitle("YouTube MP3 Player")
        self.setWindowIcon(QIcon(icon("mp3_icon.png")))

        # 버튼 클릭 시 슬롯 연결
        self.ui.PlaybackBtn.clicked.connect(self.toggle_loop_mode)

        # Download 버튼에 연결 추가
        self.ui.downloadBtn.clicked.connect(self.open_download_ui)

        # 아이콘 초기 설정
        self.update_loop_icon()

        # List 버튼에 연결 추가
        self.ui.downloadListBtn.clicked.connect(self.open_slot)

        # Add Player 버튼 연결
        self.ui.addMusicBtn.clicked.connect(self.create_new_playlist)

        # music 폴더가 없으면 생성
        self.ensure_music_folder()

        # 기존 플레이리스트 로드
        self.load_existing_playlists()

    def ensure_music_folder(self):
        """music 폴더가 없으면 생성"""
        music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
        if not os.path.exists(music_folder):
            os.makedirs(music_folder)

    def load_existing_playlists(self):
        """기존에 만들어진 플레이리스트들을 로드"""
        music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
        if os.path.exists(music_folder):
            for folder_name in os.listdir(music_folder):
                folder_path = os.path.join(music_folder, folder_name)
                if os.path.isdir(folder_path):
                    self.add_playlist_button(folder_name)

    def create_new_playlist(self):
        """새로운 플레이리스트 생성"""
        playlist_name, ok = QInputDialog.getText(
            self,
            "새 플레이리스트",
            "플레이리스트 이름을 입력하세요:",
            text="My Playlist"
        )

        if ok and playlist_name.strip():
            playlist_name = playlist_name.strip()

            # 중복 체크
            if any(btn.text() == playlist_name for btn in self.playlist_buttons):
                QMessageBox.warning(self, "중복된 이름", "이미 존재하는 플레이리스트 이름입니다.")
                return

            # music 폴더에 새 폴더 생성
            music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
            playlist_folder = os.path.join(music_folder, playlist_name)

            try:
                os.makedirs(playlist_folder, exist_ok=True)
                self.add_playlist_button(playlist_name)
                QMessageBox.information(self, "성공", f"'{playlist_name}' 플레이리스트가 생성되었습니다.")
            except Exception as e:
                QMessageBox.critical(self, "오류", f"플레이리스트 생성 중 오류가 발생했습니다: {str(e)}")

    def add_playlist_button(self, playlist_name):
        """플레이리스트 버튼을 사이드바에 추가"""
        # 새 버튼 생성
        playlist_btn = QPushButton(playlist_name)
        playlist_btn.setObjectName(f"playlist_{len(self.playlist_buttons)}")

        # 버튼 클릭 시 플레이리스트 선택
        playlist_btn.clicked.connect(lambda: self.select_playlist(playlist_name))

        # 버튼 우클릭 메뉴 설정
        playlist_btn.setContextMenuPolicy(Qt.CustomContextMenu)
        playlist_btn.customContextMenuRequested.connect(
            lambda pos: self.show_playlist_context_menu(playlist_btn, playlist_name, pos)
        )

        # Add Music 버튼 위에 삽입
        insert_index = self.ui.verticalLayout_6.count() - 2  # spacer 위에
        self.ui.verticalLayout_6.insertWidget(insert_index, playlist_btn)

        self.playlist_buttons.append(playlist_btn)

    def show_playlist_context_menu(self, button, playlist_name, pos):
        """플레이리스트 버튼 우클릭 메뉴"""
        menu = QMenu(self)

        rename_action = QAction("이름 변경", self)
        rename_action.triggered.connect(lambda: self.rename_playlist(button, playlist_name))

        delete_action = QAction("삭제", self)
        delete_action.triggered.connect(lambda: self.delete_playlist(button, playlist_name))

        menu.addAction(rename_action)
        menu.addAction(delete_action)

        menu.exec(button.mapToGlobal(pos))

    def rename_playlist(self, button, old_name):
        """플레이리스트 이름 변경"""
        new_name, ok = QInputDialog.getText(
            self,
            "플레이리스트 이름 변경",
            "새 이름을 입력하세요:",
            text=old_name
        )

        if ok and new_name.strip() and new_name.strip() != old_name:
            new_name = new_name.strip()

            # 중복 체크
            if any(btn.text() == new_name for btn in self.playlist_buttons if btn != button):
                QMessageBox.warning(self, "중복된 이름", "이미 존재하는 플레이리스트 이름입니다.")
                return

            try:
                music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
                old_path = os.path.join(music_folder, old_name)
                new_path = os.path.join(music_folder, new_name)

                os.rename(old_path, new_path)
                button.setText(new_name)

                # 현재 선택된 플레이리스트라면 제목도 업데이트
                if self.current_playlist == old_name:
                    self.current_playlist = new_name
                    self.ui.playBox.setTitle(f"Play List - {new_name}")

                QMessageBox.information(self, "성공", f"플레이리스트 이름이 '{new_name}'으로 변경되었습니다.")

            except Exception as e:
                QMessageBox.critical(self, "오류", f"이름 변경 중 오류가 발생했습니다: {str(e)}")

    def delete_playlist(self, button, playlist_name):
        """플레이리스트 삭제"""
        reply = QMessageBox.question(
            self,
            "플레이리스트 삭제",
            f"'{playlist_name}' 플레이리스트를 삭제하시겠습니까?\n(폴더와 모든 파일이 삭제됩니다)",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
                playlist_folder = os.path.join(music_folder, playlist_name)

                # 폴더와 내용물 삭제
                if os.path.exists(playlist_folder):
                    shutil.rmtree(playlist_folder)

                # 버튼 제거
                self.ui.verticalLayout_6.removeWidget(button)
                button.deleteLater()
                self.playlist_buttons.remove(button)

                # 현재 선택된 플레이리스트라면 초기화
                if self.current_playlist == playlist_name:
                    self.current_playlist = None
                    self.ui.playBox.setTitle("Play List")
                    self.ui.musicList.clear()

                QMessageBox.information(self, "성공", f"'{playlist_name}' 플레이리스트가 삭제되었습니다.")

            except Exception as e:
                QMessageBox.critical(self, "오류", f"삭제 중 오류가 발생했습니다: {str(e)}")

    def select_playlist(self, playlist_name):
        """플레이리스트 선택"""
        self.current_playlist = playlist_name
        self.ui.playBox.setTitle(f"Play List - {playlist_name}")
        self.load_playlist_songs(playlist_name)

    def load_playlist_songs(self, playlist_name):
        """플레이리스트의 곡들을 로드"""
        self.ui.musicList.clear()

        # Add 버튼 추가
        add_item = QListWidgetItem("+ Add")
        add_item.setData(Qt.UserRole, "ADD_BUTTON")
        self.ui.musicList.addItem(add_item)

        # 플레이리스트 폴더의 음악 파일들 로드
        music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
        playlist_folder = os.path.join(music_folder, playlist_name)

        if os.path.exists(playlist_folder):
            for file_name in os.listdir(playlist_folder):
                if file_name.lower().endswith('.mp3'):
                    song_item = QListWidgetItem(file_name[:-4])  # .mp3 확장자 제거
                    song_item.setData(Qt.UserRole, os.path.join(playlist_folder, file_name))
                    self.ui.musicList.addItem(song_item)

        # 리스트 아이템 클릭 이벤트 연결
        self.ui.musicList.itemClicked.connect(self.on_music_item_clicked)

    def on_music_item_clicked(self, item):
        """음악 리스트 아이템 클릭 처리"""
        if item.data(Qt.UserRole) == "ADD_BUTTON":
            self.add_song_to_playlist()
        else:
            # 일반 음악 파일 선택
            file_path = item.data(Qt.UserRole)
            print(f"🎵 선택된 곡: {file_path}")
            # 여기에 음악 재생 로직 추가 가능

    def add_song_to_playlist(self):
        """플레이리스트에 곡 추가"""
        if not self.current_playlist:
            QMessageBox.warning(self, "플레이리스트 선택", "먼저 플레이리스트를 선택해주세요.")
            return

        # downloads 폴더에서 mp3 파일 선택
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "음악 파일 선택",
            MUSIC_DIR,
            "MP3 Files (*.mp3);;All Files (*.*)"
        )

        if file_path:
            try:
                # 파일 이름만 추출
                file_name = os.path.basename(file_path)

                # 목적지 경로
                music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
                dest_folder = os.path.join(music_folder, self.current_playlist)
                dest_path = os.path.join(dest_folder, file_name)

                # 중복 파일 체크
                if os.path.exists(dest_path):
                    reply = QMessageBox.question(
                        self,
                        "중복 파일",
                        f"'{file_name}' 파일이 이미 존재합니다. 덮어쓰시겠습니까?",
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.No
                    )
                    if reply != QMessageBox.Yes:
                        return

                # 파일 복사
                shutil.copy2(file_path, dest_path)

                # 리스트 새로고침
                self.load_playlist_songs(self.current_playlist)

                QMessageBox.information(self, "성공", f"'{file_name}' 파일이 플레이리스트에 추가되었습니다.")

            except Exception as e:
                QMessageBox.critical(self, "오류", f"파일 추가 중 오류가 발생했습니다: {str(e)}")

    def toggle_loop_mode(self):
        self.loop_mode = not self.loop_mode
        self.update_loop_icon()

    def update_loop_icon(self):
        if self.loop_mode:
            icon_path = "single_vector_icon.svg"
        else:
            icon_path = "loop_icon.svg"
        self.ui.PlaybackBtn.setIcon(QIcon(icon(icon_path)))

    def open_download_ui(self):
        dialog = DownloadDialog(self)  # QDialog 상속한 클래스
        dialog.exec()

    def open_slot(self):
        self.path = QFileDialog.getOpenFileName(self,
                                                'Open File', fpath(''),
                                                'mp3 File(*.mp3);;All File(*.*)')
        if self.path[0]:
            with open(self.path[0], 'r', encoding='utf-8') as f:
                str_read = f.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MP3Player()
    window.show()
    sys.exit(app.exec())