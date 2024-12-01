from os import listdir
from shutil import copyfile

nextDay = max([int(f[0:2]) for f in listdir(".") if f[0:2].isdigit() and f.endswith(".py")]) + 1
copyfile("00.py", f"{nextDay:02d}.py")
copyfile("inputs/00_sample.txt", f"inputs/{nextDay:02d}_sample.txt")
copyfile("inputs/00_test.txt", f"inputs/{nextDay:02d}_test.txt")
