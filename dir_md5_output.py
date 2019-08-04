#!/usr/bin/python
#encoding:utf-8
#author:Jack
# use for checking   dir's/files's md5 --->just for safe
import sys
import os
import hashlib

if len(sys.argv) < 2:
    print 'this script need a arv'
    sys.exit(0)

if not os.path.exists(sys.argv[1]) or not os.path.isdir(sys.argv[1]):
    print 'it is not exists or not a dir'
    sys.exit(1)


def getmd5(filename):
    m = hashlib.md5()
    mfile = open(filename, 'rb')
    m.update(mfile.read())
    mfile.close()
    md5value = m.hexdigest()
    return (md5value + "\t" + filename)

    # 遍历目标文件夹下的所有文件,最后返回一个flist列表


def all_files(root):
    flist = []
    for rootdir, subdirs, files in os.walk(root):
        for file in files:
            flist.append(os.path.join(rootdir, file))
    return flist


if __name__ == '__main__':
    #打开MD5file.txt
    #写入文件夹中各个文件的md5值
    outfile = open('md5file.txt', 'a+')
    flist = all_files(sys.argv[1])

# 将所有的文件循环取出,读取md5值写入文件
for fi in flist:
    res = getmd5(fi)
    outfile.write(res + '\n')
outfile.close()
