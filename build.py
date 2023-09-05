import argparse
import subprocess

parser = argparse.ArgumentParser(add_help=False)

parser.add_argument(
    '-b', '--build_location', action='store_true',
    help='Build location for the created program')

args = parser.parse_args()


subprocess.call(r"pyinstaller --noconfirm --onedir --windowed --icon C:/Users/u28o53/Desktop/Python/Copy-tool/icon.ico --paths C:/Users/u28o53/Desktop/Python/Copy-tool/app --add-data C:/Users/u28o53/Desktop/Python/Copy-tool/extensions;extensions/ --add-data C:/Users/u28o53/Desktop/Python/Copy-tool/icon.ico;.  C:/Users/u28o53/Desktop/Python/Copy-tool/app/app.py --distpath C:/Users/u28o53\Desktop/Python/Copy-tool/build/built_app")

#subprocess.call(r"python -m PyInstaller --noconsole --name WorkLogger F:\KivyApps\WorkLogger\main.py", cwd=r"F:\KivyApps\WorkLogger_Dist")