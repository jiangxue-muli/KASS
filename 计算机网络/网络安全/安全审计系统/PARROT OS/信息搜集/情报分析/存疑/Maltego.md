# Maltego 

Maltego 应用程序是一个可视化的链接分析工具，开箱即用，带有开源智能(OSINT)插件，名为转换。该工具提供实时数据挖掘和信息收集，以及在基于节点的图形上表示该信息，使得所述信息之间的模式和多阶连接易于识别。



Maltego数据来源
通过Maltego转换中心整合来自公共来源(OSINT)、商业供应商和内部来源的数据。所有数据都预先打包为转换，准备在调查中使用。



_——https://www.maltego.com/_

---



##### 一，Maltego基础

###### 1.什么是Maltego

Maltego是一个交互式的数据挖掘工具，主要用于呈现连接分析有向图。可用于在线调查、一发现来自互联网上各种来源的信息之间的关系。

Maltego也可以使用转换的思想来自动化查询不同数据源的过程，该信息随后显示在基于节点的图表上，适合执行链接分析。



目前Maltgo只有四个版本的客户端，虽然他可以渲染有向图和链接分析，发现来自互联网上的各种信息之间的联系：

- Maltego  CE - 无CE，非商业用途
- Maltego Classic -  经典付费商业用途
- Maltego XL  - 付费，商业用途
- Maltego CaseFile - 免费，商业、没有任何变化



前三个Maltego客户端可以访问标准的转换库，从而广泛的在公众资源中发现数据，这些数据通常通用与在线调查或数字取证。

由于Maltego可以与几乎任何数据源无缝集成，许多数据供应商选择Maltego作为其数据的交付平台，这将意味着Maltego可以适应自己的独特需求。



###### 2.你可以使用Maltego做什么

Maltego可以用用于安全相关的工作和信息搜集阶段，可以更加的节省你的时间，更准确的工作。

Maltego提供了强大的搜索功能，提供了更加智能的结果，并且可以发现一些“隐藏”的信息资源，这些通过Maltego可以是实现。

Maltego的重点是分析互联网上的公开信息之间的联系，这包括追踪互联网的基础设施，以及找到他的所有者和他的组织信息。



Maltego可以确定以下实体之间的联系：

| 大类           | 具体         |
| -------------- | ------------ |
| 人             | 名字         |
|                | 电子邮件地址 |
|                | 化名         |
|                |              |
| 社群网络       | 公司         |
|                | 组织         |
|                | 网站         |
|                |              |
| 互联网基础设施 | 域名         |
|                | DNS名称      |
|                | IP地址       |
|                |              |
| 丛属关系       |              |
| 文件和档案     |              |
|                |              |

通过查询域名系统记录，whois记录，搜索引擎，社交网络，各种在线应用的接口和提取数据等资源，可使用开源智能技术找到这些信息的联系

Maltego在各种图形分布中提供结果，并允许信息聚集，这使得他们的间隔三四度，也可以查看隐藏的联系

Maltego应用与各个行业，如执法部门，互联网公司，和银行等。



###### 3.常见版本特征

__Maltego Classic__

- 能够在但个图形上对多大10000个实体执行链接分析能力;

- 运行的每个转换最多可返回10000实体;

- 包括集合节点，这些节点将会自动将实体与公共特征组合在一起，允许你查看传递的噪声并找到你正在寻找的关键联系;

- 包括在单个会话中多个分析师实时共享图表能力;

- 并且可以导出为图像，比如jpg,bmp,png等，还支持生成PDF报告哦啊，表格格式CSV，XLX，XLSX，GraohML等。



__Maltego XL__

Maltego XL是三个Maltego中的首个客户端版本，他包含了 Maltego Classic的所有功能和特性，但是增加了处理超大图形的能力。虽然他很多方面类似与 Matogo Classic的特点，但是他依然有很多功能：

- 但个图形上对多达__1,000,000__实体执行链接分析的能力。
- 每次最多返回10,000个实体，包括集合节点，这些节点将会自动将实体与公共特征组合在一起没允许您查看到传递的噪声并找到您正在寻找的关键连关系

- 包括在单个会话中多个分析师实时共享图表能力;

- 并且可以导出为图像，比如jpg,bmp,png等，还支持生成PDF报告哦啊，表格格式CSV，XLX，XLSX，GraohML等。



__Maltego Community edition__

Malotogo CE，是一个社区版，被全世界的安全专业人员使用，并且在Parrot os和Kali Linux都有安装其版本。

想对于Maltego Classic相为比较，Maltego的功能会有所欠缺，但他的唯一好处是在与Maltego是相对于免费的存在。但是他的局限性是不可以为商业目的进行使用，并且对但个转换返回实体的最大数量也有限制。

- 能够在但个图形上对多大10000个实体执行链接分析能力;

- 运行的每个转换最多可返回12实体;

- 包括在单个会话中多个分析师实时共享图表能力;

- 并且可以导出为图像，比如jpg,bmp,png等，还支持生成PDF报告哦啊，表格格式CSV，XLX，XLSX，GraohML等。



__Maltego CaseFile __

Maltego CA 是用于对离线情报问题的回答，他允许分析师们检查离线数据之间的联系。

- CaseFile是一个视觉智能应用程序，可以用于实现不同信息之间的关联和与现实是世界的联系。

- 当然你也可以选择绘制信息片段之间的关系，即使他们相距甚远，也能看到不同的隐藏联系。

- 在CaseFile中，附带了很多不同类型是实体，这些实体通用与调查，允许你快速的采取一些行动，比如破门，丢炸弹和炮轰等相关军事行动。并且还支持自定义实体数据的能力。

- 还有一个案例文件，可以为你调用几乎所有类型的调查的信息搜集，分析和情报阶段，包括信息技术安全、执法和任何数据驱动的工作，他会节省你的时间。

- 并且能够以可视化CSV、XLS、和XLSX个是存储的数据集，以及将图表导出为这些格式。

​                                                                                                                                                                                                                                                                                                                                       

##### 二，安装Maltego CE

![image-20200429133503711](/home/kun/.config/Typora/typora-user-images/image-20200429133503711.png)

如果对功能不是太高的话，我们可以选择 Maltego CE 社区版



![image-20200429133703004](/home/kun/.config/Typora/typora-user-images/image-20200429133703004.png)



![image-20200429134725787](/home/kun/.config/Typora/typora-user-images/image-20200429134725787.png)

前往社区注册帐号和密码以便于完成安装，以下是社区注册地址：

```
https://www.maltego.com/ce-registration/?utm_source=paterva.com&utm_medium=referral&utm_campaign=301#tab-1
```



![image-20200429141234437](/home/kun/.config/Typora/typora-user-images/image-20200429141234437.png)



![image-20200429141512947](/home/kun/.config/Typora/typora-user-images/image-20200429141512947.png)



![image-20200429141747398](/home/kun/.config/Typora/typora-user-images/image-20200429141747398.png)

此时Maltego会问你：”Automaticall send Error Reports“是否自动发送错误报告。

当发送错误报告时，将不包括图形或用户数据。发送的唯一信息是操作系统名称、马耳他版本和错误本身。

> Disclaimer: When error reports are sent no graph or user data will be included. The only information sent will be the Operating System name, Maltego version and the error itself.

可根据需要进行选择



![image-20200429142129188](/home/kun/.config/Typora/typora-user-images/image-20200429142129188.png)

此时Maltego会提醒你选择模式，在Maltego会分为两种主要模式，分别为”正常隐私模式和”秘密隐私模式“

```
正常隐私模式
使用此模式可以享受到最丰富的Maltego体验，Maltego可直接从互联网上获取数据
```

```
秘密模式
如果你是一个自身的调查员可使用这种模式，这种形式的好处就是没有互联网流量来自你的电脑IP，那么你的Maltego也不会从桌面上直接从Internet获得任何数据。
就比如说实体图像的下载将会被阻止，
```



![image-20200429150621062](/home/kun/.config/Typora/typora-user-images/image-20200429150621062.png)

当你的Maltego如上图状态的话，则可以证明Maltego CE已经完成了安装，此时你可以选择:



[CN]:中文

- 打开一个空白的图形，让我来处理一下
- 打开一个示例图
- 走开，我已经做了前面的事!



[EN]:官方

- Open a blank graph and let me play around 
- Open an example graph
- Go away ,I have done the bofore!



##### 三，Maltego CE 界面翻译

###### 头部

![image-20200429151600444](/home/kun/.config/Typora/typora-user-images/image-20200429151600444.png)

| 索引 | EN               | CN           |
| ---- | ---------------- | ------------ |
| 1    | Investigete      | 研究         |
| 2    | View             | 视角         |
| 3    | Entities         | 实体         |
| 4    | Collections      | 搜集         |
| 5    | Transforms       | 变换         |
| 6    | Machines         | 机器         |
| 7    | Collaboration    | 合作         |
| 8    | Import \| Export | 导入 \| 导出 |
| 9    | Windows          | 窗口         |
|      |                  |              |

###### 1.研究 - Investigete

![image-20200429155157140](/home/kun/.config/Typora/typora-user-images/image-20200429155157140.png)

| 索引 | EN                   | 中文          |
| ---- | -------------------- | ------------- |
| 1    | Cupy                 | 复制          |
|      | Pase                 | 粘贴          |
|      | Clear Graph          | 清晰图形      |
|      | Cut                  | 剪切          |
|      | Delete               | 删除          |
|      |                      |               |
| 2    | Number of Results    | 结果数        |
|      |                      |               |
| 4    | Privacy Mode         | 当前/切换模式 |
|      |                      |               |
| 5    | Quick Find           | 快速查找      |
|      | Find in Files        | 在文件中查找  |
|      |                      |               |
| 6    | Entity Selection     | 实体选择      |
|      | Select All           | 全选          |
|      | Select None          | 选择无        |
|      | Invert Selection     | 反转选择      |
|      |                      |               |
|      | Add Parents          | 添加父级      |
|      | Add Children         | 添加子集      |
|      | Add Similar Siblings | 添加同级      |
|      |                      |               |
|      | Add Neighbors        | 添加相邻      |
|      | Add Path             | 添加路径      |
|      | Select Parents       | 添加父级      |
|      |                      |               |
|      | Select Children      | 选择子集      |
|      | Select Neighbors     | 选择相邻      |
|      | Select Leaves        | 选择树叶      |
|      |                      |               |
|      | Select Bookmarked    | 添加书签      |
|      | Select by Type       | 按类型选择    |
|      | Select Links         | 选择链接      |
|      | Servers Links        | 反向链接      |
|      |                      |               |
| 7    | Zoom to Fit          | 缩放至适合    |
|      | Zoom 100 %           | 缩放100%      |
|      | Zoom to              | 10~200        |
|      |                      |               |
|      | Zoom In              | 放大          |
|      | Zoom Out             | 缩小          |
|      | Zoom Selection       | 缩放选择      |
|      |                      |               |

###### 2.视角 -   View

![image-20200429161426523](/home/kun/.config/Typora/typora-user-images/image-20200429161426523.png)

| 索引 | EN                           | CN                         |
| ---- | ---------------------------- | -------------------------- |
| 1    | Manage View                  | 管理视图                   |
|      |                              |                            |
|      | None                         | 没有                       |
|      | Graph View                   | 图表视图                   |
|      | Ball Size by Diverse Descent | 不同类别的球尺寸           |
|      | Ball Size Links (All)        | 按链接列出球的大小（全部） |
|      | Ball Size by Links(Incoming) | 按链路划分的球大小（传入） |
|      | Ball Size Links(Qutoging)    | 按链路划分球大小（导出）   |
|      | Ball Size by Rank            | 按等级划分球大小           |
|      | Ball Size by Weight          | 球的重量和尺寸             |
|      |                              |                            |
|      | MAnage View                  | 管理视图                   |
|      |                              |                            |
| 2    | Block Selection              | 块选择                     |
|      | Hierarchical Selectior       | 分级选择                   |
|      | Circular Selector            | 图形选择器                 |
|      | Organic Selection            | 有机选择                   |
|      |                              |                            |
| 3    | Left Align                   | 坐对齐                     |
|      | Top Align                    | 顶部对齐                   |
|      | Bottom Align                 | 底部对齐                   |
|      |                              |                            |
|      | Right Align                  | 右对齐                     |
|      | Center Vertically            | 垂直剧中                   |
|      | Center Horiszontally         | 水平剧中                   |
|      |                              |                            |
| 4    | Show Custion Link Labels     | 显示客户链接标签           |
|      | Show Transform Link Labels   | 显示变换链接标签           |
|      | Properties Affect Aooearance | 属性影响外观               |
|      |                              |                            |
| 5    | Show Notes                   | 显示注释                   |
|      | Hide Notes                   | 隐藏注释                   |
|      |                              |                            |

###### 3.实体 - Entities

![image-20200429163022191](/home/kun/.config/Typora/typora-user-images/image-20200429163022191.png)

| 索引 | EN                         | CN                   |
| ---- | -------------------------- | -------------------- |
| 1    | New Entity Type            | 新建实体类型         |
|      | New Entitiy Type(Advanced) | 新建实体类型（高级） |
|      |                            |                      |
|      | Manage Entitiess           | 管理实体             |
|      | Import Entities            | 导入实体             |
|      | Export Entities            | 导出实体             |
|      |                            |                      |
| 2    | Manage Icons               | 管理图标             |
|      |                            |                      |

###### 4.搜集 - Collections

![image-20200429164055327](/home/kun/.config/Typora/typora-user-images/image-20200429164055327.png)

| 索引 | EN                       | CN                 |
| ---- | ------------------------ | ------------------ |
| 1    | Disable Collections      | 禁用集合           |
|      |                          |                    |
| 2    | Simplify Graph           | 简化图，左多，右少 |
|      |                          |                    |
| 4    | Show Collections Tutoria | 显示Tutoria        |
|      | Select Collections       | 选择集合           |
|      |                          |                    |

###### 5.变换 - Transforms

![image-20200429164546200](/home/kun/.config/Typora/typora-user-images/image-20200429164546200.png)

| 索引 | EN                  | CN           |
| ---- | ------------------- | ------------ |
| 1    | Transform Hub       | 转换中心     |
|      | Transform Managet   | 转换管理     |
|      | New Local Transform | 新建局部变换 |
|      |                     |              |
| 2    | Certificate Manager | 证书管理器   |
|      |                     |              |
| 4    | Manage Serbvices    | 管理服务     |
|      |                     |              |
| 5    | Run View            | 运行视图     |
|      |                     |              |

###### 6.机器 - Machines  

![image-20200429165856083](/home/kun/.config/Typora/typora-user-images/image-20200429165856083.png)

| 索引 | EN                | CN               |
| ---- | ----------------- | ---------------- |
| 1    | Run Macine        | 运行机器         |
|      | Stop all Machines | 停止运行所有机器 |
|      |                   |                  |
| 2    | New Machine       | 新建机器         |
|      | Manage Machines   | 管理机器         |
|      |                   |                  |
| 3    | Machines Window   | 机器窗口         |
|      |                   |                  |

###### 7.合作 - Collaboration

![image-20200429171040619](/home/kun/.config/Typora/typora-user-images/image-20200429171040619.png)

| 索引 | EN                     | CN           |
| ---- | ---------------------- | ------------ |
| 1    | Share New Graph        | 共享新图表   |
|      | Share Current Graph    | 共享当前图表 |
|      |                        |              |
| 2    | Chat Windows           | 聊天窗口     |
|      | Collaborationn Windows | 协作窗口     |
|      |                        |              |
| 3    | Show Usernames         | 显示用户名   |
|      |                        |              |

###### 8.导出 - Import | Export 

![image-20200429173158333](/home/kun/.config/Typora/typora-user-images/image-20200429173158333.png)

| 索引 | EN                        | CN               |
| ---- | ------------------------- | ---------------- |
| 1    | Import Graph form Table   | 从表中导入图形   |
|      | Mappings - Tabular Import | 映射-表格导入    |
|      |                           |                  |
| 2    | Export Graph to Table     | 将图表导出为表格 |
|      | Export Graph as Image     | 将图形导出为图像 |
|      | Generate Report           | 生成报告         |
|      | Export Graph as XML       | 导出图形为XML    |
|      |                           |                  |
| 3    | Import Config             | 导入配置         |
|      | Export Config             | 导出配置         |
|      |                           |                  |

###### 9.窗口 - Window

| 索引 | EN                    | CN           |
| ---- | --------------------- | ------------ |
| 1    | Close All Graphs      | 关闭所有图形 |
|      | Closs Othe Graphs     | 关闭其他图表 |
|      | Reset Windows         | 重置 Windows |
|      |                       |              |
| 2    | Hone                  | 首页         |
|      | Overview              | 概观         |
|      | Detail View           | 详细视图     |
|      |                       |              |
| 3    | Property View         | 属性视图     |
|      | Entity Palette        | 实体调色版   |
|      | Output Windows        | 输出窗       |
|      |                       |              |
| 4    | Machines Windows      | 机器窗口     |
|      | Run View              | 运行视图     |
|      | Chat Windows          | 聊天窗口     |
|      |                       |              |
| 5    | Collaboration Windows | 协作窗口     |
|      | Hub Transform Inputs  | 中枢变换输入 |
|      |                       |              |

##### 四，Maltego CE 使用

###### 1.解决安装后没有变换问题

![image-20200429185048609](/home/kun/.config/Typora/typora-user-images/image-20200429185048609.png)

此时可以在”Transform Hub“中安装你所需的相关插件。

安装的操作也非常简单，你只需要选择你需要类型的插件然后带点击 Install即可完成安装。



![image-20200429190058318](/home/kun/.config/Typora/typora-user-images/image-20200429190058318.png)

就比如我们安装名为”PeopleMon“ 的变换模块

PeopleMon是档案领域方面的领导者，他允许机构和公司创建全面的档案。

如如果你使用Maltego进行相关方面的搜索， 你甚至可以搜索和访问十亿人的个人数据资料，包括家庭地址，亲属，地址，照片，联系信息，电子邮件，社交媒体数据，违规数据等等一些符合OSINT特色的信息。



![image-20200429192947544](/home/kun/.config/Typora/typora-user-images/image-20200429192947544.png)

注册并填写信息，然后进入到OFFERS页面中点击地一个。



![image-20200429193015756](/home/kun/.config/Typora/typora-user-images/image-20200429193015756.png)



![image-20200429193117235](/home/kun/.config/Typora/typora-user-images/image-20200429193117235.png)



![image-20200429193322120](/home/kun/.config/Typora/typora-user-images/image-20200429193322120.png)



![image-20200429193409769](/home/kun/.config/Typora/typora-user-images/image-20200429193409769.png)

此时的”PeopleMon“已经完成安装，你可以选择这时重启Maldego。



###### 2.实体介绍

| 大类                          | EN                     | CN               | 描述                               |
| ----------------------------- | ---------------------- | ---------------- | ---------------------------------- |
| 设备(Devices)                 | Device                 | 设备             | 手机或照相设备                     |
|                               |                        |                  |                                    |
| 组(Groups)                    | Company                | 公司             | 商业组织                           |
|                               | Organization           | 组织             | 为集体目标分配任务的社会团体       |
|                               |                        |                  |                                    |
| 基础设施(Infrastucture) | AS                     | AS               | 互联网自治系统                     |
|                               | Banner                 | 旗帜             | 旗帜                               |
|                               | Dns Name               | 域名             | 域名系统服务器名称                 |
|                               | Domain                 | IPv4地址         | IPv4地址                           |
|                               | MX Record              | MX记录           | 域名系统邮件交互记录               |
|                               | NS Record              | 全国记录         | 域名服务器记录                     |
|                               | Netblock               | 网络块           | 一系列IPv4地址                     |
|                               | URL                    | 网址             | 一种内部统一资源定位神器           |
|                               | Tracking Code          | 跟踪代码         | 表示web服务的跟踪代码              |
|                               | Website                | 网站             | 互联网网站                         |
|                               |                        |                  |                                    |
| 位置(Locations)               | Circular Area          | 圆形区域         | 地球上某处的圆形区域               |
|                               | GPS Coordinate         | 全球定位系统坐标 | 在地球测量系统坐标中的位置哦       |
|                               | Location               | 位置             | 目标地球所在的位置                 |
|                               |                        |                  |                                    |
| 恶意软件Malware)              | Hash                   | 混淆             | 哈系实体                           |
|                               |                        |                  |                                    |
| Passive Total(第三方实体)     | SSL Certificate        | SSL证书          | SSL证书详细信息                    |
|                               |                        |                  |                                    |
| 渗透测试(Penetration Testing) | BuiltWith RelationShip | 建立关系         | 由建立者标识的关系                 |
|                               | BuiltWith Technologuy  | 建筑科技         | 由BuiltWuith识别的技术             |
|                               | port                   | 端口             | 一个网络端口                       |
|                               | Service                | 服务             | 网络服务（端口横幅组合）           |
|                               |                        |                  |                                    |
| 个人的(Personal)              | Alias                  | 别名             | 一个人的别名                       |
|                               | Document               | 文档             | 互联网上的一份文件                 |
|                               | Email Address          | 电子邮件地址     | 可以向其发送电子邮件的电子邮件邮箱 |
|                               | Image                  | 图像             | 某物的视觉表现                     |
|                               | Person                 | 人               | 代表人类的实体                     |
|                               | Phone Number           | 电话号码         | 电话号码                           |
|                               | Phrase                 | 短语             | 任何文本或其他部分                 |
|                               | Sentiment              | 感情             | 代表了一个人对物体的感情           |
|                               |                        |||
| Passive Total(第三方实体)     |                        |                  |                                    |
| 社交网络(Social Network)      | Twitter                | 推特             | Twitter实体                        |
|                               | Twitter User Lint      | 推特用户列表     | 推特用户实体                       |
|                               | Hashtag                | 标签             | 推特标签                           |
|                               |                        |                  |                                    |
| PeopleMon(第三方插件)         | Background             | 背景             | 搜寻背景                           |
|                               | Board Member           | 董事会成员       | 搜寻董事会成员                     |
|                               | Car Details            | 汽车详情         | 搜寻相关汽车信息                   |
|                               | Details                | 细节             | 查询细节                           |
|                               | Detailed Info          | 详情信息         | 查询详情信息                       |
|                               | Donor                  | 捐赠者           | 查询捐增者信息                     |
|                               | Email Data             | 电子邮件数据     | 查询泄漏来源的数据                 |
|                               | Email data             | 电子邮件数据     | 查询泄漏来源的数据                 |
|                               | Email source           | 电子邮件来源     | 泄漏的来源                         |
|                               | Facebook               | 脸书网           | 查询脸书指定的信息                 |
|                               | Filckr                 | Filckr           | Filckr                             |
|                               | Instagram              | Instagram        | Instagram详情信息                  |
|                               | Instagram              | 投资者           | 搜寻投资者信息                     |
|                               | Person                 | 人               | 搜寻人员                           |
|                               | Phone Details          | 电话             | 电话详情信息                       |
|                               | Phone Details          | 电话详情信息     | 搜寻电话详情信息                   |
|                               | Phone data             | 电话数据         | 搜寻电话数据                       |
|                               | Phones                 | 电话             | 搜寻电话信息                       |
|                               | Photos                 | 照片             | 搜寻照片信息                       |
|                               | Pinterest              | 品质             | 品质细节                           |
|                               | Shareholder            | 股东             | 搜寻股东信息                       |
|                               | Social Links           | 社会联系         | 社会联系                           |
|                               | Twitter                | 推特             | 推特详情                           |
|                               | Whatsapp               | Whatsapp         | Whatsapp详情信息                   |



###### 3.使用Maltego实体

__- 新建项目__

![image-20200430002824613](/home/kun/.config/Typora/typora-user-images/image-20200430002824613.png)

Maltego的实体使用非常的简单，你可以在"Infrastucture"基础设施中选择Websitez添加到新建项目中，而Walgego会从该网站中搜索所有公开的信息。



__- 扫描项目中在进行搜索__

![image-20200430003952399](/home/kun/.config/Typora/typora-user-images/image-20200430003952399.png)

操作与第一次相同，此时你可以根据搜索出的结果继续进行搜索。



###### 4.使用机器人

![image-20200430011312985](/home/kun/.config/Typora/typora-user-images/image-20200430011312985.png)

使用下文新建的名为 “Dns web size”的机器人，对Ipv4站点进行相关方面的搜寻。

输入相关的IPV4域名后即可对站点进行 OSINT的信息搜集，主要搜集DNS信息。

![image-20200430011544941](/home/kun/.config/Typora/typora-user-images/image-20200430011544941.png)



##### 五.实体

Maltego基本上形成了“互相依赖”的这一个鲜明的特点个，这就比如当你新建一个实体的话，那你需要用到机器人，如过你没有为实体添加机器人，那么你的实体也和空壳也没有什么区别。



###### 1.新建实体

![image-20200430000400816](/home/kun/.config/Typora/typora-user-images/image-20200430000400816.png)

将实体种类设置为“Personal”，并将基础实体设置为“Maltego.WebTitle”



![image-20200430000507087](/home/kun/.config/Typora/typora-user-images/image-20200430000507087.png)

你可以在这个页面中添加描述和样本值及类型等进行相关的设置或添加



![image-20200430000958399](/home/kun/.config/Typora/typora-user-images/image-20200430000958399.png)



![image-20200430000839428](/home/kun/.config/Typora/typora-user-images/image-20200430000839428.png)

你可以新建一个项目或在“Entitles”中的“Manage Entitles”中进行查看



在Maltego中，创建高级实体与普通实体相关步骤基本相似，可自行操作。



##### 六.机器

而机器，依赖与变换，如果你没有一个变换，那么你是不会成功创建一个可以运行的机器。而这也将构成了Maltego中的一个重要一环。



###### 1.新建机器

![image-20200429232618543](/home/kun/.config/Typora/typora-user-images/image-20200429232618543.png)



| EN            | CN       | 描述                            |
| ------------- | -------- | ------------------------------- |
| Macro         |          | 这种机器启动时运行一次          |
| Timer Machine | 计时器   | 机器类型定期运行，直到停止      |
| Blank machine | 空白机器 | 空白机器 创建机器时不要使用模板 |



![image-20200430010058836](/home/kun/.config/Typora/typora-user-images/image-20200430010058836.png)

​	

默认代码，你可以在里面调用切换并使得自己的机器人更加的强大。

````
//Welcome to Maltego Machines!

//Each machine starts with a statement like this
machine("backsunli.", 
        displayName:"One by Machine", 
        author:"",
        description: "") {

    //A macro machine has a start function like this
    start {

        //Put the sequence of transforms to run in here...

        //For example, We will start with a Domain and get the MX records for it
        run("paterva.v2.DomainToMXrecord_DNS") //iPv4域名
        
        //Then we resolve these MX records to IP Addresses
        run("paterva.v2.DNSNameToIPAddress_DNS") 
//IPv4地址
    }
}
//Of course there is much more you can do with machines... Have fun!

````

![image-20200429235302240](/home/kun/.config/Typora/typora-user-images/image-20200429235302240.png)

将此打上勾即可完成自建机器人，你可以在“Machine Manager中看到”



##### 七，变换

在Maltego的环境了里面，变换基本上就是Maltego中的一个微小的核心，在前面所讲的“实体” or “机器人”，都是依赖于变换。

Maltego中基本上形成了“互相依赖”的这一个鲜明的特点个，并且这将会让Maltego成为一个特点，大大增强了Maltago的扩展性和可自定义性。

这也方便了安全人员或是情报人员及分析师等专业认识进行相关方面的扩展和应用。



当然，你也可以尝试选择新建一个 变换，只不过这样有点小麻烦。。

