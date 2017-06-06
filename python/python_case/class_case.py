# coding:utf-8
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_info(self):
        print('%s\'s score is %d.' % (self.__name, self.__score))


stu=Student('hyqiu',100)
stu.print_info()