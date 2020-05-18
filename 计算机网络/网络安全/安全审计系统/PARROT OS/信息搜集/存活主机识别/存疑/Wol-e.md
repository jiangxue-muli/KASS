# Wol-e

Wol-e是一款网络唤醒工具，当目标主机处于睡眠状态时。可使用Wol-e进行唤醒，当一个主机处于睡眠状态时，该目标主机并不是服务全部关闭的情况，而是属于半开启状态。



_——by Nathaniel Carew_

---



#### 什么是WOL？

网络唤醒（WOL，Wake-on-LAN）,是一种电源管理功能，如果存在网络活动。则允许设备将操作系统从待机或睡眠模式下进行唤醒。

为此，IBM也为许多主板厂商提供了一套明确的网络唤醒标准，该标准允许网络管理员远程打开PC机电源，便于网络管理员进行文件升级，资源跟踪和设备清点等工作。

---



#### 一，参数介绍

###### -m 唤醒单台主机

-m 目标MAC地址 -b 目标地址/网关地址 -p 端口 -k 密码



###### -s -i 网卡

-s 嗅探网络中的WOL请求和密码 -i 监听指定网卡范围



###### -s -p 端口

使用Wol-e文件名为“bfmac.lst”中的地址进行供电，默认端口为“9”



###### -f

检测苹果设备在网络上的WOL网络呼唤，将会输出到屏幕中，并将结果写入到“AppleTargrts.txt”文件中



-fa 

尝试唤醒所有在/usr/share/wol-e/AppleTargets.txt.目录下的地址，并向列表中的每一个客户端发送一个WOL数据包，wol-e会告诉你尝试发送了多少个客户端



#### 二，命令实例

wol-e -m 00:0c:29:b4:7f:fc -b 192.168.11.255 -p 520 -k 00:12:34:56:78:90

向目标192.168.11.255网关发送网络唤醒，端口为520，对方主机密码为“001234567890”

> 根据官方文档所记载：If a password is required use the -k 00:12:34:56:78:90 at the end of the above command.
>
> 貌似仅仅支持数字密码，使用使用其他密码将会报错，如果对方目标主机没有密码的话可将-t参数去掉既可

![image-20200421135307516](/home/kun/.config/Typora/typora-user-images/image-20200421135307516.png)



wol-e -s -i vmnet8 

嗅探vmnet8网络中的WOL请求和密码，并将所有请求显示在终端中。并且村书/usr/share/WOL-e/WolClientstxt中

![image-20200421140433312](/home/kun/.config/Typora/typora-user-images/image-20200421140433312.png)

![image-20200421140523754](/home/kun/.config/Typora/typora-user-images/image-20200421140523754.png)



wol-e -a -p 20
在唤醒对方的数据包中使用的目标端口统一为 “20”

![image-20200421142358804](/home/kun/.config/Typora/typora-user-images/image-20200421142358804.png)



目标地址都将存放在"bfmac.lst"文件总，为wol-o发送唤醒请求成功时所记录，如果手动添加格式应为“00:01:02:03”

![image-20200421142532509](/home/kun/.config/Typora/typora-user-images/image-20200421142532509.png)



-f 

> 没有苹果设备，不演示，如果您有相关的实验环境且完成请联系 backsunli@yeah.net 进行补充



-fe

> 没有苹果设备，不演示，如果您有相关的实验环境且完成请联系 backsunli@yeah.net 进行补充



