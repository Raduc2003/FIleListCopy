f= open("files.txt")
import shutil
path=f.readline()
path2=f.readline()
filetype = f.readline().strip()
for file in f:
    original = path.strip()
    target = path2.strip()

    original+='\\\\' + file.strip()+'.'+filetype
    target += '\\\\' + file.strip()+'.'+filetype
    try:
        shutil.copyfile(original,target)
    except:
        print("wrong file name or type").