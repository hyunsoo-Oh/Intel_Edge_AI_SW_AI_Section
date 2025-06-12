import os

# 기준 경로: 항상 gui/ 기준
BASE_DIR = os.path.dirname(__file__)
MUSIC_DIR = os.path.abspath(os.path.join(BASE_DIR, "../downloads"))
ICON_DIR = os.path.abspath(os.path.join(BASE_DIR, "../resources/icons"))

def icon(filename):
    return os.path.join(ICON_DIR, filename)

def fpath(folder):
    return os.path.join(MUSIC_DIR, folder)