# Netmask

这是一个方便的工具，用于生成几种常见的简洁的网络掩码格式。如果你曾经维护过不止几条规则的防火墙 在这里，您可以使用netmask来清理和归纳netadmin留给您的草率规则。它还将转换一种格式的网络掩码 换防火墙软件的那天。



_——http://trap.mtview.ca.us/~talby/_

---



###### 一，帮助手册

[中文]: 翻译

Usage: netmask spec [spec ...]

​	-h		帮助打印选项摘要
​	-v		版本打印版本号
​	-d		调试打印状态/进度信息
​	-a 		标准输出地址/网络掩码对	
​	-c		cidr输出cidr格式地址列表
​	-i	 	思科输出思科风格的地址列表	
​	-r	 	输出ip地址范围
​	-x		十六进制输出地址/网络掩码对
 	-o		八进制输出地址/网络掩码对
 	-b		二进制输出地址/网络掩码对	
​	-n		禁用地址的域名系统查找
​	-f		将参数视为输入文件

​		定义:
​			规格可以是以下任何一种:
​			地址
​			地址:地址
​			地址:+地址
​			地址/掩码	

​		地址可以是以下任何一种:
​				十进制数
​				0N八进制数
​				0xN十六进制数
​				N.N.N.N点状四边形
​				主机名dns域名
​				掩码是从左边设置为1的位数



[EN]:官方

Usage: netmask spec [spec ...] 
  -h, --help           Print a summary of the options 
  -v, --version         Print the version number 
  -d, --debug          Print status/progress information 
  -s, --standard         Output address/netmask pairs 
  -c, --cidr           Output CIDR format address lists 
  -i, --cisco          Output Cisco style address lists 
  -r, --range          Output ip address ranges 
  -x, --hex           Output address/netmask pairs in hex 
  -o, --octal          Output address/netmask pairs in octal 
  -b, --binary          Output address/netmask pairs in binary 
  -n, --nodns          Disable DNS lookups for addresses 
  -f, --files          Treat arguments as input files 
Definitions: 
  a spec can be any of: 
   address 
   address:address 
   address:+address 
   address/mask 
  an address can be any of: 
   N      decimal number 
   0N      octal number 
   0xN     hex number 
   N.N.N.N   dotted quad 
   hostname   dns domain name 
  a mask is the number of bits set to one from the left

---



###### 二，网络掩码（Netmas）



| 类型 | 格式           | 默认子网掩码  |
| ---- | -------------- | ------------- |
| A    | 节点 节点 节点 | 255.0.0.0     |
| B    | 网络 节点 节点 | 255.255.0.0   |
| C    | 网络 网络 节点 | 255.255.255.0 |
|      |                |               |

网络掩码（Netmas），又称子网掩码。主要用于从IP地址总提取的网络号或主机号，网络掩码就是结构为网络号，全都为1，主机号全部为0的IP地址。|

---



###### 三，命令实例

![image-20200426120102179](/home/kun/.config/Typora/typora-user-images/image-20200426120102179.png)

netmask -v 

查看netmask版本号



> netmask -d 192.168.11.137 
>
> 查看目标调试打印信息和进度	
>
> 
>
> netmask -r 192.168.11.137
>
> 输出IP地址范围
>
> ![image-20200426134415122](/home/kun/.config/Typora/typora-user-images/image-20200426134415122.png)
>
> 
>
> netmask -i 192.168.11.137
>
> 以cisco格式来输出
>
> ![image-20200426131702529](/home/kun/.config/Typora/typora-user-images/image-20200426131702529.png)



![image-20200426122458075](/home/kun/.config/Typora/typora-user-images/image-20200426122458075.png)



netmask -s 192.168.11.137

输出标准的IP和子网掩码

---



![img](http://pic.baike.soso.com/ugc/baikepic2/11922/20161225115427-880071911.jpg/0)

五类别域间路由选择（CIDR，Classless lnterDomain Routing），是一个在Internet上创建附加地址的方法，这些地址提供给服务器提供商（ISP），在由服务器我提供商（ISP）分配给客户，CIDR会将路由集合起来，使一个IP地址代表骨干提供商服务的几千个IP地址，从而解决了路由器的负载压力。

所有发送这些地址的信息包都被发生哦感到MCI或Springt等ISP上。在1990年时，Internet上大约有2000个路由，五年后internet上有3万多个路由。如果没有CIDR，路由器将不会支持Internet上的网站增多。

主要是因为CIDR采用的13~27位的可变网络ID，而不是A-B-C类的网络ID所固定的6、16、24位。



---



__进制输出__

[格式]:IP+子网掩码



netmask -x 192.168.11.137

以16进制输出信息

![image-20200426135429272](/home/kun/.config/Typora/typora-user-images/image-20200426135429272.png)



netmask -0 192.168.11.137

以八进制输出信息

![image-20200426135610718](/home/kun/.config/Typora/typora-user-images/image-20200426135610718.png)



netmask -d 192.168.11.137

以二进制的形式进行输出

![image-20200426135815374](/home/kun/.config/Typora/typora-user-images/image-20200426135815374.png)



---

netmask -n 192.168.11.137

禁止地址域名系统的查找	



netmask -f 1

读取文件中的内容并检索

![image-20200426141910500](/home/kun/.config/Typora/typora-user-images/image-20200426141910500.png)

