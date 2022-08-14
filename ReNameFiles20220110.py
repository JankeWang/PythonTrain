import os,re

os.listdir(）
def file_name(file_dir):
    for files in os.listdir(file_dir):  # 不仅仅是文件，当前目录下的文件夹也会被认为遍历到
        print("files：", files)


#from pathlib import Path
#print(Path.home())
#ddd= Path('D:/')
#print(ddd.exists())


# encoding:utf-8
##
# 文件名如:
# 贺龙传奇d+[有声下吧www.ysx8.com].mp3
##
#fs=os.listdir('单田芳_贺龙传奇')
#for f in fs:
#  ######方法一：partition获取无用字符
#  #1.将文件名以'['符分为3部分
#  #ls=f.partition('[')
#  #2.ls[0]为需要文件名，因此获取ls[1:]
#  #dirtystring = ''.join(ls[1:])
#  #3.开始替换
#  #newname=f.replace(dirtystring, '') + '.mp3')
#  #os.rename('单田芳_贺龙传奇/' + f, newname)
#  ######方法二：正则获取无用字符
#  dirtymatch = re.search(r'[.*?]', f)
#  if dirtymatch:
#    dirtystring=dirtymatch.group(0)
#    newname=f.replace(dirtystring, '') + '.mp3'
#    os.rename('单田芳_贺龙传奇/' + f, newname)
#

    #注意：可以直接用re.sub方法进行正则替换掉文件名中不需要字符
