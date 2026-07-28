import os

print(f"cwd is: {os.getcwd()}")
import pathlib

print(pathlib.Path.cwd())  # current working directory
print(pathlib.Path.home())  # home directory
print(pathlib.Path(__file__).parent)  # directory of the current script
print(pathlib.Path(__file__).resolve())
