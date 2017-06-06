# coding:utf-8
str = 'qiuhaiyang'
newstr = []
for s in str:
    if s == 'i' or s == 'a':
        continue
else:  # 因为要在for循环执行完才能执行else部分，所以最后一个字符s被添加到列表中
    newstr.append(s)
print(newstr)
