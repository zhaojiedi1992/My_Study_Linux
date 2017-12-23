import os.path
import os
import os,shutil

def my_copytree(src, dst):
    """Recursively copy a directory tree using copy2().
    Modified from shutil.copytree
    """
    base = os.path.basename(src)
    dst = os.path.join(dst, base)
    names = os.listdir(src)
    if not os.path.exists(dst):
        os.mkdir(dst)
    for name in names:
        srcname = os.path.join(src, name)
        try:
            if os.path.isdir(srcname):
                my_copytree(srcname, dst)
            else:
                shutil.copy2(srcname, dst)
        except:
            error.traceback()
            raise
def get_files(dir):
    results=[]
    for root,dirs,files in os.walk(dir):
        for file in files:
            
            results.append(os.path.join(root,file))
    return results

def replace(file_path, old_str, new_str):  
  try:  
    f = open(file_path,'r+',encoding='UTF-8')  
    all_lines = f.readlines()  
    f.close()
    f=open(file_path,'w',encoding='UTF-8')
    f.seek(0)  
    f.truncate()  
    for line in all_lines:  
      line = line.replace(old_str, new_str)  
      f.write(line)  
    f.close()  
  except Exception as e:
      print(e)


source=r'E:\ZhaojiediProject\github\My_Study_Linux\rstdoc\build\html'
source_dir=os.path.dirname(source)
dst=r"E:\ZhaojiediProject\github\zhaojiedi1992.github.io"
files = get_files(source)
files = [ i for i in files if i.endswith(".html")]

for file in files:
    print(file+"\n")
    replace(file,"_static","static")
    replace(file,"_sources","sources")
print("finish")

try:    
    os.rename(os.path.join(source,"_static"),os.path.join(source,"static"))
    os.rename(os.path.join(source,"_sources"),os.path.join(source,"sources"))
except:
    pass
names = os.listdir(source)
for i in names:
    if os.path.isdir(os.path.join(source,i)):
        my_copytree(os.path.join(source,i), dst)
    else:
        shutil.copy2(os.path.join(source,i), dst)
