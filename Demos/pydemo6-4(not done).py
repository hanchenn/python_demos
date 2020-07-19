#文件示例二：多文件读写
'''
思路：
1.将电话文件里的姓名、电话这两个字段分别取出放到列表list1中，
  邮箱文件进行相同操作，生成list2
2.新建列表3，在list3中添加表头
3.将list1存到list3中
4.将list2中的二维列表遍历加入到list3中，有相同名字则添加邮箱字段，没有相同字段在
  list3中新建一个list元素，电话字段为“------------”
5.

'''
def filePlus():
    file1 = open("file1.txt",'rb')#以二进制的方式读取文件，避免中文出现乱码
    file2 = open("file2.txt",'rb')
    
    lines1 = []
    lines2 = []
    file1.readline()#跳过文件第一行
    file2.readline()

    lines1 = file1.readlines()
    lines2 = file2.readlines()
    
    list1_name = []
    list1_tele = []
    list2_name = []
    list2_emai = []

    for line in lines1:
        elements = line.split()#注意：列表没有split方法，字符串有，split()的默认参数是空格
        list1_name.append(str(elements[0].decode("gbk")))
        list1_tele.append(str(elements[1].decode("gbk")))

    for line in lines2:
        elements = line.split()
        list2_name.append(str(elements[0].decode("gbk")))
        list2_emai.append(str(elements[1].decode("gbk")))

    #合并处理
    lines = []
    lines.append("姓名\t      电话\t      邮箱\n")
    
    
    
    
    print("hh")
    
def main():
    filePlus()

main()
