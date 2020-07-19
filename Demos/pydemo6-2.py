#文件的基本处理
'''
第一步：文件打开
var = open(filename,mode)#var就是文件指针
mode:
r 只读，不存在时报错
w 只写，不存在时自动创建;存在时删除旧文件，创建新文件
a 附加到文件末尾

rb 只读二进制文件，不存在时不错
wb 只写二进制文件，不存在时自动创建
ab 附加到二进制文件末尾

r+ 读写

第二步：文件操作
    读取

    写入

    定位

    其他：追加、计算

第三步：文件关闭


eg：
打开一个numbers.dat的文本文件：infile = open("numbers.dat","r")

打开一个music.mp3的音频文件： infile = open("music.mp3","rb")


'''


'''
Python提供的文件读取的操作：
read():返回值为包含整个文件内容的一个字符串
readline():返回值为文件下一行内容的字符串
readlines():返回值为整个文件内容的列表，每项是以换行符为结尾的一行字符串

'''
#使用read()读取文件
def readFile1():
    fname = input("Please input the name of the file:")
    infile = open(fname,"r")
    data = infile.read()
    print(data)
    
#使用readline()读取文件的前5行
def readFile2():
    fname = input("Please input the name of the file:")
    infile = open(fname,"r")
    for i in range(4):
        line = infile.readline()
        #print(line)
        print(line[:-1])#这里使用切片操作是为了不在shell中打印出\n，否则每一行之间都会有一个空行
'''
Python的文件写入：
write():把含有文本数据或二进制数据块的字符串写入文件中
writelines()：针对列表操作，接受一个字符串列表作为参数，将它们写入文件，并且
              换行符不会被自动加入。

'''
#使用 writelines()方法写内容
def writeFile():
    fname = input("Please input the name of the file:")
    outfile = open(fname,'w')
    strlist = ["hello"," ","world!"]
    outfile.writelines(strlist)
    outfile.close()

    infile = open(fname,'r')
    content = infile.read()
    print("File content is:",content)


'''
文件遍历
通用代码框架；
(一)
file = open(someFile,"r")
for line in file.readlines():
    #处理每一行文件内容
file.close()

(二)
file = open(someFile,"r")
for line in file:    #可以这么做的原因是Python把文件本身当做一个行的列表
    #处理每一行文件内容
file.close()
'''
#文件遍历案例—使用通用文件遍历代码框架实现文件拷贝
def copyFile():
    #strip():用于移除字符串头尾指定的字符（默认为空格）,只要是字符串首尾的空格，多少个都可以删掉
    fname = input("Please input the file you want to COPY:").strip()

    infile = open(fname,'r')
    outfile = open(fname+"_copy2","w")
    
    for line in infile:
        outfile.write(line)

    infile.close()
    outfile.close()

    print("Done")

#不使用文件的遍历方法来复制文件，直接使用readlines()和writelines()
def copyFile2():
    fname = input("Please input the file you want to COPY:").strip()

    infile = open(fname,'r')
    outfile = open(fname+"_copy3","w")

    strlist = infile.readlines()
    outfile.writelines(strlist)

    infile.close()
    outfile.close()

def main():
    copyFile2()

main()
