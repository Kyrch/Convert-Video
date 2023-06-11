import winreg
import subprocess
import sys
import os

class RegisterKey:

    def __init__(self):
        self.command = RegisterKey.create_command()
        self.context = RegisterKey.add_context_menu_to_formats(self)

    def create_command():
        python_path = os.path.dirname(sys.executable) + '\python.exe'
        script_path = os.path.dirname(os.path.abspath(__file__)) + '\_convert_video.py'
        command = f'"{python_path}" "{script_path}" "%1"'

        return command

    def create_context_menu(self):
        key_path = r"Software\Classes\SystemFileAssociations\video\shell\ConvertVideo\Command"
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)

        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, self.command)
        winreg.CloseKey(key)
        RegisterKey.add_context_menu_to_formats()

    def add_context_menu_to_formats(self):
        formats = ['.webm', '.mp4', '.mkv', '.mov', '.avi', '.wmv', '.avchd', '.flv', '.f4v', '.swf', '.m2ts']

        for format in formats:
            key_path = fr"Software\Classes\SystemFileAssociations\{format}\shell\ConvertVideo\Command"

            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, self.command)
            winreg.CloseKey(key)

        subprocess.call(["ie4uinit.exe", "-show"])

        print('Keys created')