import homework08
l = int(input("请输入长度："))
w = int(input("请输入宽度："))
# 实例化类
r = homework08.Rectangle(l, w)
# 求周长
r.get_perimeter()
# 求面积
r.get_area()
