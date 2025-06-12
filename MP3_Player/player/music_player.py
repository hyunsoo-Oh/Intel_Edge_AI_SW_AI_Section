from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl

class MusicPlayer:
    def __init__(self):
        self.audio_output = QAudioOutput()
        self.player = QMediaPlayer()
        self.player.setAudioOutput(self.audio_output)
        self.audio_output.setVolume(0.5)
        self.current_index = -1
        self.playlist_items = []

    def set_playlist(self, items):
        self.playlist_items = items

    def play_index(self, index):
        if 0 <= index < len(self.playlist_items):
            self.current_index = index
            path = self.playlist_items[index]
            self.player.setSource(QUrl.fromLocalFile(path))
            self.player.play()

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def toggle(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.pause()
        else:
            self.play()

    def next(self):
        self.play_index(self.current_index + 1)

    def prev(self):
        self.play_index(self.current_index - 1)

    def set_volume(self, value):  # 0~100
        self.audio_output.setVolume(value / 100.0)