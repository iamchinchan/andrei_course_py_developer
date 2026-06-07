from PIL import Image
import sys
import os
from pathlib import Path
# print(f"path is: {os.getcwd()}")
# source_dir = sys.argv[1]
# dest_dir = sys.argv[2]
# print(source_dir,dest_dir)
source_dir = "../pokedex/"
dest_dir = "../new/"

source_dir = (Path(__file__).parent/source_dir).resolve()
dest_dir = (Path(__file__).parent/dest_dir).resolve()
print(source_dir,dest_dir)
print(type(source_dir))


dest_dir.mkdir(parents=True, exist_ok=True)
for file_path in source_dir.iterdir():
    # .is_file() ensures you skip subfolders and only target actual files
    if file_path.is_file():
        with Image.open(file_path) as img:
            img.save(f"{dest_dir}\\{file_path.name.split(".")[0]}.png","png")