# Automater 

_Automater最初创建用来自动分析IP地址的OSINT的工具。它很快成长为一个分析IP地址、url和散列的工具。_



_"幸运的是，我的一位导师和朋友(@jameshub3r)提供了他的时间和专业知识，帮助enitre重新编写代码，重点放在模块化的可扩展框架上。就这一点而言，新准则达到了要求。Automater的真正强大之处在于，无需修改python代码，就可以轻松地修改所检查的源和从中获取的数据。要修改源代码，只需打开site .xml文件并进行修改。稍后我将发表另一篇文章，在那里有更详细的介绍 "_



_—— http://www.tekdefense.com/automater/_

----



###### 一，基础知识

__散列__

散列（Hashing）是一种休息你安全的实作方法他是一串资料中经过的杂凑算法（Hashing Algorithms）计算出来的资料指纹（data fingerprint）经常用来做自来哦是否被篡改，以保证档案与资料确实由原创作者提供



__DGA__

DGA是域名生成算法，主要利用字符来生成C&C域名，从而逃避技术检测的手段。例如一个由程序创建的DGA生成域qhdasdisdbdae.com，如果机器尝试与域名相互建立链接则会直接下载此程序。

域名黑名单通常会阻断这也域名的俩接，但是如ugo使用DGA算法则不会成功的拦截。国内一些下相关厂商也对此进行研究和探讨，比如“数盟”





__OSINT__

公开资源情报计划（Open source intelligence，OSINT），是美国中央情报局（CIA）的一种情报搜集手段。其意思为从各种公开的信息信息资源中寻找和获得有价值的情报

OSINT不同与一般的情报搜集，他可以为特定的人或团队而量身定制的信息之支持



_相关定义_

美国行政管理和预局认为，公开资源情报属于“军事与决策支持（Office of Management and Budget）”的工作范畴。



在西方界中，认为“公开”指的是“不隐蔽”，公开情报资源OSINT是想对于“秘密的情报”。

“谍报”相对而言就是从舆论信息中搜集，甄别和获取信息，并对其进行分析，从而可以得到有价值的情报的学问。其输入的信息，而输出的确实情报。





| 大类                                                         | 名称                         | EN                                                           |
| ------------------------------------------------------------ | ---------------------------- | ------------------------------------------------------------ |
| 媒体                                                         | 报纸                         | newspapers                                                   |
|                                                              | 杂志                         | magazines                                                    |
|                                                              | 电台                         | radio                                                        |
|                                                              | 电视节目                     | television                                                   |
|                                                              | 基于计算机信息               | computer-based information                                   |
|                                                              |                              |                                                              |
| 基于网络社区（Web-based communities）和用户创造的内容（user generated content） | 社交站点                     | social-[networking](https://baike.sogou.com/lemma/ShowInnerLink.htm?lemmaId=63379853&ss_c=ssc.citiao.link) sites |
|                                                              | 视频分享网站                 | video sharing sites                                          |
|                                                              | 维基百科                     | wikis                                                        |
|                                                              | 博客                         | blogs                                                        |
|                                                              | 通俗分类                     | folksonomies                                                 |
|                                                              |                              |                                                              |
| 基于公开数据（Public data）                                  | 政府报告                     | [government](https://baike.sogou.com/lemma/ShowInnerLink.htm?lemmaId=7616301&ss_c=ssc.citiao.link) reports |
|                                                              | 官方数据（如预算）           | official data（budgets）                                     |
|                                                              | 人口统计资料                 | demographics                                                 |
|                                                              | 听证会                       | hearings                                                     |
|                                                              | 立法辩论                     | legislative debates                                          |
|                                                              | 新闻发布会                   | press conferences                                            |
|                                                              | 演讲                         | speeches                                                     |
|                                                              | 海洋和航空的安全警告         | marine and aeronautical safety warnings                      |
|                                                              | 环境影响图片                 | environmental impact statements                              |
|                                                              | 合同签订                     | contract awards                                              |
|                                                              |                              |                                                              |
| 观察（Observation）和报告（reporting）                       | 谷歌地球                     | Google Earth                                                 |
|                                                              |                              |                                                              |
| 专家（Professional）和学者（ academic）                      | 会议                         | conferences                                                  |
|                                                              | 研讨会                       | symposia                                                     |
|                                                              | 专业组织                     | professional associations                                    |
|                                                              | 学术论文                     | academic papers                                              |
|                                                              | 专家                         | subject matter experts                                       |
|                                                              |                              |                                                              |
| 地理信息数据                                                 | 地图                         | maps                                                         |
|                                                              | 地图集                       | atlases                                                      |
|                                                              | 地名录                       | gazetteers                                                   |
|                                                              | 港口规划                     | port plans                                                   |
|                                                              | 重力数据                     | gravity data                                                 |
|                                                              | 航空数据                     | aeronautical data                                            |
|                                                              | 导航数据                     | navigation data                                              |
|                                                              | 人类分布数据（如文化和形象） | human terrain data                                           |
|                                                              | 环境数据                     | human terrain data                                           |
|                                                              | 商业影像                     | [commercial](https://baike.sogou.com/lemma/ShowInnerLink.htm?lemmaId=174534542&ss_c=ssc.citiao.link) imagery |
|                                                              | 激光雷达                     | LIDAR ，Light Detection And Ranging                          |
|                                                              | 超多光谱数据                 | hyper and multi-spectral data                                |
|                                                              | 机载成像                     | airborne imagery                                             |
|                                                              | 地理名称                     | geo-names                                                    |
|                                                              | 地理特征                     | geo-features                                                 |
|                                                              | 城市地形                     | urban terrain                                                |
|                                                              | 垂直阻塞的数据               | VOD， vertical obstruction data                              |
|                                                              | 界标数据                     | boundary marker data                                         |
|                                                              | 地理空间聚合                 | geospatial mashups                                           |
|                                                              | 空间数据库                   | spatial databases                                            |
|                                                              | WEB服务                      | web services                                                 |
|                                                              | 地理信息系统                 | Geographic Information System或 Geo－Information system，GIS） |
---



###### 二，帮助手册

[CN]:翻译

usage: Automater.py [-h] [-o 输出] [-b] [-f CEF] [-w WEB] [-c CSV] 
           [-d 延迟] [-s 源] [--proxy 代理] [-a  用户代理] [-V] 
           [-r] [-v] 
           目标

IP、URL和散列被动分析工具

target 

列出一个IP地址(接受CIDR或dash符号)，URL或散列来查询或传递文件的文件名包含IP地址信息、URL或散列来查询每一个用换行符分隔。



可选参数:

-h, --help 				 				 				   

显示此帮助消息并退出



-o OUTPUT, --output OUTPUT  				

此选项将输出结果到文件中。



-b, --bot 					 				 				 

此选项将为机器人输出最小化的结果。



-f CEF, --cef CEF  				 				    

 此选项将输出结果到CEF格式文件



-w WEB, --web WEB  				 			   

此选项将输出结果到HTML文件。



-c CSV, --csv CSV 									  

此选项将输出结果到CSV文件。



-d DELAY, --delay DELAY 						

这将把延迟改为输入的秒数，默认是2。



 -s SOURCE, --source SOURCE 			   

此选项仅对a运行目标特定的源引擎来获取相关的域。选项在站点的name属性中定义XML配置文件中的元素。这可以是用分号分隔的名称列表。



--proxy PROXY

此选项将设置要使用的代理(例如：proxy.example.com: 8080)



 -a USERAGENT, --useragent USERAGENT  

此选项允许用户设置所看到的用户代理
通过使用web服务器。默认情况下，user-代理被设置为Automater/version



-V, --vercheck 

此选项用于检查和报告版本控制自动化。检查自动程序中的每个python模块范围。默认，(no -V)为False



-r, --refreshxml 

属性刷新tekdefense.xml文件远程GitHub的网站。Default (no -r)为False。



-v, --verbose 

此选项将消息打印到屏幕。默认(没有-v)是错误的。

---



###### 三，命令实例

| 类型 | 序列 | 名称                        | 翻译                                               |
| ---- | ---- | --------------------------- | -------------------------------------------------- |
| IP   | 1    | RTex DNS                    |                                                    |
| IP   | 2    | FNet URL                    |                                                    |
| IP   | 3    | VT ASN:                     | 一种 ISO/ITU-T 标准                                |
| IP   | 4    | VT Country                  | 国家                                               |
| IP   | 5    | AS Owner                    | 所有者                                             |
| IP   | 6    | pDNS                        | 公共数据网络（Public Data Network）                |
| IP   | 7    | Malware                     | 恶意软件                                           |
| IP   | 8    | Mal URLs                    | 网站链接                                           |
| IP   | 9    | Blacklist from IPVoid       | 黑名单                                             |
| IP   | 10   | ISP                         | ISP（Internet Service Provider）即因特网服务提供商 |
| IP   | 11   | Country from IPVoid         | 来自IPVoid的国家                                   |
| IP   | 12   | Malc0de Date                | 日期                                               |
| IP   | 13   | IP                          | IP                                                 |
| IP   | 14   | Country                     | 国家                                               |
| IP   | 15   | ASN                         | 一种 ISO/ITU-T 标准                                |
| IP   | 16   | MD5                         | 摘要算法（Message-Digest algorithm 5，MD5）        |
| IP   | 17   | Authority Score             | Authority Score（权威度）                          |
| IP   | 18   | Country Name                | 国家名称                                           |
| IP   | 19   | Region Name                 | 域名                                               |
| IP   | 20   | City                        | 城市                                               |
| IP   | 21   | zipcode                     | 邮政编码                                           |
| IP   | 22   | Latitude                    | 维度                                               |
| IP   | 23   | longitude                   | 经线、经度                                         |
| IP   | 24   | total target IPs            | 目标IP总数                                         |
| IP   | 25   | total packets               | 数据包总数                                         |
| IP   | 26   | last seen on                | 最后一次露面                                       |
| IP   | 27   | first seen                  | 第一次见到                                         |
| IP   | 28   | THIP                        |                                                    |
| IP   | 29   | TekHP                       |                                                    |
| IP   | 30   | activity type               | 活动类型                                           |
| IP   | 31   | first mail received         | 收到的第一封邮件                                   |
| IP   | 32   | last mail received          | 收到的最后一封邮件                                 |
| IP   | 33   | total mails received        | 收到邮件总数                                       |
| IP   | 34   | spider first seen           | 蜘蛛首次出现                                       |
| IP   | 35   | spider last seen            | 蜘蛛最后出现                                       |
| IP   | 36   | spider sightings            | 蜘蛛目击                                           |
| IP   | 37   | user-agent sightings        | 用户代理目击                                       |
| IP   | 38   | first post on               | 第一篇文章                                         |
| IP   | 38   | last post on                | 最后文章                                           |
| IP   | 40   | form posts                  | 表单提交                                           |
| IP   | 41   | first rule break on         | 第一次打破规则                                     |
| IP   | 42   | last rule break on          | 最后一次打破规则                                   |
| IP   | 43   | rule break sightings        | 规则打破目击                                       |
| IP   | 44   | first dictionary attack     | 第一个字典攻击                                     |
| IP   | 45   | last dictionary attack on:  | 最后一次字典攻击                                   |
| IP   | 46   | dictionary attack sightings | 字典攻击目击                                       |
| IP   | 47   | harvester first seen        | 收获者首次出现                                     |
| IP   | 48   | harvester last seen         | 最后一次见到收或者                                 |
| IP   | 49   | harvester sightings         | 目击收或者                                         |
| IP   | 50   | harvester results           | 收获结果                                           |



__基本扫描__

![image-20200428210451968](/home/kun/.config/Typora/typora-user-images/image-20200428210451968.png)

![image-20200428180753168](/home/kun/.config/Typora/typora-user-images/image-20200428180753168.png)

automater 220.181.38.148

> 或地址改为 44A6A7D4A039F7CC2DB6E85601F6D8C1

列出一个IP地址(接受CIDR或dash符号)，URL或散列来查询或传递文件的文件名包含IP地址信息、URL或散列来查询每一个用换行符分隔。





![image-20200428184656340](/home/kun/.config/Typora/typora-user-images/image-20200428184656340.png)

automater -b 120.79.196.240 

将为机器人输出最小化的结果。



> Robtex
>
> Robtex用于各种IP号码、域名等的研究 。
>
> 如果你是一个数字取证的人员或经常调查竞争对手，追踪垃圾邮件发生者，黑客或普通IT人员，那你应该是一定要去了解的。
>
> 
>
> https://www.robtex.com/



automater -s robtex 220.181.38.148

使用RTex库进行查找信息

![image-20200428212100856](/home/kun/.config/Typora/typora-user-images/image-20200428212100856.png)





automater -d 10 120.79.196.240

设置延迟数为10 ，默认为2



automater --proxy xxxxx:端口 120.79.196.240

使用代理服务器

![image-20200428213333219](/home/kun/.config/Typora/typora-user-images/image-20200428213333219.png)





> “User Agent” 也被称之为用户代理，现在主要广泛被用于标注浏览器客户信息。
>
> 在互联网早期的时候，互联网是完全基于文本形式的，用户需要连难忘需要输入各种键盘命令。
>
> 后来开发人员开发出了多种浏览工具帮助用户浏览
>
> 而这种工具就被用户称之为 “代理（User Agent）



![image-20200428214330867](/home/kun/.config/Typora/typora-user-images/image-20200428214330867.png)

automater -a Automater/version 120.79.196.240

设置用户代理,默认用户代理为 Automater/version



![image-20200428214823038](/home/kun/.config/Typora/typora-user-images/image-20200428214823038.png)

automater -V 120.79.196.240

> automater -v 120.79.196.240将结果打印到屏幕中？

使用全部模块进行扫描



![image-20200428215315212](/home/kun/.config/Typora/typora-user-images/image-20200428215315212.png)

automater -r 120.79.196.240

刷新属性tekdefense.xml文件，远程链接到Github网站





__文件存储__

![image-20200428183013199](/home/kun/.config/Typora/typora-user-images/image-20200428183013199.png)

automater 120.79.196.240 -o 02.txt

将输出结果存储到/usr/share/automater02.txt文件中



![image-20200428185544638](/home/kun/.config/Typora/typora-user-images/image-20200428185544638.png)

automater -f 03.cef 120.79.196.240 

将结果输出为CEF格式文件



![image-20200428190232742](/home/kun/.config/Typora/typora-user-images/image-20200428190232742.png)

automater -w 04.html 120.79.196.240 

将结果输出为html格式文件



![image-20200428190847894](/home/kun/.config/Typora/typora-user-images/image-20200428190847894.png)

automater -c 05.csv 120.79.196.240

输出为CSV格式文件









----




###### 3

 ASN是一种ISO/ITU-T标准，描述了了一种对数据进行表示、编码和解码的数据格式。提供了一整套中呢高贵的格式用于描述对象的结构。



advance shipping notice (ASN)                               

预先运送通知 --  供应商向客户发出的，说明订单发运时间的文书。ASN通常以电子方式传输。



###### 17

权威度（Authority Score）可通过提供来自其他社交媒体网站的内向链接数量，放映出一个网站或社交媒体的影响力，比如PR值等。。