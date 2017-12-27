#!/usr/bin/env python
import os


def crawl_dirname():
    path = "E:\python\plsqldev715\Demo"
    list_path = os.listdir(path)
    print(list_path)
    fp = open("myfile.txt","wb")
    for i in list_path:
        fp.write("{}\n".format(i).encode("utf-8"))
    fp.close()
    abspath = os.path.abspath("myfile.txt")
    print(abspath)
    return

def crawl_path(path):
    myfile = "myfile.txt"
    if not os.path.exists(path):
        print("Error:文件或目录不存在")
        return
    if os.path.isfile(path):
        print("Error:不能是文件")
        return
    list_paths = os.listdir(path)
    with open("myfile.txt","wb") as fp:
        fp.write("\n".join(list_paths).encode("utf-8"))
        return myfile

def usage():
    print("please input path")
    print("eg. crwaler_path.py path_name")


if __name__ == '__main__':
    #crawl_dirname()
    crawl_path("E:\自动化测试\github\huangpengling01\selenium _demo")


