import sys
import os
import shutil

from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import (
    QApplication, QDialog, QWidget, QFileDialog,
    QInputDialog, QMessageBox, QListWidgetItem,
    QPushButton, QMenu
)
from PySide6.QtGui import QIcon, QAction, QFontMetrics, QPixmap
from PySide6.QtCore import QSize, Qt, QUrl, QTime
from gui.mp3_player_ui import Ui_Form
from gui.downloadDialog import DownloadDialog
from gui.constants import icon, fpath, MUSIC_DIR
from player.music_player import MusicPlayer
from player.playlist_manager import get_mp3_list_from_folder

class MP3Player(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.music_player = MusicPlayer()

        self.path = ['', '']
        self.loop_mode = False
        self.playlist_buttons = []
        self.current_playlist = None
        self.current_song_index = -1

        self.ui.volumeSlider.setValue(50)
        self.setWindowTitle("YouTube MP3 Player")
        self.setWindowIcon(QIcon(icon("mp3_icon.png")))
        self.ui.prevBtn.setIcon(QIcon(icon("prev_icon.svg")))
        self.ui.playBtn.setIcon(QIcon(icon("play_icon.svg")))
        self.ui.nextBtn.setIcon(QIcon(icon("next_icon.svg")))
        self.ui.label.setPixmap(QPixmap(icon("volume_icon.svg")))

        self.ui.PlaybackBtn.clicked.connect(self.toggle_loop_mode)
        self.ui.downloadBtn.clicked.connect(self.open_download_ui)
        self.ui.downloadListBtn.clicked.connect(self.open_slot)
        self.ui.addMusicBtn.clicked.connect(self.create_new_playlist)
        self.ui.musicList.itemClicked.connect(self.on_music_item_clicked)
        self.ui.playBtn.clicked.connect(self.toggle_play_pause)
        self.ui.prevBtn.clicked.connect(self.play_previous)
        self.ui.nextBtn.clicked.connect(self.play_next)
        self.ui.volumeSlider.valueChanged.connect(self.music_player.set_volume)

        self.music_player.player.positionChanged.connect(self.update_position)
        self.music_player.player.durationChanged.connect(self.update_duration)
        self.music_player.player.mediaStatusChanged.connect(self.check_auto_next)
        self.ui.playTimeSlider.sliderMoved.connect(self.seek_position)

        self.update_loop_icon()
        self.ensure_music_folder()
        self.load_existing_playlists()

    def ensure_music_folder(self):
        music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
        if not os.path.exists(music_folder):
            os.makedirs(music_folder)

    def load_existing_playlists(self):
        music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
        if os.path.exists(music_folder):
            for folder_name in os.listdir(music_folder):
                folder_path = os.path.join(music_folder, folder_name)
                if os.path.isdir(folder_path):
                    self.add_playlist_button(folder_name)

    def create_new_playlist(self):
        playlist_name, ok = QInputDialog.getText(self, "새 플레이리스트", "플레이리스트 이름을 입력하세요:", text="My Playlist")
        if ok and playlist_name.strip():
            playlist_name = playlist_name.strip()
            if any(btn.text() == playlist_name for btn in self.playlist_buttons):
                QMessageBox.warning(self, "중복된 이름", "이미 존재하는 플레이리스트 이름입니다.")
                return
            music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
            playlist_folder = os.path.join(music_folder, playlist_name)
            try:
                os.makedirs(playlist_folder, exist_ok=True)
                self.add_playlist_button(playlist_name)
                QMessageBox.information(self, "성공", f"'{playlist_name}' 플레이리스트가 생성되었습니다.")
            except Exception as e:
                QMessageBox.critical(self, "오류", f"플레이리스트 생성 중 오류: {str(e)}")

    def add_playlist_button(self, playlist_name):
        playlist_btn = QPushButton(playlist_name)
        playlist_btn.setObjectName(f"playlist_{len(self.playlist_buttons)}")
        playlist_btn.clicked.connect(lambda: self.select_playlist(playlist_name))
        playlist_btn.setContextMenuPolicy(Qt.CustomContextMenu)
        playlist_btn.customContextMenuRequested.connect(
            lambda pos: self.show_playlist_context_menu(playlist_btn, playlist_name, pos)
        )
        insert_index = self.ui.verticalLayout_6.count() - 2
        self.ui.verticalLayout_6.insertWidget(insert_index, playlist_btn)
        self.playlist_buttons.append(playlist_btn)

    def show_playlist_context_menu(self, button, playlist_name, pos):
        menu = QMenu(self)
        rename_action = QAction("이름 변경", self)
        rename_action.triggered.connect(lambda: self.rename_playlist(button, playlist_name))
        delete_action = QAction("삭제", self)
        delete_action.triggered.connect(lambda: self.delete_playlist(button, playlist_name))
        menu.addAction(rename_action)
        menu.addAction(delete_action)
        menu.exec(button.mapToGlobal(pos))

    def rename_playlist(self, button, old_name):
        new_name, ok = QInputDialog.getText(self, "이름 변경", "새 이름:", text=old_name)
        if ok and new_name.strip() and new_name.strip() != old_name:
            new_name = new_name.strip()
            if any(btn.text() == new_name for btn in self.playlist_buttons if btn != button):
                QMessageBox.warning(self, "중복된 이름", "이미 존재하는 플레이리스트입니다.")
                return
            try:
                music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
                old_path = os.path.join(music_folder, old_name)
                new_path = os.path.join(music_folder, new_name)
                os.rename(old_path, new_path)
                button.setText(new_name)
                if self.current_playlist == old_name:
                    self.current_playlist = new_name
                    self.ui.playBox.setTitle(f"Play List - {new_name}")
            except Exception as e:
                QMessageBox.critical(self, "오류", f"이름 변경 실패: {str(e)}")

    def delete_playlist(self, button, playlist_name):
        reply = QMessageBox.question(self, "삭제 확인", f"'{playlist_name}' 삭제하시겠습니까?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
            playlist_folder = os.path.join(music_folder, playlist_name)
            try:
                if os.path.exists(playlist_folder):
                    shutil.rmtree(playlist_folder)
                self.ui.verticalLayout_6.removeWidget(button)
                button.deleteLater()
                self.playlist_buttons.remove(button)
                if self.current_playlist == playlist_name:
                    self.current_playlist = None
                    self.ui.playBox.setTitle("Play List")
                    self.ui.musicList.clear()
            except Exception as e:
                QMessageBox.critical(self, "오류", f"삭제 실패: {str(e)}")

    def select_playlist(self, playlist_name):
        self.current_playlist = playlist_name
        self.ui.playBox.setTitle(f"Play List - {playlist_name}")
        self.load_playlist_songs(playlist_name)

    def load_playlist_songs(self, playlist_name):
        self.ui.musicList.clear()
        add_item = QListWidgetItem("+ Add")
        add_item.setData(Qt.UserRole, "ADD_BUTTON")
        self.ui.musicList.addItem(add_item)
        music_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music")
        playlist_folder = os.path.join(music_folder, playlist_name)
        if os.path.exists(playlist_folder):
            for file_name in os.listdir(playlist_folder):
                if file_name.lower().endswith(".mp3"):
                    item = QListWidgetItem(file_name[:-4])
                    item.setData(Qt.UserRole, os.path.join(playlist_folder, file_name))
                    self.ui.musicList.addItem(item)

    def on_music_item_clicked(self, item):
        if item.data(Qt.UserRole) == "ADD_BUTTON":
            self.add_song_to_playlist()
            return
        index = self.ui.musicList.row(item) - 1
        mp3_list = [self.ui.musicList.item(i).data(Qt.UserRole) for i in range(1, self.ui.musicList.count())]
        self.music_player.set_playlist(mp3_list)
        self.music_player.play_index(index)
        self.current_song_index = index + 1
        file_path = mp3_list[index]
        self.ui.nowTitleLabel.setText(os.path.basename(file_path))
        self.ui.nowArtistLabel.setText("Unknown")
        self.highlight_current_song(self.current_song_index)
        file_path = mp3_list[index]
        base_name = os.path.basename(file_path)

        metrics = QFontMetrics(self.ui.nowTitleLabel.font())
        elided = metrics.elidedText(base_name, Qt.ElideRight, self.ui.nowTitleLabel.width())

        self.ui.nowTitleLabel.setText(elided)

    def play_song_at_index(self, index):
        if index < 1 or index >= self.ui.musicList.count():
            return
        item = self.ui.musicList.item(index)
        self.on_music_item_clicked(item)

    def toggle_play_pause(self):
        self.music_player.toggle()
        if self.music_player.player.playbackState() == QMediaPlayer.PlayingState:
            self.ui.playBtn.setIcon(QIcon(icon("pause_icon.svg")))
        else:
            self.ui.playBtn.setIcon(QIcon(icon("play_icon.svg")))

    def play_previous(self):
        if self.current_song_index > 1:
            self.play_song_at_index(self.current_song_index - 1)

    def play_next(self):
        if self.loop_mode:
            self.play_song_at_index(self.current_song_index)
        elif self.current_song_index < self.ui.musicList.count() - 1:
            self.play_song_at_index(self.current_song_index + 1)

    def update_position(self, position):
        self.ui.playTimeSlider.setValue(position)
        total = self.music_player.player.duration()
        now = self.ms_to_time(position)
        full = self.ms_to_time(total)
        self.ui.playTimeView.setText(f"{now}/{full}")

    def update_duration(self, duration):
        self.ui.playTimeSlider.setMaximum(duration)

    def seek_position(self, position):
        self.music_player.player.setPosition(position)

    def check_auto_next(self, status):
        if status == QMediaPlayer.MediaStatus.EndOfMedia:
            self.play_next()

    def ms_to_time(self, ms):
        seconds = int(ms / 1000)
        return f"{seconds // 60}:{seconds % 60:02d}"

    def highlight_current_song(self, index):
        from PySide6.QtGui import QFont, QColor
        for i in range(self.ui.musicList.count()):
            item = self.ui.musicList.item(i)
            if i == index:
                item.setBackground(QColor("#005500"))
                item.setForeground(Qt.white)
                item.setFont(QFont("Arial", 10, QFont.Bold))
            else:
                item.setBackground(Qt.black)
                item.setForeground(Qt.white)
                item.setFont(QFont("Arial", 10, QFont.Normal))

    def add_song_to_playlist(self):
        if not self.current_playlist:
            QMessageBox.warning(self, "플레이리스트 선택", "먼저 플레이리스트를 선택해주세요.")
            return
        file_path, _ = QFileDialog.getOpenFileName(self, "음악 파일 선택", MUSIC_DIR, "MP3 Files (*.mp3);;All Files (*.*)")
        if file_path:
            file_name = os.path.basename(file_path)
            dest_folder = os.path.join(os.path.dirname(MUSIC_DIR), "resources", "music", self.current_playlist)
            dest_path = os.path.join(dest_folder, file_name)
            if os.path.exists(dest_path):
                reply = QMessageBox.question(self, "중복", f"'{file_name}' 이미 존재. 덮어쓸까요?", QMessageBox.Yes | QMessageBox.No)
                if reply != QMessageBox.Yes:
                    return
            shutil.copy2(file_path, dest_path)
            self.load_playlist_songs(self.current_playlist)

    def toggle_loop_mode(self):
        self.loop_mode = not self.loop_mode
        self.update_loop_icon()

    def update_loop_icon(self):
        icon_path = "single_vector_icon.svg" if self.loop_mode else "loop_icon.svg"
        self.ui.PlaybackBtn.setIcon(QIcon(icon(icon_path)))

    def open_download_ui(self):
        dialog = DownloadDialog(self)
        dialog.exec()

    def open_slot(self):
        self.path = QFileDialog.getOpenFileName(self, 'Open File', fpath('*'), 'mp3 File(*.mp3);;All File(*.*)')
        if self.path[0]:
            with open(self.path[0], 'r', encoding='utf-8') as f:
                str_read = f.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MP3Player()
    window.show()
    sys.exit(app.exec())