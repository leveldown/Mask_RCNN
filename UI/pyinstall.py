import  os
import sys
sys.setrecursionlimit(10000)
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['E:/Anaconda/Python_workspace/Mask_RCNN/UI/main.py', '-w', '-F', '--icon=Amnesia.ico']
    run(opts)