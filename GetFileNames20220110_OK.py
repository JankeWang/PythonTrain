import os,re
##################################定义函数##################################### 
#获取路径下所有文件名
def F_GetAllFileName(file_dir):
    AllFileNames = os.listdir(file_dir)
    print(AllFileNames)
#逐一获取文件名
def F_OneByOneGetAllFileName(file_dir):
    i =0
    for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
        print("文件名：", str(i) +'  '+ files)
        i+=1
#检查路径合法
def F_CheckPathRight(file_dir):
    from pathlib import Path
    Resout= Path(file_dir)
    print("检查结果：", Resout.exists())
#################################执行区域#######################################        
MyPaths ='D:/'
F_CheckPathRight(MyPaths)
F_GetAllFileName(MyPaths)
F_OneByOneGetAllFileName(MyPaths)
