# 数字（Number）

数字类型主要用于存储数值，数据类型是不允许改变的，如果想改变数字类型的值，需要重新分配内存空间。



​	在进行赋值的时候，也会同时创建一个数字对象：

```python
>>> num = 10
>>> num2 = 20
>>> num3 = 30
>>> num
10
>>> num2
20
>>> num3
30
>>> 
```

​	

​	删除变量

```python
# 单个删除
del num

# 多个删除
del num2,num3
```



###### 一，数字类型转换

> ​	整数（Int）通常被肠胃整型或证书，不带任何小数点。
>
> ```python
> int(a) #将a抓换为整数
> ```
>
> 
>
> ​	浮点型（Float）由整数和部分小数组成。
>
> ```python
> float(a)	#转换为浮点型
> ```
>
> 
>
> ​	负数（Complex）由部分你虚数部分组成。
>
> ```python
> complex(a)	#传唤为复数
> ```

	> ````python
	> >>> a = 10.10
	> >>> int(a)			
	> 10
	> >>> float(a)
	> 10.1
	> >>> complex(0)
	> 0j
	> >>> 
	> ````



###### 二，数学函数

| 函数   | 描述             | 返回值 |
| ------ | ---------------- | ------ |
| abs(a) | 返回数字的绝对值 | 10     |



