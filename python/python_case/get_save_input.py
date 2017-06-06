# coding:utf-8
if __name__ == '__main__':
    fp = open('test1.txt', 'w')
    string = input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('test1.txt', 'r')
    print(fp.read())
    fp.close()
