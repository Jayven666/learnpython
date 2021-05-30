# 1.提醒用户输入自己的英文名字，然后保存到字典中（以name为key）,将用户输入的英文名字翻转，继续保存到刚才的字典中（以new_name为key）
# 将字典中用户的正常的英文姓名赋值给变量real_name,告知客户“您的英文名字是：” + 变量,“您的英文名字翻转是：” + 字典里获取
# # 创建一个空字典
# dic = {}
# en_name = input("请输入英文名：")
# # 添加键值对到dic字典
# dic['name'] = en_name
# # 反转英文名
# en_name_reverse = en_name[::-1]
# # 添加键值对到dic字典
# dic['new_name'] = en_name_reverse
# # 将姓名赋值给real_name
# real_name = en_name
# # 输出
# print("您的英文名是:%s\n您的英文名字反转是:%s" % (real_name,en_name_reverse))

# 2.提醒用户依次输入数学、语文、英语、综合四门的成绩，按照输入的成绩排序，告诉用户“您的最高的一门成绩是：”xx （不用告诉用户是哪一科）
# # 创建一个空字典
# dic = {}
# a = int(input("请输入数学成绩："))
# b = int(input("请输入语文成绩："))
# c = int(input("请输入英语成绩："))
# d = int(input("请输入综合成绩："))
# # 添加键值对到字典中
# dic.update({"数学": a, "语文": b, "英语": c, "综合": d})
# # 按成绩降序排序
# maxscore = sorted(dic.values(), reverse=True)
# # 输出
# print("您最高的一门成绩是：%s" % maxscore[0])

# 3.使用input让用户依次输入两个数字, 计算两个数字的和并显示.
# num1 = float(input("请输入第一个数字："))
# num2 = float(input("请输入第二个数字："))
# # 求和, %.2f指保留小数点后2位
# sum_num = num1 + num2
# print("和为:%.2f" % sum_num)

# 4.使用Python输出99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (j, i, j * i), end=' ')
#     print()

# 5.用python实现冒泡算法，给你一个包含若干值的列表，将他们从小到大排序输出（不能用sort或者sorted,自己用代码实现）
# eg:
# maopao([2,1,8,4,3,6])
# 输出结果：[1,2,3,4,6,8]
# 冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。它重复地走访过要排序的元素列，依次比较两个相邻的元素，
# 如果顺序（如从大到小、首字母从Z到A）错误就把他们交换过来
# list1 = [2, 1, 8, 4, 3, 6]
# # 执行轮数=列表长度-1
# for i in range(len(list1) - 1):
#     # 每一轮比较次数=列表长度-1-已经排好的个数
#     for j in range(len(list1) - 1 - i):
#         # 判断并交换位置
#         if list1[j] > list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]
# print(list1)

# 6.猜数字游戏
# 代码中生成一个随机整数. 然后用户输入数字后, 程序提示用户的输入是高了还是低了. 直到用户猜中这个数字,  游戏结束. 提示,
# random模块的randint函数能够帮助我们生成随机整数.
# # 导入模块
# import random
# # 生成随机数
# correct_num = random.randint(1, 100)
# # 创建循环并进行判断
# while True:
#     # 猜测的数字
#     guess_num = int(input("请猜一个整数:"))
#     if guess_num == correct_num:
#         print("恭喜你猜对了，游戏结束！")
#         break
#     elif correct_num < guess_num <= 100:
#         print("数字猜大了，请继续输入")
#     elif correct_num > guess_num >= 1:
#         print("数字猜小了，请继续输入")
#     else:
#         print("输入有误，请继续输入")

# 7.打开一个txt文本，将第一题内容写入此文本，读取一个不存在的文件，不能让程序停下来，而是能够继续读取存在文件里的文本内容，并输出
# # 创建了一个07.txt文本文件，并把第一题内容放入01.txt文本文件
# with open("01.txt", "r", encoding='UTF-8') as file01:
#     r = file01.read()
# with open("07.txt", "w") as file07:
#     file07.write(r)
# print("写入完成")
#
# # 读取一个不存在的文件夹，会报错FileNotFoundError
# try:
#     with open("test.txt", "r", encoding='UTF-8') as test07:
#         r = test07.read()
#         print(r)
# except Exception as e:
#     print("文件找不到！")
#     try:
#         with open("07.txt", "r") as test:
#             print(test.read())
#     except Exception as e:
#         print(e)
# # 创建test.txt文件，并写入内容"123"
# def create_text(name, msg):
#     path = "./" + name + ".txt"
#     file = open(path, "w")
#     file.write(msg)
#     file.close()
# create_text("test", "123!")

# 8.创建一个包，包下面创建一个模块,模块里定义一个长方形类，实例化时需要传入参数：长、宽（使用__init__方法）
# 拥有两个方法：
# 1)求周长
# 2)求面积
# 再创建一个模块，导入上一个类，实例化这个类，调用他的两个方法

# 90
# num = int(input("请输入一个整数n："))
# nums = input("请输入n个整数：")
# # 根据,进行切割存入列表中
# numlist = nums.split(",")
# print(numlist)
# # 批量转换成int类型
# for i in range(len(numlist)):
#     numlist[i] = int(numlist[i])
# print(numlist)
# # 将列表中的数字进行增序排序变成新列表
# newList = sorted(numlist)
# # 使用abs函数获取绝对值
# dif = abs(newList[0] - newList[1])
# # 循环取两两之差的值
# for i in range(len(newList)):
#     # 最后一个数不继续取差值，循环结束
#     if i == len(newList)-1:
#         break
#     # 如果任意两数之差的绝对值小于了第一对结果dif，dif就等于新的最小值
#     if abs(newList[i] - newList[i+1]) < dif:
#         dif = abs(newList[i] - newList[i+1])
# print(dif)

# 91
with open("bcbx_exam.txt", "r", encoding='UTF-8') as file:
    r = file.read()
print(r.count('bcbx'))

print("测试从pycharm上传代码到GitHub上")





