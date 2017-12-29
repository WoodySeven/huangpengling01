#!/usr/bin/env python
import os


##从文件中读数据
def file_write_read():
    """
    文件读、写，的步骤：
    1.打开文件
    2.读/写
    3.关闭文件
    """
    fn = open("名单","rb")
    print(fn.read())
    fn.seek(0)
    content = fn.readlines()  ## 读取所有行并返回列表
    print(content)
    for i in content:
        print(i.decode("utf-8").strip())
    fn.close()


##把数据写入到文件
    fp = open("名单.txt", "wb")
    address = ["中国","美国","新加坡"]
    for i in address:
        fp.write("{}\n".format(i).encode("utf-8"))

    fp.close()

if __name__ == "__main__":
    file_write_read()



