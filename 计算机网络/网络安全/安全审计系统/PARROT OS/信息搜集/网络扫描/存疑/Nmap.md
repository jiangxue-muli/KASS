# Nmap

Nmap是一个网络映射程序，用于进行网络发现和安全审计，以新颖的方式来发现网络上有那些主机可用。并且还会扫描出该主机提供有那些服务和使用的是什么规则的过滤器和防火墙，还支持识别对方主机系统。

Nmap被设计为快速扫描大型网络，对但个主机扫描性能也非常优秀。并且除了原有的命令行可执行文件他还附带了一个高级用的图形用户界面和结果查看器（Zenmap），重定向和调试工具(Ncat)，还有一个比较扫描结果的实用程序（Ndiff），以及一个数据包生成和响应分析工具（Nping）。

于此之外，作为一个专业的网络扫描工具，你会在很多电影和电视剧上看到他的身影。比如电影《黑客帝国：重装上阵》、《死神4》。电视剧《亲爱的热爱的（烂片）》等影视作品。



_——https://nmap.org/_

---



###### 一，帮助手册

[CN]:翻译

```
PORT SPECIFICATION AND SCAN ORDER:nmap 7.80(https://nmap.org)
用法:nmap [扫描类型][选项]{目标规格}
目标规格:
可以传递主机名、IP地址、网络等。
例如：scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254

-iL <inputfilename >:					来自主机/网络列表的输入
-iR:								 	<主机数量>:选择随机目标
--exclude <host1[,host2][,host3],...>:	排除主机/网络
--excludefile <exclude_file>:			从文件中排除列表


主机发现:
-sL:		列出扫描-简单地列出要扫描的目标
-sn:		Ping扫描-禁用端口扫描
-Pn:		Ping扫描-禁用端口扫描

-PS/PA/PU/PY[portlist]:		对给定端口的TCP SYN/ACK、UDP或SCTP发现	
-PE/PP/PM:					CMP echo、时间戳和网络掩码请求发现探测
-PO[protocol list]:			IP协议Ping
-n/-R:
--dns-servers <serv1[,serv2],...>:	从不执行DNS解析/始终解析[默认：有时]
--system-dns:						指定自定义dns服务器
--traceroute:						到每个主机的跟踪跃点路径	

扫描技术:
-sS/sT/sA/sW/sM:		TCP SYN/Connect（）/ACK/Window/Maimon扫描
-sU:					UDP扫描
-sN/sF/sX:				TCP空、FIN和Xmas扫描
--scanflags <flags>:	自定义TCP扫描标志

-sI <zombie host[:probeport]>:		空闲扫描
-sY/sZ:								SCTP INIT/COOKIE-ECHO扫描
-sO:								IP协议扫描
-b <FTP relay host>:				FTP跳转扫描

端口规格和扫描顺序:
-p <port ranges>:					仅扫描指定端口
示例：-p22；-p1-65535；-p U:53111137，T:21-25，801398080，S:9

--exclude-ports <port ranges>		从扫描中排除指定端口
-F:									快速模式-扫描比默认扫描少的端口
-r:									连续扫描端口-不要随机化
--top-ports <number>:				扫描最常见端口
--port-ratio <ratio>:				扫描端口比<ratio>更常见


服务/版本检测:
-sV							探测打开的端口以确定服务/版本信息
--version-intensity <level>:从0（轻）设置为9（尝试所有探针）
--version-light:			最有可能的探头限制（强度2）
--version-all:				尝试每个探针（强度9）
-version-trace:				显示详细的版本扫描活动（用于调试）

脚本扫描:
-sC:						相当于--script=默认值
--script=<Lua scripts>:		<Lua scripts>是以逗号分隔的目录、脚本文件或脚本类别

--script-args=<n1=v1,[n2=v2,...]>		为脚本提供参数
--script-args-file=filename:			在文件中提供NSE脚本参数
--script-trace:							显示发送和接收的所有数据
--script-updatedb:						更新脚本数据库
--script-help=<Lua scripts>:			显示有关脚本的帮助
<Lua scripts>:是以逗号分隔的脚本文件列表，或脚本类别。

操作系统检测:
-O:					启用操作系统检测
--osscan-limit:		将OS检测限制在有希望的目标上
--osscan-guess:		更积极地猜测操作系统
 
时间和性能:
花费&lt; time &gt;的选项以秒为单位，或者附加“ms”(毫秒)，
s '(秒)、' m '(分钟)或' h '(小时)到该值(例如，30m)。

-T<0-5>		设置计时模板（越高速度越快）
--min-hostgroup/max-hostgroup <size>: 		并行主机扫描组大小
--min-parallelism/max-parallelism <numprobes>:		探针并行化

--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>:	指定探测往返时间。 

--max-retries <tries>:		限制端口扫描探测器重新传输的次数。
--host-timeout <time>:		超过此时间后放弃目标
--scan-delay/--max-scan-delay <time>:	调整探针之间的延迟
--min-rate <number>: 		每秒发送不慢于<number>的数据包
--max-rate <number>:		发送数据包的速度不超过每秒<number>


防火墙/入侵检测系统规避和欺骗:
-f; --mtu <val>:				片段包（可选w/给定mtu）
-D <decoy1,decoy2[,ME],...>:	用诱饵掩蔽扫描
-S <IP_Address>:				欺骗源地址
-e <iface>:						使用指定接口
-g/--source-port <portnum>:		使用给定的端口号
--proxies <url1,[url2],...>: 	通过HTTP/SOCKS4代理中继连接
--data <hex string>: 			将自定义负载附加到发送的数据包
--data-string <string>: 		将自定义ASCII字符串附加到发送的数据包
--data-length <num>:  			向发送的数据包追加随机数据
--ip-options <options>: 		使用指定的ip选项发送数据包
--ttl <val>:					设置IP time to live字段
--spoof-mac <mac address/prefix/vendor name>:		欺骗mac地址
--badsum:						使用伪造的TCP/UDP/SCTP校验和发送数据包


输出:
-oN/-oX/-oS/-oG <file>:		以normal、XML、s |<cript kIddi3格式输出扫描，以normal、XML、s |<cript kIddi3格式输出扫描，

oA <basename>:				同时以三种主要格式输出
-v:							提高详细程度（使用-vv或更大的效果）
-d:							提高调试级别（使用-dd或更多以获得更大的效果）
--reason:					显示端口处于特定状态的原因
--open:						仅显示打开（或可能打开）的端口
--packet-trace:				显示发送和接收的所有数据包
--iflist:					打印主机接口和路由（用于调试）
--append-output:			追加到而不是删除指定的输出文件
--resume <filename>:		恢复中止的扫描
--stylesheet <path/URL>:	将XML输出转换为HTML的XSL样式表
--webxml:					从Nmap.Org中引用样式表以获得更可移植的XML
--no-stylesheet:			禁止将XSL样式表与XML输出相关联


混杂:
-6:			启用IPv6扫描
-A:			启用操作系统检测、版本检测、脚本扫描和traceroute		
--datadir <dirname>:		指定自定义Nmap数据文件位置
--send-eth/--send-ip:		使用原始以太网帧或ip包发送
--privileged: 				假设用户是完全特权的
--unprivileged:				假设用户缺乏原始套接字特权
-V:							打印版本号			
-h:							打印此帮助摘要页。


例子:
nmap -v -A scanme.nmap.org
nmap -v -sn 192.168.0.0/16 10.0.0.0/8
nmap -v -iR 10000 -Pn -p 80

SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
```



[EN]:官方

```
Nmap 7.80 ( https://nmap.org )
Usage: nmap [Scan Type(s)] [Options] {target specification}
TARGET SPECIFICATION:
  Can pass hostnames, IP addresses, networks, etc.
  Ex: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
  -iL <inputfilename>: Input from list of hosts/networks
  -iR <num hosts>: Choose random targets
  --exclude <host1[,host2][,host3],...>: Exclude hosts/networks
  --excludefile <exclude_file>: Exclude list from file
HOST DISCOVERY:
  -sL: List Scan - simply list targets to scan
  -sn: Ping Scan - disable port scan
  -Pn: Treat all hosts as online -- skip host discovery
  -PS/PA/PU/PY[portlist]: TCP SYN/ACK, UDP or SCTP discovery to given ports
  -PE/PP/PM: ICMP echo, timestamp, and netmask request discovery probes
  -PO[protocol list]: IP Protocol Ping
  -n/-R: Never do DNS resolution/Always resolve [default: sometimes]
  --dns-servers <serv1[,serv2],...>: Specify custom DNS servers
  --system-dns: Use OS's DNS resolver
  --traceroute: Trace hop path to each host
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
PORT SPECIFICATION AND SCAN ORDER:
  -p <port ranges>: Only scan specified ports
    Ex: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
  --exclude-ports <port ranges>: Exclude the specified ports from scanning
  -F: Fast mode - Scan fewer ports than the default scan
  -r: Scan ports consecutively - don't randomize
  --top-ports <number>: Scan <number> most common ports
  --port-ratio <ratio>: Scan ports more common than <ratio>
SERVICE/VERSION DETECTION:
  -sV: Probe open ports to determine service/version info
  --version-intensity <level>: Set from 0 (light) to 9 (try all probes)
  --version-light: Limit to most likely probes (intensity 2)
  --version-all: Try every single probe (intensity 9)
  --version-trace: Show detailed version scan activity (for debugging)
SCRIPT SCAN:
  -sC: equivalent to --script=default
  --script=<Lua scripts>: <Lua scripts> is a comma separated list of
           directories, script-files or script-categories
  --script-args=<n1=v1,[n2=v2,...]>: provide arguments to scripts
  --script-args-file=filename: provide NSE script args in a file
  --script-trace: Show all data sent and received
  --script-updatedb: Update the script database.
  --script-help=<Lua scripts>: Show help about scripts.
           <Lua scripts> is a comma-separated list of script-files or
           script-categories.
OS DETECTION:
  -O: Enable OS detection
  --osscan-limit: Limit OS detection to promising targets
  --osscan-guess: Guess OS more aggressively
TIMING AND PERFORMANCE:
  Options which take <time> are in seconds, or append 'ms' (milliseconds),
  's' (seconds), 'm' (minutes), or 'h' (hours) to the value (e.g. 30m).
  -T<0-5>: Set timing template (higher is faster)
  --min-hostgroup/max-hostgroup <size>: Parallel host scan group sizes
  --min-parallelism/max-parallelism <numprobes>: Probe parallelization
  --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <time>: Specifies
      probe round trip time.
  --max-retries <tries>: Caps number of port scan probe retransmissions.
  --host-timeout <time>: Give up on target after this long
  --scan-delay/--max-scan-delay <time>: Adjust delay between probes
  --min-rate <number>: Send packets no slower than <number> per second
  --max-rate <number>: Send packets no faster than <number> per second
FIREWALL/IDS EVASION AND SPOOFING:
  -f; --mtu <val>: fragment packets (optionally w/given MTU)
  -D <decoy1,decoy2[,ME],...>: Cloak a scan with decoys
  -S <IP_Address>: Spoof source address
  -e <iface>: Use specified interface
  -g/--source-port <portnum>: Use given port number
  --proxies <url1,[url2],...>: Relay connections through HTTP/SOCKS4 proxies
  --data <hex string>: Append a custom payload to sent packets
  --data-string <string>: Append a custom ASCII string to sent packets
  --data-length <num>: Append random data to sent packets
  --ip-options <options>: Send packets with specified ip options
  --ttl <val>: Set IP time-to-live field
  --spoof-mac <mac address/prefix/vendor name>: Spoof your MAC address
  --badsum: Send packets with a bogus TCP/UDP/SCTP checksum
OUTPUT:
  -oN/-oX/-oS/-oG <file>: Output scan in normal, XML, s|<rIpt kIddi3,
     and Grepable format, respectively, to the given filename.
  -oA <basename>: Output in the three major formats at once
  -v: Increase verbosity level (use -vv or more for greater effect)
  -d: Increase debugging level (use -dd or more for greater effect)
  --reason: Display the reason a port is in a particular state
  --open: Only show open (or possibly open) ports
  --packet-trace: Show all packets sent and received
  --iflist: Print host interfaces and routes (for debugging)
  --append-output: Append to rather than clobber specified output files
  --resume <filename>: Resume an aborted scan
  --stylesheet <path/URL>: XSL stylesheet to transform XML output to HTML
  --webxml: Reference stylesheet from Nmap.Org for more portable XML
  --no-stylesheet: Prevent associating of XSL stylesheet w/XML output
MISC:
  -6: Enable IPv6 scanning
  -A: Enable OS detection, version detection, script scanning, and traceroute
  --datadir <dirname>: Specify custom Nmap data file location
  --send-eth/--send-ip: Send using raw ethernet frames or IP packets
  --privileged: Assume that the user is fully privileged
  --unprivileged: Assume the user lacks raw socket privileges
  -V: Print version number
  -h: Print this help summary page.
EXAMPLES:
  nmap -v -A scanme.nmap.org
  nmap -v -sn 192.168.0.0/16 10.0.0.0/8
  nmap -v -iR 10000 -Pn -p 80
SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
```



##### 二，帮助实例
###### 1.文件扫描和排除

nmap -iL 文件名 

Nmap对文件中的IP进行扫描。



![image-20200504122948444](/home/kun/.config/Typora/typora-user-images/image-20200504122948444.png)

nmap -iR 100 -p445

随机扫描100个ip扫描开放445端口的主机



![image-20200504124229680](/home/kun/.config/Typora/typora-user-images/image-20200504124229680.png)

nmap -iR 10 -p445 --exclude 192.168.11.139,192.168.11.132

随机扫描10个ip内的445端口但扫描时排除192.168.11.139和192.168.11.132。



###### 2.主机发现

![image-20200504130918304](/home/kun/.config/Typora/typora-user-images/image-20200504130918304.png)

nmap -sL 192.168.11.138 

简单的列出扫描列表



![image-20200504131028661](/home/kun/.config/Typora/typora-user-images/image-20200504131028661.png)

nmap -sn 192.168.11.138

对目标进行Ping扫描，禁止端口扫描。



nmap -Pn 192.168.11.138

使用端口扫描，禁用Ping扫描。



​	_PS/PA/PU/PY_

​	对指定端口进行TCP\SYN\ACK\UDP\SCTP发现

> ![img](https://pic.baike.soso.com/ugc/baikepic2/0/20160921213813-1723299128.jpg/800)
>
> 流控制传输协议（SCTP，Stream Control Transmission Protocol）是一种可靠的传输协议，他在两点之间提供了稳定和有序的数据传输服务。类似与TCP，并可以保护数据消息边界。
>
> 与TCP不同的是SCTP主要一多宿主和多流动功能提供收益，两种功能均可提高可用性。

```
nmap -PS 192.168.11.138
使用TCP协议对目标进行扫描

nmap -PA 192.168.11.138
使用SYN协议对目标进行扫描

nmap -PU 192.168.11.138
使用ACK协议对目标进行扫描

nmap -PY 192.168.11.138
使用SCTP协议对目标进行扫描
```



​	_PE/PP/PM_

​	ICMP回应/时间戳/网络掩码/请求发现探测

```
nmap -PE 192.168.11.138
对目标使用ICMP回应探测

nmap -PP 192.168.11.138
对目标进行时间戳探测

nmap -PM 192.168.11.138
对目标进行时间戳探测
```



nmap -PO 192.168.11.138

IP协议PING



​	_-n/-R_

```
nmap -n 192.168.11.138
对本次扫描不解析域名系统

nmap -R 192.168.11.138
对本次扫描解析域名系统
```

​	

![image-20200504143920775](/home/kun/.config/Typora/typora-user-images/image-20200504143920775.png)

nmap --dns-servers 8.8.8.8 192.168.11.138

指定DNS服务器对目标进行检索



nmap --system-dns 192.168.11.138
使用系统默认的DNS对目标进行检索



nmap --traceroute sogo.com

扫描目标的同时并进行链路追踪



###### 3.扫描（协议扫描）技术

​	_sS/sF/sA/sW/sM_

> Connect()用来将参数Sockfd的Connect()连接至serv_addr指定的网络地址。
>
> Connect()主要用于指定和建立Socket连接
>
> 
>
> Maimon扫描
>
> Maimon 是一位古代到现在最有影响的以为犹太哲学家。
>
> 其中有一个代表著作是《困惑者指南》，所以-sM命令的意思为“困惑扫描，指指定目标后迷茫的继续扫描”

```
nmap -sS 192.168.11.138
TCP回应扫描

nmap -sT 192.168.11.138 
connect()扫描

nmap -sA 192.168.11.138
ACK扫描

nmap -sW 192.168.11.138
窗口扫描

nmap -sM 192.168.11.138
Maimon扫描
```

 

nmap -sU 192.168.11.138

使用UDP协议进行扫描



​	_sN/sF/sX_

![image-20200504172232641](/home/kun/.config/Typora/typora-user-images/image-20200504172232641.png)

![image-20200504181911676](/home/kun/.config/Typora/typora-user-images/image-20200504181911676.png)

```
nmap -sN 192.168.11.138
使用TCP空扫描

nmap -sF 192.168.11.138
使用FIN标志扫描

nmap -sX 192.168.11.138
使用Fin\Push\Urgent标志进行扫描
```



​	nmap -scanflags FIN 192.168.11.138
​	自定义扫描标志为FIN。

​	nmap 192.168.11.138 -sI 192.168.11.139
​	使用僵尸机器192.168.11.138对192.168.11.139进行扫描



​	_sY/sZ_

```
nmap -sY 192.168.11.138
使用SCTP协议进行扫描

nmap -sZ 192.168.11.138
使用Cookie_echo区块扫描
```

​	

​	nmap -sO 192.168.11.138

​	使用IP协议进行扫描



###### 4.扫描规格

nmap -p445 192.168.11.138

指定扫描目标为445端口



nmap --exclude-ports 445 192.168.11.138

在扫描的过程中排除445端口。



nmap -F 192.168.11.138

使用快速模式对目标进行检索



nmap -r 192.168.11.138

连续扫描端口，不需要随机化



nmap --top-ports 100 192.168.11.138

扫描最长用端口排名为1的开放端口



###### 5.版本检测

nmap -sV 192.168.11.138

探测目标服务和操作系统。

​	

​	_探针 - version_

```python
nmap --version-intensity 9 192.168.11.138
使用探针深度为9的等级对目标进行扫描

nmap --version-light 192.168.11.138
设置最有可能的探针限制（等级为2）

nmap --version-all 192.168.11.138
使用全部探针（等级为9）进行扫描

nmap--version-trace 192.168.11.138
显示详细的版本扫描活动，官方北其名曰×（调试模式）
```



###### 6.操作系统检测	

```
nmap -O 192.168.11.138
检测操作系统从

nmap --osscan-limit 192.168.11.138
将操作系统识别放放在有希望的目标上。

nmap --osscan-guess 192.168.11.138
更积极的猜测对方系统
```



###### 7.时光的留去与坚毅

nmap -T 5 12.168.11.138

设置时间模板对目标进行检索（0~5）

​	

​	hostgroup

```python
nmap --max-hostgroup 10000 192.168.11.138
设置并行主机扫描组大小为“10000”

nmap --min-hostgroup 10000 192.168.11.138
设置扫描主机大小组为“10000”
```



​	_timeout_

```python
nmap --max-rtt-timeout 1 192.168.11.138
设置与数据包的往返时间

nmap --min-rtt-timeout 1 192.168.11.139

nmap --initial-rtt-timeout 1 192.168.11.138
```



nmap --max-retries 1 192.168.11.138

设置重传次数为1



nmap --host-timeout 1 192.168.11.138

对方在一秒中无答应则放弃数据包



​	_delay_

```
nmap --scan-delay 1 192.168.11.138
设置探针之间的延迟为 1秒

nmap --max-scan-dalay 1 192.168.11.138
设置探针之间的时间为 1 毫秒
```



​	_rate_

```
nmap --min-rate 1 192.168.11.138
设置数据包发送数量不慢于1秒

nmap --max-rate 1 192.168.11.138
设置数据不发送不慢于 1 秒
```



###### 8.入侵检测和系统规避及欺骗

​	_片段包_

	片段包可以理解为将一个数据分割为很多包进行发送，

```
nmap --mtu 8 182.168.11.138
设置片段包为8(0~8)

nmap -f 19999 192.168.11.138
设置片段包为19999
```



​	nmap -D 192.168.11.139,192.168.11.139 192.168.11.132

​	使用僵尸机器对目标进行扫描。



​	nmap -S 192.168.11.139 -e vmnet8 192.168.11.138

​	对目标进行IP欺骗

​	

​	nmap -e vmnet8 182.168.11.138



​	_指定端口号_

```
nmap -g 445 192.168.11.138
通过指定的端口号对目标进行检索

nmap --source-ports 445 192.168.11.138
使用指定的端口号对目标进行检索
```

​	

> --proxies <url1,[url2],...>: 	通过HTTP/SOCKS4代理中继连接



​	_插入数据_

![image-20200505100441592](/home/kun/.config/Typora/typora-user-images/image-20200505100441592.png)	

![image-20200505095952320](/home/kun/.config/Typora/typora-user-images/image-20200505095952320.png)

```python
nmap --data 11002233 192.168.11.138
将自定义负载插入到数据包之中

nmap --data-string 11002233 192.168.11.138
插入十六进制数"11002233"到数据包中。
```



​	_ip-options_

> ip-options 是一个非常蛋疼的，因为这个参数吧，基本上没多少人写的这么全，那么今日我xxx某人，就来为他做一个点精之笔。
>
> 
>
> 首先呢，ip-options一共差不多有“S|R|L|T|U”几种参数，大概对应字母为“Traceroute” or "record route"
>
> 
>
> 根据官方所称是：
>
> > 这些选项可以放在包头之中，与无处不在的TCP选项不同。当你夹杂了这些选项的时候，会出现安全性和多方面的因素，Internet会阻止这些选项。
> >
> > 而这些选项并不是没有用的，就假如传统的tracerouter的风格方法失败了。此时还有一个选项你可以使用，那就是 record route 选项来确定达到目标的路径。
> >
> > 
> >
> > 除此之外，你也可在选项后面加上十六进制数插入到数据包中，但是你需要遵守他的规格。
> >
> > \x00\x11
> >
> > ![image-20200505111754664](/home/kun/.config/Typora/typora-user-images/image-20200505111754664.png)
> >
> > 就是上面的这个规格，你必须要遵守才可发送数据包

```python
nnmap --ip-options R 192.168.11.255 192.168.11.138
指定route通过指定IP选项发送数据包

nmap --ip-options S 192.168.11.255 192.168.11.138
使用tracouter选项发送包，虽然有极大的可能被过滤

nmap --ip-options T 192.168.11.138
使用record routes选项发送数据包

nmap --ip-options U 192.168.11.138
使用record timestamp选项发送数据包
```



​	nmap --ttl 122 192.168.11.138

​	设置数据包生存时间为“122”，最高生存时间为（0～	255）



​	nmap --spoof-mac 00:0C:29:AC:29:25 192.168.11.138

​	欺骗MAC地址00:0C:29:AC:29:25



​	nmap --badsum 192.168.11.138

​	使用伪造的TCP/UDP/SCTP的校验和发送数据包



###### 9.输出

​	_oN/oX/oS/oG_

```
nmap -oN a 192168.11.138
将扫描结果以Normal格式输出

nmap -oS b 192.168.11.138
将扫描结果以XML格式输出

nmap -oX c 192.168.11.138
将扫描结果一cript格式输出

nmap -oG d 192.168.11.138
将扫描结果以kIddi3格式输出了；了；了
```



​	nmap -oA a 192.168.11.139

​	以三种主要格式进行输出



​	

###### - 详细与调试

![image-20200505130032277](/home/kun/.config/Typora/typora-user-images/image-20200505130032277.png)

nmap -v 192.168.11.138

详细打印输出结果，你也可以使用nmap -vv来显示更详细的输出结果

 		

![image-20200505130251225](/home/kun/.config/Typora/typora-user-images/image-20200505130251225.png)

nmap -d 192.168.11.138

调试输出，类似verison-tracer 

​	

> --append-output:			追加到而不是删除指定的输出文件
>
> 
>
> --resume \<filename>:		恢复中止的扫描
>
> 
>
> --stylesheet <path/URL>:	将XML输出转换为HTML的XSL样式表



​	nmap -oX a --no-stylesheet 192.168.11.138	

​	禁止将XSL样式表与XML输出相互关联



###### 10.效果

nmap --reason 192.168.11.138

显示端口处于特定状态下的原因



nmap --open 192.168.11.138

只输出已经打开的端口



![image-20200505130938521](/home/kun/.config/Typora/typora-user-images/image-20200505130938521.png)

nmap --packet-trace 192.168.11.138

显示发送包和接收包信息



![image-20200505131025364](/home/kun/.config/Typora/typora-user-images/image-20200505131025364.png)

nmap --iflist 192.168.11.138

输出主机接口信息







###### 11.其他

nmap -6 fe80::485d:7e23:566:b84d

使用/启用 ipv6协议进行扫描



![image-20200505133153649](/home/kun/.config/Typora/typora-user-images/image-20200505133153649.png)

nmap -A 192.168.11.138

使用/启用操作系统检测，版本检测，脚本扫描，tracerout





>  --datadir \<dirname>:		指定自定义Nmap数据文件位置





​	_send_

```
nmap --send-echo 192.168.11.138
使用原始的以太网帧发送

nmap --send-ip 192.168.11.138
使用原始的IP包发送
```



​	_privileged_

> 有了原始套接字特权可以

```
nmap --privileged 192.168.11.138
假设用户是完全特权的

nmap --unprivileged 192.168.11.138
假设用户是缺乏原始套接字特权的
```





