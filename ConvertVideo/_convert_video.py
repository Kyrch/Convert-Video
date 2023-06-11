import subprocess
import sys
import os

def convert_video():
    print(sys.argv)
    os.system("PAUSE")
    input_file = sys.argv[1]

    format = input("Choose a format to convert (e.g. mp4, webm): ")
    output_file = input_file.split('.')[0] + "." + format
    command = f'ffmpeg -i "{input_file}" -vcodec copy -acodec copy "{output_file}"'
    subprocess.call(command, shell=True)

convert_video()