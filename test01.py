# 数字
# num = 10
# print(type(num), num)
# num1 = '10'
# print(type(num1),num1)
# num2 = 10.00
# print(type(num2),num2)
#
# num += 2
# print(num)  #12
# num *= 10
# print(num)  #120
#
# m = 10
# print(type(m),m)    #<class 'int'> 10
# m = float(m)
# print(type(m),m)    #<class 'float'> 10.0
#
# m=5.99999999999999999999999
# print(type(m),m)
# m = int(m)
# print(type(m),m)

# 字符串
# a = """I say "stupid"，you say 'nice!'."""
# print(a)
#
# a =  " I say: \n 'nice!'."
# print(a)
#
# a="abcd12"
# print(a[0:])

# 字符串反转
# a = "abcd12"
# print(a[::-1])
#
# a = "ab"*4
# print(len(a))
#
# a="ab"*4
# print(a.count("ab"))

# 格式化
# date = 10
# name = "jayven"
# print("今天是%d号,%s,欢迎登录" %(date,name))
#
# a=True
# print(type(a),a)
#
# # date = input("请输入日期：")
# # name = input("请输入姓名：")
# # print("今天是%d号,%s,欢迎登录" %(date,name))
# # 这里会报错，因为虽然输入的是数字但实际上传的还是字符串，所以不能和%d匹配
#
# # 解决方法1：把%s改成%d
# date = input("请输入日期：")
# name = input("请输入姓名：")
# print("今天是%s号,%s,欢迎登录" %(date,name))
# # 解决方法2：把date转为int型
# date = int(input("请输入日期："))
# name = input("请输入姓名：")
# print("今天是%d号,%s,欢迎登录" %(date,name))

# import sys
# print (sys.getdefaultencoding())

# a=1
# b=2
# print(a%b)

# listA = [1, 2, 3, 4]
# print(listA)
# print(listA[-1])
# tupleB = (1, 2, 3, 4)
# print(tupleB)
#
# t=(2)
# #print(len(t))
# print(type(t))
# l=[2]
# print(len(l))
# print(type(l))
#
# a=["a","A","b","3"]
# print(sorted(a))
#
# a=["4444","333","22","1"]
# print(sorted(a,key=len))
#
# a=[1,2,3,4]
# a[0]=100
# print(a)

# 元组不能修改
# a=(1,2,3,4)
# a[0]=100
# print(a)

# a=[1,3,4,2]
# a.sort()
# print(a)
#
# a=[1,2,3,4]
# a.insert(2,5)
# print(a)
# a=[1,2,3,4]
# a.append(5)
# print(a)
#
# a=[1,2,2,2,3,4]
# a.remove(2)
# print(a)
#
# a=[1,2,2,2,3,4]
# print(a.count(2))
#
# a=[1,2,2,2,3,4]
# del a[-1]
# print(a)
#
# a=([1,2,3],True,1,"abc",["a","b","c","d"])
# a[0][-1] = 4
# a[4][0] = "e"
# print(a)

# a={"ip":"192.168.0.105"}
# print(a["ip"])
# a["port"]=80
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())
# del a["port"]
# print(a)
# b=a.pop("ip")
# print(b)
# print(a)
# 键为元组，元组里含有字典也不能作为键
# b={({1:"123"},2,3):"123"}
# print(b)

# a=["aa","bb","cc"]
# b=":"
# print (b.join(a))
#
# a="aa,bb,cc"
# print(a.split(","))
#
# a="你好，这是啥?"
# print(a.startswith("你好"))
# print(a.endswith("?"))
#
# a="     hello world \n   "
# print(a.strip())
#
# a="hello world"
# print(a.find("ell"))
#
# a="hello world"
# print(a.replace("world","earth"))
#
# a="hello world"
# print(a.isalpha())
# a="1234"
# print(a.isdigit())

# name="jayven"
# print(id(name),type(name),name)

# if 3 > 2:
#     print('ojbk')
# elif 4 > 5:
#     print('nook')
# else:
#     print('nicemff')

# n=1
# while 3>2:
#   print("bcbx",n)
#   n+=1
#   if n>5:
#     break

# name = "jayven"
# n = 1
# for b in name:
#     print("这是第%d次循环:" % n, end="")
#     print(b)
#     n += 1
# list = [1,2,3,"a","b","c"]# m = 1
# for a in list:
#     print("这是第%d次循环：" %m,end="")
#     print(a)
#     m+=1

# di = {"ip":"10.0.10.1","port":3306}
# j = 1
# for k in di.items():
#     print("这是第%d次循环："%j,end="")
#     print(k)
#     j+=1

# a=["a","b","c",1,2,3]
# for k in range(len(a)):
#     print(k)

# print(round(4.987,1))
# a=[b**2 for b in range(4)]
# print(a)

# list=[]
# for a in range(10):
#     if a % 2 !=0:
#         list.append(a)
# print(list)

# a=[b for b in range(10) if b%2!=0]
# print(a)

# def Add(x,y):
#   return x+y
# print(Add(1,2))
#
# def test2(**data):
#   print(data)
# test2(a="abc",b=123,c=True)
#
# handle = open("test02.py","r",encoding="utf-8")
# for line in handle:
#   print(line.strip())
#
# write_file = open("test02.py","w")
# write_file.write("dbqdbq\n")
# write_file.close()
# try:
#     list = [1,2,3,4]
#     print(list[5])
# except IndexError:
#     print("ERROR")
