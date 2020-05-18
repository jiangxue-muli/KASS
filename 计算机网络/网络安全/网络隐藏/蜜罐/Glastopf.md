# Glastopf

Glastopf是由Lukas Rist创建的一个Python网络应用程序蜜罐。

漏洞类型模拟，而不是漏洞模拟。一旦模拟了漏洞类型，Glastopf就可以处理相同类型的未知攻击。虽然实现可能更慢更复杂，但我们仍然领先于攻击者，直到他们想出新方法或发现我们实现中的新缺陷。 模块化设计，添加新的日志记录功能或攻击类型处理程序。各种数据库功能已经就位。集中式数据收集支持HPFeeds日志记录。 流行的攻击类型仿真已经就位:通过内置的PHP沙盒实现远程文件包含，通过虚拟文件系统提供文件的本地文件包含，以及通过POST请求实现的HTML注入。 对手通常使用搜索引擎和特制的搜索请求来寻找他们的受害者。为了吸引他们，Glastopf提供了这些关键字(又名“呆子”)，并从请求中提取它们，自动扩展其攻击面。结果，蜜罐变得越来越有吸引力，每一次新的攻击都试图攻击它。 我们将使SQL注入模拟器公开，为爬虫识别和智能呆子选择提供IP分析。



_——Lukas Rist_

_https://github.com/mushorg/glastopf_

---



#### 一，所需环境

系统<kbd>Ubuntu 12</kbd>



__更新源__

> 以下是国内的一些相关更新源，由于版本依赖的问题其中包含了很多旧版本的更新源，具体添加方法可使用如下两个命令：
>
> gedit /etc/apt/sources.list 也可以使用 vi /etc/apt/sources.list
>
> 之后使用 apt-get update 进行更新即可

```
# 清华源
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse


# 阿里源
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse

# 腾讯源
deb http://mirrors.cloud.tencent.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.cloud.tencent.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.cloud.tencent.com/ubuntu/ xenial-updates main restricted universe multiverse
#deb http://mirrors.cloud.tencent.com/ubuntu/ xenial-proposed main restricted universe multiverse
#deb http://mirrors.cloud.tencent.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.cloud.tencent.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.cloud.tencent.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.cloud.tencent.com/ubuntu/ xenial-updates main restricted universe multiverse
#deb-src http://mirrors.cloud.tencent.com/ubuntu/ xenial-proposed main restricted universe multiverse
#deb-src http://mirrors.cloud.tencent.com/ubuntu/ xenial-backports main restricted universe multiverse

# 老更新源
deb http://old-releases.ubuntu.com/ubuntu/ karmic main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu/ karmic-security main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu/ karmic-updates main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu/ karmic-proposed main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu/ karmic-backports main restricted universe multiverse
deb-src http://old-releases.ubuntu.com/ubuntu/ karmic main restricted universe multiverse
deb-src http://old-releases.ubuntu.com/ubuntu/ karmic-security main restricted universe multiverse
deb-src http://old-releases.ubuntu.com/ubuntu/ karmic-updates main restricted universe multiverse
deb-src http://old-releases.ubuntu.com/ubuntu/ karmic-proposed main restricted universe multiverse
deb-src http://old-releases.ubuntu.com/ubuntu/ karmic-backports main restricted universe multiverse


# 中科大8.10
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid-security main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid-updates main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid-proposed main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid-backports main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid-security main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid-updates main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid-proposed main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ intrepid-backports main restricted universe multiverse

# 中科大12
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic-security main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic-updates main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic-proposed main restricted universe multiverse
deb http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic-backports main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic-security main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic-updates main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic-proposed main restricted universe multiverse
deb-src http://mirrors.ustc.edu.cn/ubuntu-old-releases/ubuntu/ utopic-backports main restricted universe multiverse

# 中科大12。04
deb http://debian.ustc.edu.cn/ubuntu/ precise main restricted universe multiverse
deb http://debian.ustc.edu.cn/ubuntu/ precise-backports restricted universe multiverse
deb http://debian.ustc.edu.cn/ubuntu/ precise-proposed main restricted universe multiverse
deb http://debian.ustc.edu.cn/ubuntu/ precise-security main restricted universe multiverse
deb http://debian.ustc.edu.cn/ubuntu/ precise-updates main restricted universe multiverse
deb-src http://debian.ustc.edu.cn/ubuntu/ precise main restricted universe multiverse
deb-src http://debian.ustc.edu.cn/ubuntu/ precise-backports main restricted universe multiverse
deb-src http://debian.ustc.edu.cn/ubuntu/ precise-proposed main restricted universe multiverse
deb-src http://debian.ustc.edu.cn/ubuntu/ precise-security main restricted universe multiverse
deb-src http://debian.ustc.edu.cn/ubuntu/ precise-updates main restricted universe multiverse

# 中科大14
deb http://mirrors.163.com/ubuntu/ wily main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ wily-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ wily-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ wily-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ wily-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ wily main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ wily-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ wily-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ wily-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ wily-backports main restricted universe multiverse
```



