# Amap

> 识别运行端口上的应用程序

这是Amap的公开发布。Amap是圣诞节的下一代扫描工具。它试图识别应用程序，即使它们运行在与正常端口不同的端口上。

它还识别非ascii应用程序。这是通过发送触发数据包，并在响应字符串列表中查找响应来实现的。

如果没有包含触发器和响应的填充数据库，该工具就毫无价值，所以我请求您帮助我们填充数据库。怎么做？

每当一个客户端应用程序连接到一个服务器时，某种握手就被交换了(至少通常是这样。例如，Syslogd不会说什么，snmpd也不会没有正确的社区字符串)。无论如何，amap会将第一个返回的数据包与签名响应列表进行比较。

实际上非常简单。事实上，至少对大多数协议来说，这真的很简单。

现在，通过amap，您可以识别在端口3442上运行的SSL服务器，以及在端口23上运行的Oracle侦听器。

对于未知协议，您可以使用amapcrap(向audp、tcp或ssl端口发送随机垃圾)来非法响应，然后将其放入appdefs.trig和appdefs.resp文件中。





_——by van Hauser and DJ RevMoon / THC <amap-dev@thc.org>_

---



###### 一，帮助手册	

[CN]:翻译

```
语法:AMAP[-A |-B |-P |-W][-1BushHudQv][[-m]-o &lt; file &gt;][-D &lt; file &gt;][-T/-T秒] [-c cons] [-C重试] [-p协议][-I &lt; file &gt;][目标端口[端口]...]

模式：
-A	映射应用程序:发送触发器和分析响应(默认)
-B	只需抓住横幅，不要发送触发器
-P	没有横幅或应用程序的东西-是一个(完全连接)端口扫描仪

选择：
-1	仅向端口发送触发器，直到第一次识别。演讲！

-6	使用IPv6而不是IPv4

-b	打印回应的ascii横幅

-i	文件 要从中读取端口的文件Nmap机器可读输出文件

-u	命令行上指定的端口是UDP(默认为TCP)

-R	不要识别RPC服务

-H	不要发送标记为潜在有害的应用程序触发器 

-U	不要转储未识别的响应(最好是脚本)

-d	转储所有响应

-v	详细模式，使用两次(或更多次！)进行调试(不推荐:-)

-q	不要报告关闭的端口，也不要将其打印为未识别的端口

-o	文件	[-m]将输出写入文件文件，-m创建机器可读输出

-c	CONS要建立的并行连接数(默认32，最大256)

-C	重试次数 连接超时时重新连接的次数(参见-T)(默认为3)

-T	秒 以秒为单位的连接超时(默认为5

-t	秒 以秒为单位的响应等待超时(默认为5)

-p  原型 仅发送此协议的触发器(例如ftp)



目标端口要扫描的目标地址和端口(除-i之外)，用法提示:建议使用选项“-bqv”，快速/紧急检查时添加“-1”。
amap是识别目标端口上的应用协议的工具。注意:这个版本不是用SSL支持编译的！
用法提示:建议使用选项“-bqv”，快速/紧急检查时添加“-1”。

amap v5.4 (c) 2011 by van Hauser <vh@thc.org> www.thc.org/thc-amap
```



[EN]:官方

```
Syntax: amap [-A|-B|-P|-W] [-1buSRHUdqv] [[-m] -o <file>] [-D <file>] [-t/-T sec] [-c cons] [-C retries] [-p proto] [-i <file>] [target port [port] ...]
Modes:
  -A         Map applications: send triggers and analyse responses (default)
  -B         Just grab banners, do not send triggers
  -P         No banner or application stuff - be a (full connect) port scanner
Options:
  -1         Only send triggers to a port until 1st identification. Speeeeed!
  -6         Use IPv6 instead of IPv4
  -b         Print ascii banner of responses
  -i FILE    Nmap machine readable outputfile to read ports from
  -u         Ports specified on commandline are UDP (default is TCP)
  -R         Do NOT identify RPC service
  -H         Do NOT send application triggers marked as potentially harmful
  -U         Do NOT dump unrecognised responses (better for scripting)
  -d         Dump all responses
  -v         Verbose mode, use twice (or more!) for debug (not recommended :-)
  -q         Do not report closed ports, and do not print them as unidentified
  -o FILE [-m] Write output to file FILE, -m creates machine readable output
  -c CONS    Amount of parallel connections to make (default 32, max 256)
  -C RETRIES Number of reconnects on connect timeouts (see -T) (default 3)
  -T SEC     Connect timeout on connection attempts in seconds (default 5)
  -t SEC     Response wait timeout in seconds (default 5)
  -p PROTO   Only send triggers for this protocol (e.g. ftp)
  TARGET PORT   The target address and port(s) to scan (additional to -i)
amap is a tool to identify application protocols on target ports.
Note: this version was NOT compiled with SSL support!
Usage hint: Options "-bqv" are recommended, add "-1" for fast/rush checks.
```

----



###### 二，模式

![image-20200501234101329](/home/kun/.config/Typora/typora-user-images/image-20200501234101329.png)

_A (APPLICATION MAPPING)：映射应用程序，发送触发器和分析相应，为Amap默认模式_

_B (BANNER)：之抓住横幅，不发送触发器_

_P (PORTSCAN)：没有横幅或是应用程序的东西，是一个（完全链接端口扫描仪）_

> 你也可以理解为-P模式就是为了检测对方端口是否开启的
>
> _Port on 192.168.11.138:445/tcp is OPEN_
>



---



###### 三，命令实例

![image-20200501210509900](/home/kun/.config/Typora/typora-user-images/image-20200501210509900.png)

amap 192.168.11.138 445

查找对方开放的445端口对应的相关协议及应用。

> 如果你想要查看一些非常详细的端口信息，可以通过http://zsdk.org.cn/zsdk/445.html 来查看445端口的详细信息及相关方面的漏洞



![image-20200501213250607](/home/kun/.config/Typora/typora-user-images/image-20200501213250607.png)

amap -u -o 192 192.168.11.138 445

使用udp模式对目标445端口进行检索，并将结果以人类可读的形式导出

> ![image-20200501213616490](/home/kun/.config/Typora/typora-user-images/image-20200501213616490.png)
>
> amap -m -o 192 192.168.11.138 445
>
> 将检索之后的结果以机器可读的形式导出



![image-20200501222111749](/home/kun/.config/Typora/typora-user-images/image-20200501222111749.png)

amap -c 35 -C 1 -T 1 -t 192.168.11.138

设置CONS（面向连接服务）建立并发数为35,anap默认为“35～256”	，重试连接数目为“1”[^默认为3,单位为秒]，连接超时时间为”1“，等待超时时间为”1“[^-T与-t默认为3 。单位为秒]



> 面相连接服务，在通信双方进行通信时，要事先建立一条通信线路，其过程主要有建立链接，使用链接和释放链接三个过程。就比如TCP连接，也属于面向连接的一种。
>
> 而面向连接服务的特点就是，你如果想连接我，那你必须给我建立一条连接线路。然后当你用完了这个管道的时候，那你需要关闭这个管道
>
> 
>
> 这就跟你买房一样，你可以自己慢慢联想一下，首付就是建立链接，还款就是使用链接，还款完后就是关闭链接。



amnp -v 192.168.11.138 445

详细模式，第一次可能会比较慢，当你多尝试几次的话，那就可以享受到用户体验了。



> 远程过程调用协议（RPC，Remote Procedure Call Protocol），他是一种通过网路哦从远程计算机程序上请求服务，而不需要了解网络底层技术的协议。
>
> 该协议主要用于允许一台计算机的程序访问另一台计算机的子程序，而开发人员无需为此特地搞一个交互式作用的编程。



amap -R 192.168.11.138 445

不识别PRC服务。



> amap -q 192.168.11.138 445
>
> 不报告关闭的端口，也不要将其打印为未识别的端口





> ![img](https://pic.baike.soso.com/ugc/baikepic2/21285/20200224142416-1277807046_jpeg_1155_815_264649.jpg/0)
>
> ASCII(American Standard Code for Information Interchange，美国信息交换标准代码)是基于拉丁字母的一套电脑编码系统，主要用于显示现代英语和西欧语言，他是通用的信息交换标准，并同等与国际标准ISO/IEC 646
>
> 
>
> 而ACSII横幅，就类似与下图：
>
> ![在命令行创建ASCII艺术文字横幅](http://mos86.com/wp-content/uploads/2017/06/ascii-art-text.jpg)
>
> 当然你可以使用banner 生成一个类似的



amap -b 192.168.11.138 445

打印回应的ascii横幅



> 转储(Dump)
>
> 转储就是将一个动态易丢失的数据保存为静态不易改变的数据。



![image-20200501225029737](/home/kun/.config/Typora/typora-user-images/image-20200501225029737.png)

amap -d -o zs 192.168.11.138 445

将所有响应数据转储到zs文本文件之中

> amap -U 192.168.11.138 445
>
> 转储为识别的响应 （最好配合-o）一起用



> 触发器（Trigger）是一个特殊的存储过程，他的执行不是由程序掉通用，也不是手工启动。而是当某一个事件触发的。而简单的可以理解为，与表时间和相关特殊的存储过程。



> amap -1 192.168.11.138
>
> 仅向目标端口发送触发器，直到第一次识别。
>
> 
>
> amap -p ftp 192.168.11.138 445
>
> 发生一个ftp类型的触发器
>
> 
>
> amap -H 192.168.11.138 445 
>
> 不要发送标记为潜在有害的程序触发器





