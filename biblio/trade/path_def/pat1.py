from pathlib import Path
import os,sys

d1=("file","plot","serie")
for st1 in d1:
  path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+'\\').parent.parent, st1)
  sys.path.append(path)
  # print(path)