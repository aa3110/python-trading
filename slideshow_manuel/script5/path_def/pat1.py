from pathlib import Path
import os,sys

d1="app"

i1="biblio\\"+d1
path =  os.path.join(Path(os.path.abspath(os.path.dirname(__file__))+"\\").parent.parent.parent, i1)
if (path not in  sys.path) : sys.path.append(path)
# print(path)
  
# print(sys.path)