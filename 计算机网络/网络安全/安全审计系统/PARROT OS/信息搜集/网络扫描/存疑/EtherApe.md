# EtherApe

EtherApe是一个模仿etherman的Unix图形网络监视器。它采用链路层、IP和TCP模式，以图形方式显示网络活动。主机和链路的大小随流量而变化。彩色编码协议显示。

它支持以太网、FDDI、令牌环网、ISDN、PPP、SLIP和无线局域网设备，以及几种封装格式。它可以过滤要显示的流量，可以从文件中读取数据包，也可以从网络中实时读取。 可以导出节点统计信息。



_https://etherape.sourceforge.io/_

---



##### 一，界面翻译

###### 可见

__头部__

![image-20200502171906373](/home/kun/.config/Typora/typora-user-images/image-20200502171906373.png)

| EN    | CN     | 描述 |
| ----- | ------ | ---- |
| Start | 关闭   |      |
| Next  | 下一个 |      |
| Pause | 暂停   |      |
| Stop  | 停止   |      |
| Pref  | 设置   |      |
| Prot  | 端口   |      |
| Nodes | 节点   |      |



__File - 文件__

| EN          | CN       | 描述 |
| ----------- | -------- | ---- |
| Open        | 打开     |      |
| Export      | 导出     |      |
| Preferences | 设置偏好 |      |
| Quit        | 退出     |      |



__Capture - 捕获__

| EN         | CN     | 描述 |
| ---------- | ------ | ---- |
| Mode       | 模式   |      |
| Interfaces | 接口   |      |
| Play       | 开始   |      |
| Next       | 下一个 |      |
| Pause      | 终止   |      |
| Stop       | 关闭   |      |



__View - 视图__

| EN          | CN             | 描述 |
| ----------- | -------------- | ---- |
| Protocols   | 协议           |      |
| Nodes       | 节点           |      |
| Full screen | 全屏           |      |
| Toolbar     | 工具栏是否开启 |      |
| Legend      | 图列           |      |
| Status Bar  | 状态栏         |      |



__Help - 帮助__

| EN    | CN   |
| ----- | ---- |
| Help  | 帮助 |
| About | 关于 |



###### 不可见

__偏好设置__

![image-20200502182215047](/home/kun/.config/Typora/typora-user-images/image-20200502182215047.png)



![image-20200502185715591](/home/kun/.config/Typora/typora-user-images/image-20200502185715591.png)



__Colors 界面__

![image-20200502190847996](/home/kun/.config/Typora/typora-user-images/image-20200502190847996.png)

| 界面             | EN                              | CN                    |
| ---------------- | ------------------------------- | --------------------- |
| Diagram          |                                 | 图表                  |
|                  | Prootoocol Stack Level          | 协议栈水平            |
|                  | Size Variable                   | 尺寸变量              |
|                  | Size Mode                       | 尺寸模式              |
|                  | Node Radius Multiplier          | 节点半径乘数          |
|                  | Link Width - Node Radius Ration | 链路宽度 - 节点半径比 |
|                  | Central Node                    | 中心节点              |
|                  | Inner Ring Scale                | 内环秤                |
|                  |                                 |                       |
|                  | Capture Filter                  | 捕获过滤器            |
|                  | ode Label Font                  | 节点标签字体          |
|                  | Node Label Color                | 节点标签颜色          |
|                  | Hide Node Names                 | 隐藏节点名称          |
|                  | Group Unknown Ports             | 对未知端口进行分组    |
|                  | Name RResolution                | 名字解析              |
|                  | Background Image                | 背景图像              |
|                  | Display pcap stats              | 显示PCAP统计信息      |
|                  |                                 |                       |
| Colors           |                                 | 修改颜色              |
|                  | Add Color                       | 添加颜色              |
|                  | Remove color                    | 删除颜色              |
|                  | Change color                    | 更改颜色              |
|                  | Edit protocol                   | 编辑协议对应颜色      |
|                  |                                 |                       |
| Timings          |                                 | 计时                  |
|                  | Diagram Refresh eriod (ms)      | 图表刷新周期（毫秒）  |
|                  | Averaging Time(ms)              | 平均时间（毫秒）      |
|                  |                                 |                       |
| Node Timeouts(s) |                                 | 节点超时              |
|                  | Diagram                         | 图表                  |
|                  | Traffic Statistics              | 交通统计              |
|                  | Protocol Statics                | 协议统计              |
|                  |                                 |                       |
| Link Timeouts(s) |                                 | 链接超时              |
|                  | Diagram Traffic Statistics      | 图表流量统计          |
|                  | Protocol Statistics             | 协议统计              |
|                  |                                 |                       |
|                  | Global Protocol Timeouts（s）   | 全局协议超时时间      |





##### 二，具体使用
###### 1.打开端口数据页面
![image-20200502200332557](/home/kun/.config/Typora/typora-user-images/image-20200502200332557.png)

| EN            | CN           |
| ------------- | ------------ |
| Protocols     | 协议         |
| Port          | 端口         |
| Inst Traffic  | 流量         |
| Accum Traffic | 累计流量     |
| Avg Size      | 平均大小     |
| Last Heard    | 最后一次收到 |
| Packets       | 数据包       |



###### 2.查看节点数据页面

![image-20200502202935030](/home/kun/.config/Typora/typora-user-images/image-20200502202935030.png)

| EN            | CN           |
| ------------- | ------------ |
| Name          | 名称         |
| Address       | 地址         |
| Inst Traffic  | 流量         |
| Accum Traffic | 累计流量     |
| Avg Size      | 平均大小     |
| Last Heard    | 最后一次收到 |
| Packets       | 数据包       |

