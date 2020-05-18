# Xprobe2

Xprobe2是一款远程主机系统探查工具，可通过ICMP协议来获取指纹等信息。



_——by Ofir Arkin, Fyodor Yarochkin_

---



#### 一，帮助手册

[中英]:翻译

Xprobe2 v.0.3 Copyright (c) 2002-2005 fyodor@o0o.nu, ofir@sys-security.com, meder@o0o.nu
Xprobe2 v.0.3版权所有（c）2002-2005 fyodor@o0o.nu，ofir@sys-security.com，meder@o0o.nu

usage: xprobe2 [options] target
使用：xprobe2[选项]目标

Options:

选项：

-v                       Be verbose
-五

-r                       Show route to target(traceroute)
-显示到目标的路由（traceroute）

-p <proto:portnum:state> Specify portnumber, protocol and state.
-p<proto:portnum:state>指定端口号、协议和状态。

Example: tcp:23:open, UDP:53:CLOSED
示例：tcp:23:打开，UDP:53:关闭

-c \<configfile>          Specify config file to use.
-c \<config file>指定要使用的配置文件。

-h                       Print this help.
打印此帮助。

-o  <\fname>               Use logfile to log everything.
-o \<fname>使用日志文件记录所有内容。

-t <time_sec>            Set initial receive timeout or roundtrip time.
-t<time_sec>设置初始接收超时或往返时间。

-s <send_delay>          Set packsending delay (milseconds).
-s<send_delay>Set packsending delay（毫秒）。

-d \<debuglv>             Specify debugging level.
-指定调试级别。

-D \<modnum>              Disable module number \<modnum>.
-D \<modnum>禁用模块号 \<modnum>。

-M \<modnum>              Enable module number \<modnum>.
-M\<modnum>启用模块号\<modnum>。

-L                       Display modules.
显示模块。

-m \<numofmatches>        Specify number of matches to print.
-m\<numofmatches>指定要打印的匹配数。

-T \<portspec>            Enable TCP portscan for specified port(s).
-T\<portspec>为指定端口启用TCP端口扫描。

Example: -T21-23,53,110
示例：-T21-23,53110

-U \<portspec>            Enable UDP portscan for specified port(s).
-U\<portspec>为指定端口启用UDP端口扫描。

-f                       force fixed round-trip time (-t opt).
强制固定往返时间（-t opt）。

-F                       Generate signature (use -o to save to a file).
生成签名（使用-o保存到文件）。

-X                       Generate XML output and save it to logfile specified with -o.
-X生成XML输出并将其保存到用-o指定的日志文件中。

-B                       Options forces TCP handshake module to try to guess open TCP port
-B选项强制TCP握手模块尝试猜测打开的TCP端口

-A                       Perform analysis of sample packets gathered during portscan in
在中执行端口扫描期间收集的样本包分析

order to detect suspicious traffic (i.e. transparent proxies,
为了检测可疑流量（即透明代理，

firewalls/NIDSs resetting connections). Use with -T.
防火墙/NIDS重置连接）。与-T一起使用。

----



#### 二，模块介绍

| 类型                 | EN                | 描述                                          |
| -------------------- | ----------------- | --------------------------------------------- |
| PING                 | ICMP_ping         | ICMP回声发现模块                              |
| PING                 | Tcp_ping          | 基于TCP PING的发现模块                        |
| PING                 | Udp_ping          | 基于UDP PING的发现模块                        |
| 信息搜集(infogather) | Ttl_ping          | 基于TTL PING的TCP/UDP的TTL距离计算模块[^存疑] |
| 信息搜集(infogather) | Portscan          | TCP/UDP的端口扫描模块                         |
| 指纹(fingerprint)    | Icmp_echo         | ICMP回声请求指纹模块                          |
| 指纹(fingerprint)    | Icmp_tstamp       | ICMP时间戳请求模块                            |
| 指纹(fingerprint)    | Icmp_amask        | ICMP地址掩码请求指纹模块                      |
| 指纹(fingerprint)    | Icmp_info         | ICMP信息打印模块[^存疑]                       |
| 指纹(fingerprint)    | Icmp_port_unreach | ICMP端口无法到达时的指纹打印模块              |
| 指纹(fingerprint)    | Tcp_hshake        | TCP握手指纹模块                               |
| 指纹(fingerprint)    | Tcp_rst           | TCP RST指纹模块                               |
| 指纹(fingerprint)    | Smb               | SMB指纹模块                                   |
| 指纹(fingerprint)    | Snmp              | SNMPv2c指纹打印模块                           |

---



#### 三，命令实例

xprobe2 -b zsdk.org.cn

对目标进行详细的扫描

![image-20200421170901999](/home/kun/.config/Typora/typora-user-images/image-20200421170901999.png)



xprobe2 -r baidu.com

显示目标路径

![image-20200421185757102](/home/kun/.config/Typora/typora-user-images/image-20200421185757102.png)



xprobe2 -p tcp:80:open

指定端口号为80,协议为TCP，状态为“OPEN打开”

> open，全称“TCP open”其有意思为允许应用程序使用TCP/IP协议与客户端进行通讯。
>
> ---
>
> __四次挥手__
>
> ![img](http://pic.baike.soso.com/ugc/baikepic2/3967/20160727081543-1112779943.jpg/0)
>
> 
>
> TCP连接是双方的，因此需要逐个进行关闭，这原则是当一方完成他的数据发送任务后就可以发送FIN进行关闭这个方向的连接。
>
> 当收到了一个FIN则一味着这一方向的数据没有数据传输了，一个TCP连接在收到了一个FIN后仍然可以继续发送数据。首先关闭的一方将自执行主动挂比，而另一方则是被动关闭。
>
> 
>
> 1. 客户端发送了一个FIN，用来关闭服务的请求
>
> 2. 服务端收到了这个FIN，他发送了一个ACK，表示我已经确认，此时的确认序列号为1，一个FI将占用1个序列号，此时也是和SYN的共同点，SYN也是占用一个序列号。
>
> 3. 服务端关闭了客户端的连接，发送了一个FIN给客户端
> 4. 客户端返回ACK报文，并将确认号设置为收到的序列号并加1。.
>
> 
>
> 
>
> __CLOSED__
>
> 用于表示初始状态
>
> 
>
> __LISTED__
>
> 表示服务端的某一个SOCKET处于监听状态，告诉对方”我“可以接受连接
>
> 
>
> __SYN_RCVD__
>
> 表示接受到了SYN报文，在正常的情况喜爱SOCKET在建立连接时的三次握手状态下的一个中间状态。当接收到了客户端的ACK报文后，他会进入到一个ESTABLISHED的状态
>
> 
>
> __SYN_SENT__
>
> 与SYN_RCVD呼应，当客户端SOCKET执行CONNECTL连接时，首先会发出一个SYN报文，因此随即会进入SYN_SENT状态
>
> 
>
> __ESTABLISHED__
>
> 用于表示已建立链接
>
> 
>
> __FIN_WAIT_1__
>
>  等待对方的FIN报文，当SOCKET在ESTABLISHED状态时，想要主动关闭想对方发送了FIN报文，此时SOCKET即进入了FIN_WAIT_1状态
>
> 
>
> __FIN_WAIT_2__
>
> 表示在FIN_WAIT_2状态下的SOCKET表示半连接，当有一方请求连接close时，告诉对方只是暂时的连接，稍后会关闭
>
> 
>
> __TIME_WAIT__
>
> 表收收到对方的报文，并发送了ACK报文。之后等待2秒后回到CLOSED可用状态，
>
> 如果在FIN_WAIT_1状态下直接进入到TIME_WAIT状态
>
> 
>
> __CLOSING__
>
> 表示双方都关闭SOCKE连接，双方在同时发送FIN报文的情况下会出现此状况[^双方同时处于CLOSING状状态下]。
>
> 在正常的环境中，发送FIN报文后因先收到对方的ACK报文，然后在发送FIN报文，但是在CLOSING环境下并没有发送ACK报文，但是对方却收到了FIN报文。
>
> 
>
> __CLOSE_WAIT__
>
> 用于表示等待关闭，当对方关闭一个SOCKET后发送了一个FIN报文给自己，系统会好不留意的发送一个ACK报文给对方，此时会进入CLOSE_WAIT状态
>
> 此时如果没有数据要发送给对方的话，如果没有的话则可关闭这个SOCKET，发送FIN报文个对方也就是说直接关闭了链接，所以在CLOSE_WAIT模式下等待的是关闭链接。
>
> 
>
> __LAS_ACK__
>
>  表示被动关闭了一方发送的FIN报文后，最后等待对方的ACK报文。当收到了ACK报文后，则可以进入CLOSED初始状态状态。
>
> ---
>
> close ,  全程“TCP close”即TCP终止，主要分为：
>
> > 半关闭（Half-close）\  主动关闭（Active close）\ 被动关闭（Passive close）



![image-20200421190745920](/home/kun/.config/Typora/typora-user-images/image-20200421190745920.png)



xprobe2 -c zsdk.org.cn

使用配置文件对目标进行扫描

![image-20200421191744092](/home/kun/.config/Typora/typora-user-images/image-20200421191744092.png)



> xprobe2 -o zsdk zsdk.org.cn
>
> 使用日志文件zsdk 记录一切



> xprobe2 -t 10 zsdk.org.cn
>
> 设置初始接收或接受超时的时间
>
> 
>
> xprobe2 -s 10 zsdk.org.cn
>
> 设置发送包延迟为10
>
> 
>
> xprobe2 -d 3 zsdk.org.cn
>
> 设置一个调试级别
>
> 
>
> xprobe2 -m 5 zsdk.org.cn
>
> 设置一个匹配数为“5
>
> >  比如你将匹配数设置为 “1”那么xprobe2只在终端回显一行数据
>
> 
>
> xprobe2 -f 1 zsdk.org.cn
>
> 强制固定往返时间为1分钟
>
> 
>
> xprobe2 -B zsdk.org.cn
>
> 强制使用TCP握手模块猜测目标打开的端口



xprobe2 -D ping:icmp_ping zsdk.org.cn

禁止ping:icmp_ping模块

![image-20200421193544761](/home/kun/.config/Typora/typora-user-images/image-20200421193544761.png)



xprobe2 -M ping:icmp_ping zsdk.org.cn

只启用ping:icmp_ping模块对目标进行扫描

![image-20200421194050828](/home/kun/.config/Typora/typora-user-images/image-20200421194050828.png)



xprobe2 -L 

显示所有模块

![image-20200421194301064](/home/kun/.config/Typora/typora-user-images/image-20200421194301064.png)



xprobe2 -T 80-100 zsdk.org.cn

为指定的端口进行TCP端口扫描

![image-20200421220445986](/home/kun/.config/Typora/typora-user-images/image-20200421220445986.png)



xprobe2 -U 80 zsdk.org.cn

为指定的端口进行UDP扫描

![image-20200421221610468](/home/kun/.config/Typora/typora-user-images/image-20200421221610468.png)



xprobe2 -F zsdk.org.cn

生成签名和指纹[^可配合 "-o"参数进行使用]

![image-20200421222453751](/home/kun/.config/Typora/typora-user-images/image-20200421222453751.png)



xprobe2 -X -o xml zsdk.org.cn

将最终回显结果以XML形式输出到xml文件之中

![image-20200421223256236](/home/kun/.config/Typora/typora-user-images/image-20200421223256236.png)



xprobe2 -T 80-100 -A 192.168.11.137

对目标进行端口扫描，并从端口扫描的期间内对收集的数据包进行分析。

![image-20200421225723912](/home/kun/.config/Typora/typora-user-images/image-20200421225723912.png)

