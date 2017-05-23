# Python简介
## 适合做哪些程序
+ 首选是网络应用，包括网站、后台服务等等。
+ 其次就是许多日常需要的小工具，包括系统管理员需要的脚本任务等等。
+ 把其他语言开发的程序再包装起来，方便使用。
## 缺点
+ 运行速度慢（Python是解释型语言，在执行的时候是一行行的翻译成机器码的，所以很慢）
+ 代码不能加密（编译型语言不存在代码被反推的问题，解释型的语言就相当于发布源代码）
## 输入和输出
+ print:输出；后面加多个字符串用逗号隔开，也可以连成一串输出
+ raw_input:获取用户输入，并返回一个变量
## 基础
Python采用缩进方式来形成代码块。
+ 注释：以#开头
+ 以冒号：结尾时，缩进的语句被视为代码块
+ **数据类型**：
    * 整数：和其他语言表示一致，有时候使用十六进制比较方便
    * 浮点数：运算会存在四舍五入的误差
    * 字符串：''或者""都可以表示字符串，结果是一样的。
        - 转义字符
        - r'':表示''内部的字符串默认不转义
        - """...""":表示多行内容
    * 布尔值：True、False。可以使用and,or,not来进行运算，对应着&&,||,!
    * 空值：None，不是0，
    * 常量：用全部大写来表示，
+ 编码问题：
    * ASCII:通常是一个字节，最早的编码
    * Unicode：通常是两个字节，整合大部分的编码形成的一套编码
    * utf-8:把Unicode编码转化为“可变长编码”的utf-8编码
        - encode：Unicode->utf-8
        - decode: utf-8->Unicode
    * 格式化：使用%来表示
        - %s:字符串
        - %d:整数
        - %f:浮点数
        - %x:十六进制
        - %%：%
+ list和tuple：
    * list是一个有序的集合，可以随时添加和删除其中的元素
        - 最后一个索引：len(classes)-1或者classes[-1]
        - 末尾追加元素：append(value)
        - 追加到指定位置：insert(index,value)
        - 删除末尾元素：pop([index]),index是可选的，填的话就删除指定位置的元素
        - 要把某个元素替换，可以直接赋值：classes[i]='qiuhy'
        - list里面的数据类型可以不同，也可以是另一个list
        - 空list的长度为0
    * tuple也是一种有序列表，初始化之后就不能修改了。
        - 获取元素的方法和list是一样的
        - tuple更安全，所以如果可能，能用tuple代替list就尽量用tuple
        - 定义的时候必须初始化赋值
        - 元组只有一个元素的时候必须加一个逗号，如(1,)，用于消除和小括号(1)之间的歧义。
        - tuple不变的意思是tuple中的元素指向是不变的，但是里面如果有一个list，list里面的内容是可以改变的。
+ 条件判断和循环
    * if、elif、else：后面的判断只要非零数值、非空字符串、非空list就判断为True
    * for...in:依次把list或tuple中的每个元素迭代出来
    * range()函数：range(value)=>生成的是0~value-1的数；range(num1,num2)=>num1~num2-1的数；range(num1,num2,num3)=>num3表示的是步长，就是生成一个间隔num3的等差数列。
    * while循环
    * raw_input获取的输入永远是string，想要转化成需要的数值，需要转化，比如：int(),可以转化成整数，如果转化不了就会报错。
+ 使用dict和set
    * dict：字典，使用键-值存储，查找速度快。
        - 一个key只能对应一个值
        - 如果key不存在，程序就会报错
        - 检查key是否存在：1.key in dict,返回bool；2.dict.get(key[,value]),返回None或者value
        - 要删除一个key，使用dict.pop(key)的方法，但是不是删除的最后一个这点和list不同，因为dict是无序的。
        - 查找插入速度快，需要占用大量的内存
        - dict是一种空间换时间的方法；dict的key必须是不可变的，所以list不能作为key；这种通过key计算位置的算法成为哈希算法(hash)
    * set：
        - 只存键
        - 需要用list初始化赋值，但是显示的时候，只显示内部值。set([1,2,3])
        - 重复的值会自动过滤掉
        - add(value)和remove(value)用于添加删除元素
        - set可以看成数学上的无序和无重复元素的集合，因此两个set可以做交集、并集等操作，set1 & set2:交集；set1 | set2:并集
    * 不可变对象：调用本身方法的时候不会修改原本的对象，而是会新创建一个对象。修改后返回。
## 函数（当代码出现有规律的重复时，就要考虑使用函数封装；函数是一种最基本的代码抽象的方式）
    * 函数调用：知道函数名称和参数信息就可以直接调用。
    * 定义函数：
        - 使用def定义函数，使用return返回结果。没有return会返回None；return None可以简写成return
        - 空函数：使用pass，pass可以用来做占位符，让程序可以先运行起来。
        - 参数检查：数据类型检查可以使用isinstance(args,(type1,type2))实现，返回错误可以使用raise TypeError(msg)
        - 返回多个值：返回多个值其实是返回一个tuple，但是在语法上可以省略括号，在接收的时候，多个值按顺序赋值。
    * 函数的参数：
        - 默认参数：def getInfo(name,sex,age=6):pass 默认参数必须放在后面，否则会报错。默认参数必须指向不可变对象。
        - 可变参数：def getSum(*nums):pass   在参数前面加一个*表示参数是可变的，可以添加任意个参数。如果已经有一个list或者tuple要调用一个可变参数，可以getSum(*(1,2,3,4)),使用这种形式。
        - 关键字参数：def person(name,age,**other),关键字参数在函数内部自动组装为一个dict。也可以直接传一个dict，要def person(name,age,**dict)这样使用。
        - 参数组合：顺序必须是：必选参数、默认参数、可变参数、关键字参数。对于任何参数，基本上都可以类似func(*args,**kw)这样的方式去调用。
    * 递归函数：
        - 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
        - 解决递归调用栈溢出的方法是通过尾递归优化，尾递归是指在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
        ```python
        def fact(n):
            return fact_iter(n,1)
        def fact_iter(num,product):
            if num==1:
                return product
            return fact_iter(num-1,num*product)
        ```
        - 大多数编程语言没有针对尾递归做优化。
## 高级特性
    * 切片：list、tuple、string都可以使用切片。
    ```python
        L=[1,2,3,4,5,6,7,8,9,0]
        L[value1:value2:value:3]
        #value1:开始切的位置，如果是0，可以省略
        #value2：结束位置，省略不写就复制了整个对象
        #value3：表示隔几个取一个值,数的时候把自己也算上
    ```
    * 迭代：Python中使用for...in来迭代。如何判断对象是否可以迭代
    ```python
        #引入collections模块的Iterable类型判断
        from collections import Iterable
        isinstance(object,Iterable)
        #判断object是否可以迭代，是就返回True。否则相反
        
        #实现下标循环
        for i,value in enumerate(object):
            print i,value
        #默认情况下dict迭代的是key，如果要迭代value：for value in d.itervalues();如果要同时迭代key和value，可以用 for k,v in d,iteritems
        arr={"1":"1","2":"2","3":"3"}
        for k,v in arr.iteritems():
            pass
    ```
    在Python中，任何可以迭代的对象都是可以用for...in来迭代的。
    * 列表生成式(List Comprehensions)：
    ```python
        #下面就是列表生成式的写法，在写的时候把要生成的元素“x*x”放在前面，后面跟for循环，把list创建出来。
        [x*x for x in range(1,11)]
        #后面还可以加判断条件
        [x*x for x in range(1,11) if x%2 == 0 and not x==2]
        #还可以使用双层循环
        [m+n for m in 'ABC' for n in 'XYZ']
    ```
    * 生成器(generator)：一遍循环一遍计算的机制，为了不生成没用的浪费空间的list。但是只能使用一遍。
        - 创建：1、把列表生成式的[]换成()即可。2、yield，如果一个函数中包含yield关键字，那么这个函数就是生成器。
        - 执行流程：函数是顺序执行，遇到return或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回。再次执行时从上次返回的yield语句处继续执行。（每次只执行一个yield，再次调用next()的时候，接着上一次执行。）总的来说generator比较像C#中的IEnumberable，只有在遍历的时候才去执行查询语句。
        - 使用：一般定义generator之后，不会去调用next()来查询。会使用for...in来遍历generator
## 函数式编程

## 使用模块
    任何模块的第一个字符串都被视为模块的文档注释。__author__='XXX'，把作者名字写进去。
    - 使用模块
        * 导入模块：import sys   或者 from xxx import xxx  (导入部分功能)
        * 导入之后就会获取一个模块的变量，可以利用这个变量去调用相应的方法或者属性。
        ```python
            if __name__=='__main__':
                test()
        ```
        当在命令行运行hello模板文件时，Python解释器会把一个特殊变量__name__置为__main__,如果在其他地方导入该hello模板，if判断就会失效。因此这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
        ```python
            try:
                import cStringIO as StringIO
            except ImportError:
                import StringIO
        ```
        * 作用域：
            - 正常的函数和变量名是公开的，可以直接引用。
            - __XXX__:特殊变量，一般有特殊用途，我们自己的变量不要这么命名。
            - _XXX和__XXX:这样的函数或变量就是非公开的，不应该被直接引用。
            - 外部不需要引用的函数都定义成private，只有需要的才定义为public。
    - 安装第三方模板
    官方现在推荐使用pip来安装新的模板。
    - 使用__future__,把下一个新版本的特性导入到当前版本