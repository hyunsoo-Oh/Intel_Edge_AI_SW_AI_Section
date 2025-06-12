import sys
import os
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from gui.mainWindow import MP3Player


def main():
    """메인 애플리케이션 실행"""
    app = QApplication(sys.argv)

    # 애플리케이션 정보 설정
    app.setApplicationName("YouTube MP3 Player")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("MP3Player")

    # 메인 윈도우 생성 및 표시
    main_window = MP3Player()
    main_window.show()

    # 애플리케이션 실행
    sys.exit(app.exec())

if __name__ == "__main__":
    main()