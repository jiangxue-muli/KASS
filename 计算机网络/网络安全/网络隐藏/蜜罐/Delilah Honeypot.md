# Delilah Honeypot

Delilah是一个蜜罐系统，灵感来自Jordan Wright的Elastichoney (https://github.com/jordan-wright/elastichoney)，旨在吸引那些积极利用Elasticsearch Groovy漏洞的攻击者(http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=2015-1427)。Delilah充当一个脆弱的Elasticsearch实例，用于检测和识别攻击命令、侦察尝试和下载命令(特别是“wget”和“curl”)。每当攻击者发出下载命令时，Delilah将尝试下载攻击者试图在受害者的系统上引入的文件，以便让分析人员有机会在以后分析这些文件。每当Delilah检测到攻击者的命令时，就会向一个或多个电子邮件地址发送通知电子邮件，以便实时向分析人员发出攻击警报。

Delilah提供了各种可配置的参数来模拟Elasticsearch实例，防止攻击者轻易判断它们是否与蜜罐交互。

可以安装多个Delilah节点来形成传感器网络。为了更方便地查看传感器网络，分析人员应该使用Delilah Monitor。Delilah Monitor是一个简单的web界面，它将查询每个指定的Delilah节点，并为整个传感器集合生成一个按时间顺序排列的事件视图。如果不需要更大的传感器网络，Delilah Monitor也可以用于单个节点。

Delilah和Delilah Monitor是基于Python的，将运行在支持Python的操作系统上。Delilah和Deililah Monitor已经在Ubuntu Linux和Windows操作系统上进行了测试。

有关利用Elasticsearch漏洞进行攻击的DDoS僵尸网络以及如何使用Delilah确定这些攻击背后的参与者的行为的更多信息，请访问以下URL: http://www.novetta.com/library/downloads/#NTRG。



_——by Novetta_

---

