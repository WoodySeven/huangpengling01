#!/usr/bin/env python
import os
import sys

def file_write_read():
    fn = open("名单","rb")
    print(fn.read())
    fn.seek(0)
    content = fn.readlines()
    print(content)
    for i in content:
        print(i.decode("utf-8").strip())



def crawl_dirname(filepath):
    pathDir =  os.listdir(filepath)

# 读取文件内容并打印
def readFile():
    fb.write = open("myfile.txt","rb")
    for eachLine in fopen:
        fopen.write("{}\n".format(eachLine).encode("utf-8"))
    fopen.close()
    abspath=os.path.abspath("myfile.txt")
    print(abspath)
    return abspath

if __name__ == "__main__":
    #file_write_read()
    readFile()
    crawl_dirname(r"D:\github\autotest7")


