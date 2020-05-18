# OS

在Python中，你可以使用OS库来实现任何你想要的文件及文件夹和系统的操作。比如文件重命名，更改文件夹权限及新建文件夹等操作，而如果你想实现这个操作。只需要<kbd>os.mkdir()</kbd>这个简短的函数来实现新建文件夹操作。



###### 一，新建文件夹

```python
import os #	导入OS库
os.mkdir('Mkdir')	# 建立Mkdir目录
```

![image-20200517213420912](/home/kun/.config/Typora/typora-user-images/image-20200517213420912.png) 

​		

###### 二，写入文件

```python
import os
o = os.open('test_1.py'os.O.RDWR)	#指定目标文件并以读写模式打开

os.write(o.str.encode("Hello,world!"))	# 写入信息为“Hello,world!""
```



![image-20200517214327459](/home/kun/.config/Typora/typora-user-images/image-20200517214327459.png)



###### 三，删除文件

```python
import os
os.remove('test_1.py')	# 删除test_1.py文件
```



###### 四，删除目录

```python
import os
os.removedirs('/home/kun/Public/Projekt/Study/Mkdir') # 删除/home/kun/Public/Projekt/Study/Mkdir目录
```



###### 五，修改目录名

```python
import os
os.rename('1','yes')	#将目录名为”1"的重命名为“yes"
```

![image-20200517215418203](/home/kun/.config/Typora/typora-user-images/image-20200517215418203.png)



###### 五，重命名目录子文件/目录

```python
import os
os.renames('yes/20','yes/yes')	#将yes/20文件重命名为yes
```

![image-20200517220329486](/home/kun/.config/Typora/typora-user-images/image-20200517220329486.png)



当然你也可是重命名目录，比如：

```python
import os
os.renames(‘yes','no')	#将yes文件重新命名为no
```

![image-20200517220544251](/home/kun/.config/Typora/typora-user-images/image-20200517220544251.png)

