#coding=utf-8
'''
Created on 2016-7-10
 
@author: dogegg
'''
 
import os
import time
import datetime

def datelist(start, end):
    start_date = datetime.date(*start)
    end_date = datetime.date(*end)

    result = []
    curr_date = start_date
    while curr_date != end_date:
        result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))
        curr_date += datetime.timedelta(1)
    result.append("%04d%02d%02d" % (curr_date.year, curr_date.month, curr_date.day))
    return result


 
def nsfile(start, end):
    '''The number of new expected documents'''
    #判断文件夹是否存在，如果不存在则创建
    b = os.path.exists("E:\\NoteFile\\")
    if b:
        print "File Exist!"
    else:
        os.mkdir("E:\\NoteFile\\")
    #生成文件
    data=datelist(start, end)
    s=len(data)
    for i in range(0,s):
        filename = "E:\\testFile\\"+data[i]+".txt"
        f = open(filename,'w')
        testnote = data[i]
        f.write(testnote)
        f.close()
        #输出第几个文件和对应的文件名称
        print "file"+" "+str(i)+":"+str(data[i])+".txt"
        time.sleep(1)
    print "ALL Down"
    time.sleep(1)
 
if __name__ == '__main__':
    start = input("请输入需要生成的起始日期：example：(2016, 7, 28)")
    end = input("请输入需要生成的结束日期：example： (2016, 8, 3)")
    nsfile(start, end)
