from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtGui import QIcon, QKeyEvent
from PySide6.QtCore import Qt
from gui.download_ui import Ui_Dialog
from gui.constants import icon
from download.youtube_search import YoutubeSearchModel, YoutubeCardDelegate, search_youtube
from download.download import download_audio


class DownloadDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("YouTube Download")
        self.setWindowIcon(QIcon(icon("download_icon.png")))

        self.ui.searchBtn.setIcon(QIcon(icon("search_icon.svg")))

        # 선택된 비디오 정보 저장
        self.selected_video = None

        # 검색 버튼 연결 및 엔터 연결
        self.ui.searchBtn.setIcon(QIcon(icon("search_icon.svg")))
        self.ui.searchBtn.clicked.connect(self.on_search)

        # 모델과 델리게이트 설정
        self.model = YoutubeSearchModel()
        self.delegate = YoutubeCardDelegate()

        self.ui.listView.setModel(self.model)
        self.ui.listView.setItemDelegate(self.delegate)
        self.ui.listView.doubleClicked.connect(self.on_double_click)
        self.ui.listView.clicked.connect(self.on_item_clicked)

        # 엔터 키 처리
        self.ui.searchEdit.returnPressed.connect(self.on_search)
        self.ui.listView.installEventFilter(self)

        # OK/Cancel 버튼 처리
        self.ui.buttonBox.accepted.connect(self.on_ok_clicked)
        self.ui.buttonBox.rejected.connect(self.reject)

    def on_search(self):
        """검색 실행"""
        keyword = self.ui.searchEdit.text().strip()
        if not keyword:
            QMessageBox.warning(self, "검색어 입력", "검색어를 입력해주세요.")
            return

        try:
            print(f"🔍 검색 중: {keyword}")
            results = search_youtube(keyword, max_results=10)
            self.model.update(results)
            print(f"✅ 검색 완료: {len(results)}개 결과")
        except Exception as e:
            print(f"❌ 검색 실패: {e}")
            QMessageBox.critical(self, "검색 오류", f"검색 중 오류가 발생했습니다:\n{str(e)}")

    def on_item_clicked(self, index):
        """리스트 아이템 클릭 시 선택 저장"""
        if index.isValid():
            self.selected_video = self.model.data(index, Qt.DisplayRole)
            print(f"🎯 선택됨: {self.selected_video['title']}")

    def on_double_click(self, index):
        """더블클릭 시 즉시 다운로드"""
        if index.isValid():
            data = self.model.data(index, Qt.DisplayRole)
            self.download_selected_video(data)
            self.accept()

    def on_ok_clicked(self):
        """OK 버튼 클릭 시 선택된 비디오 다운로드"""
        if self.selected_video:
            self.download_selected_video(self.selected_video)
            self.accept()
        else:
            QMessageBox.warning(self, "선택 필요", "다운로드할 음악을 선택해주세요.")

    def download_selected_video(self, video_data):
        """선택된 비디오 다운로드 실행"""
        try:
            video_id = video_data['video_id']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            title = video_data['title']

            print(f"🎵 다운로드 시작: {title}")
            print(f"🔗 URL: {video_url}")

            # 다운로드 진행 메시지
            QMessageBox.information(self, "다운로드 시작", f"'{title}' 다운로드를 시작합니다.")

            # 실제 다운로드 실행
            download_audio(video_url)

            print(f"✅ 다운로드 완료: {title}")
            QMessageBox.information(self, "다운로드 완료", f"'{title}' 다운로드가 완료되었습니다.")

        except Exception as e:
            print(f"❌ 다운로드 실패: {e}")
            QMessageBox.critical(self, "다운로드 오류", f"다운로드 중 오류가 발생했습니다:\n{str(e)}")

    def eventFilter(self, source, event):
        """listView에서 Enter 키 처리"""
        if source == self.ui.listView and isinstance(event, QKeyEvent):
            if event.type() == QKeyEvent.KeyPress and event.key() == Qt.Key_Return:
                index = self.ui.listView.currentIndex()
                if index.isValid():
                    self.on_double_click(index)
                    return True
        return super().eventFilter(source, event)