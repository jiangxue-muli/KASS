# Atk6-passive_discovery6

被动地嗅探网络并转储所有检测到的客户端IPv6地址。注意，在切换的环境中，您可以获得更好的结果
启动parasite6，但是这会影响网络。如果在接口之后指定了脚本名，则使用检测ipv6地址作为第一个和接口作为第二个选项。



_——by van Hauser_

---



#### 一，帮助手册

[中英对照]:翻译

语法:atk6-passive_discovery6 [-Ds] [-m maxhop] [-R前缀]接口[脚本]
Syntax: atk6 passive_discovery6 [- DS] [M maxhop] [R prefix] interface [Script]

选项:
Options:

-D也转储目标地址(不与-m一起工作)
-D also dumps the destination address (does not work with - M)

-s只打印地址，没有其他输出
-S only print address, no other output

被丢弃的目标的最大跳数可能已经丢失。
The maximum number of hops for dropped targets may have been lost.

0只表示局部的，通常最大取值为5
0 means local only, usually the maximum value is 5

-R前缀与链路本地前缀交换已定义的前缀
-Exchange defined prefix between R prefix and link local prefix

----



#### 二，命令实例

atk6-passive_discovery6 -D wlan0

启动转储目标地址，当有IPV6地址加入此网络中将会显示

![image-20200420170425350](/home/kun/.config/Typora/typora-user-images/image-20200420170425350.png)



atk6-passvice_discovery6 -Ds wlan

转储目标地址，但只显示目标加入此网段的IP地址

![image-20200420170929095](/home/kun/.config/Typora/typora-user-images/image-20200420170929095.png)



atk6-passive_discovery6 -m 10 vmnet8

目标可能离开的最大跳数为“10”

> 最大跳数是主要针对跳离是失量的路由协议，主要规定了一个路由最多能跳多少个路由，比如此时规定的最大跳数为“10”则通告这个路由之可以通过10次路由器.
>
> 如果超过了这10次的话，那么路由器将会认为在这个传送是不可达的。



atk6-passive_discovery6 -R FE80/::10 vmnet8

用链路本地前缀来交换定义的前缀



> > ```mermaid
> > graph LR
> > A[本地前缀]
> > A --> | FE80::/10 | 以定义的前缀
> > 
> > ```
>
> 链路本地地址“Link-local address”，前缀为FE80::/64 是一IPv6的一个概念 

![image-20200420175137024](/home/kun/.config/Typora/typora-user-images/image-20200420175137024.png)



> 如果有脚本可在网卡后面中填写，如：
>
> atk6-passive-discovery6 wlan benben.py



