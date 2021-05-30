# 8.创建一个包，包下面创建一个模块,模块里定义一个长方形类，实例化时需要传入参数：长、宽（使用__init__方法）
# 拥有两个方法：
# 1)求周长
# 2)求面积
# 再创建一个模块，导入上一个类，实例化这个类，调用他的两个方法

class Rectangle:
    def __init__(self, width=1, length=1):
        self.width = width
        self.length = length

    # 求周长函数
    def get_perimeter(self):
        perimeter = 2*(self.length+self.width)
        print("周长是：%s" %perimeter)

    # 求面积函数
    def get_area(self):
        area = self.length * self.width
        print("面积是：%s" %area)


# 把执行代码放入执行入口
if __name__ == "__main__":
    l = int(input("请输入长度："))
    w = int(input("请输入宽度："))
    # 传参
    r = Rectangle(l, w)
    # 求周长
    r.get_perimeter()
    # 求面积
    r.get_area()



