import time
def creatfilesize(n):
    local_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
    #file_name = "C:\测试大量文件与大文件\大文件\\"+str(local_time)+".txt"
    file_name = "C:\测试大量文件与大文件\大文件\\" + str(local_time) + ".txt"
    bigFile= open(file_name, 'w',encoding='utf-8')
    bigFile.seek(1024*1024*1024*n)
    bigFile.write('test')
    bigFile.write("test")
    bigFile.close()


if __name__ == '__main__':
    n = int(input("输入你要生成的文件大小（单位为G）:"))
    creatfilesize(n)

