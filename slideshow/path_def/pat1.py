from pathlib import Path
import os,sys

d1=("file","bus","plot","serie","trade","app")
for i1 in d1:
  i1="biblio\\"+i1
  path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+"\\").parent.parent, i1)
  if (path not in  sys.path) : sys.path.append(path)
  # print(path)
  
# print(sys.path)