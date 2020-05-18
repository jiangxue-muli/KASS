# Python 基本语法

在py中，可以选择标准的路径注释，当然你也可以选择不写，毕竟你非常的有性格。但是这可能会造成你的程序出错或出现很多蛋疼的问题，所以你可以加上以下注释在文件开头中，比如：

```
#!/usr/bin/python3
#!/usr/bin/env python3

env相对于前者而言，"env"是从环境中开始寻找python3解释器的，也就是说"env"先查找你的python3的环境，然后在查找所在的安装目录
```

---



###### 一，注释

```
# hELLO,World
prin ('Hello,World') # 注释

“”“
Hello
World
"""
print ('Hello,worl') # 注释 
```



###### 二，缩进规则

```
if True:
	print ('1')
else:
	print ('2')
```



###### 三，多行分离

```、
"\"
print ('Hello,\nworld!') # 此时 world将会在第二行打印而不是与Hello同一行
```



###### 四，数字（Number）类型

在Py中，有四种类型：整数、布尔型、浮点数、复数

| 类型   | 名称    | 描述                                           |
| ------ | ------- | ---------------------------------------------- |
| 整数   | int     | 如果只有”1“只有一个整数类型的int，表示为长整型 |
| 布尔   | bool    | 比如 True                                      |
| 浮点数 | float   | 比如 1.23 、3E-2                               |
| 复数   | complex | 比如 1 + 2j、1.1 + 2.2j                        |
|        |         |                                                |

###### 六，字符串（String）

​	__单引和双引__

```
在py中，单引号和双引号，都是完全相同的
print ('Hello,world')
pring ("Hello,world")
```

​	

​    __转义字符__

```
转义字符”\“
print ('hello,\'world') # 则打印为 hello,world

"r" “raw” 即 “raw string”
print(r,'Hello,world\n!') # 此时”\n参数将会正常输出为 ”hello,world\n!“
```

​	

​	__字符串__

```
字符串可以用“+”运算符连接起来，也可以使用 “*”作为运算符重复
而在Py中，一共有两种方式索引方式，比如下图：


| 0 | 1 | 2 | 3 | 4 | 从左往右开始
| - | 从右往左开始

字符串的语法格式为 变量[头下标：尾下标：步长]

string = 'String'
print(string[0]) 		# 输出地一个字符 为‘S’
print(string[0:-1]) 	# 输出0～-1的字符，为“Strin”
print(string[0:-2])		# 输出0～-2的字符 为“StrI”
print(string[1:])		# 从1～-0的字符 为“tring”
print(string[2:4])		# 输出 2～4 的字符，为“ri”
print(string * 5) 		# 输出结果x5次打印

print(string + ' Hello')#字符传和‘Hello’一起输出为“String Hello”

切记在py中，字符串不能改变，也没有单独的字符类型，一个字符就是长度为“1”的字符串。
```



###### 七，空行及 一码多代 和 input and 代码组代码块

​	__空行__

```
空行
空行主要用来分离代码区域,配合注释会大大提高代码的阅读效果。而在py运行之中，是不会将空行所执行的，这就像对于注释，但空行又不是注释。就比如：

print('Hello')

print('World!')

则打印结果为：
Hello
World
```



​	__一行多代__

```
"一行多代"指的是一行中写进了很多代码，而主要用到的则是 “;”，使用分号进行分割代码，比如：

import sys;hello = ' Hello'; sys.stdout.write(hello + '\n')
# 打印结果为 Hellp
```

​	

​	__代码组或代码块__

```
代码快和代码组就相对与 从关键字开始，然后一“:”结束，该行之后或多行代码构成的代码组，比如：

if code_set:
    set
elif code_set:
    set
elif code_set:
    set
```



​	__input__

```
input可以理解为的等待用户输入，然后继续执行一段代码，或者直接退出

input("root>")

此时你的终端大概为以下的样子
|---------------------------+
| root>						/
----------------------------+
```



###### 八，输出样式

```
在py中，py的输出都是换行的，如果想做到同一行 输出需要用到 end=" "才能做到。

h = '1'
a = '2'
print(h,end=" ")
print(a,end=" ")

输出结果为 1 2
```



###### 九，导入模块

在py中，导入模块可以使用 <kbd>import</kbd> 或 <kbd>form xxx import</kbd> 在适当的环境中可搭配使用



将整个模块导入格式为：<kbd>import xxx</kbd>



将某一个模块某个函数导入：<kbd>form 模块 import 函数</kbd>



将某个函数导入多个函数：<kbd>form 模块 import 函数,函数</kbd>



从某个模块中的函数全部导入：<kbd>form 模块 import xxx*</kbd>



