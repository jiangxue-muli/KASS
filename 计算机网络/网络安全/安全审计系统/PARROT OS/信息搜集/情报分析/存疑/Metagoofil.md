

# Metagoofil

在笔测试期间进行文档和元数据侦察的最佳工具之一是metapril，由边缘安全组的Christian Martorella @laramies编写。源代码可以在这里找到:https://github.com/laramies/metagoofil,.

但默认情况下，它带有Kali。该工具已经有几年没有更新了，可以使用一些薄层色谱。



_——Christian Martorella @laramies_

---



###### 一，帮助文档

[CN]:翻译

usage: metagoofil.py [-h] -d 域 [-e 延时] [-f] [-i URL_TIMEOUT] [-l SEARCH_MAX] [-n 										DOWNLOAD_FILE_LIMIT] [-o SAVE_DIRECTORY] [-r NUMBER_OF_THREADS] -t
                    				    FILE_TYPES [-u [USER_AGENT]] [-w]

​	Metagoofil - Search and download specific filetypes
​	optional arguments:

	-h, --help 						显示此帮助消息并退出
	
	-d DOMAIN 						要搜索的域。
	
	-e DELAY 						搜索之间的延迟(秒)。如果太小，谷歌可能会屏蔽你的知识产权；如果太大，你的搜索可能需要一段时间。默认:30.0
	
	-f 								将html链接保存到html_links_&lt;TIMESTAMP &gt;。txt文件。			
	
	-i URL_TIMEOUT 					不可访问/过期页面超时前等待的秒数。默认值:15
	
	-l SEARCH_MAX					要搜索的最大结果。默认值:100
	
	-n DOWNLOAD_FILE_LIMIT			每个文件类型可下载的最大文件数。默认值:100
	
	-o SAVE_DIRECTORY 				保存下载文件的目录。DEFAULT是cwd，" "
	
	-r NUMBER_OF_THREADS 			搜索线程数。默认值:8
	
	-t FILE_TYPES					要下载的文件类型(pdf、doc、xls、ppt、odp、ods、docx、xlsx、pptx)。要搜索所有17，576个三字母文件扩展名，请键入“all”
	
	-u [USER_AGENT] 				针对-d域的文件检索的用户代理
									no -u = "Mozilla/5.0(兼容；Google bot/2.1；+http://www.Google.com/bot.html)
									
	-u =随机用户-代理
	-u“我的自定义用户代理2.0”=您的自定义用户代理
	下载文件，而不仅仅是查看搜索结果
[EN]:官方

usage: metagoofil.py [-h] -d DOMAIN [-e DELAY] [-f] [-i URL_TIMEOUT] [-l SEARCH_MAX] [-n DOWNLOAD_FILE_LIMIT] [-o SAVE_DIRECTORY] [-r 							NUMBER_OF_THREADS] -t 
          				 FILE_TYPES [-u [USER_AGENT]] [-w] 

Metagoofil - Search and download specific filetypes

```
optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN             Domain to search.
  -e DELAY              Delay (in seconds) between searches. If it's too small Google may block your IP, too big and your search may take a while. DEFAULT:
                        30.0
  -f                    Save the html links to html_links_<TIMESTAMP>.txt file.
  -i URL_TIMEOUT        Number of seconds to wait before timeout for unreachable/stale pages. DEFAULT: 15
  -l SEARCH_MAX         Maximum results to search. DEFAULT: 100
  -n DOWNLOAD_FILE_LIMIT
                        Maximum number of files to download per filetype. DEFAULT: 100
  -o SAVE_DIRECTORY     Directory to save downloaded files. DEFAULT is cwd, "."
  -r NUMBER_OF_THREADS  Number of search threads. DEFAULT: 8
  -t FILE_TYPES         file_types to download (pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx). To search all 17,576 three-letter file extensions, type "ALL"
  -u [USER_AGENT]       User-Agent for file retrieval against -d domain.
                        no -u = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                        -u = Randomize User-Agent
                        -u "My custom user agent 2.0" = Your customized User-Agent
  -w                    Download the files, instead of just viewing search results.
```



无法正常运行，当前系统环境:	
<kbd>Linux parrot 5.4.0-4parrot1-amd64 #1 SMP Parrot 5.4.19-4parrot1 (2020-02-27) x86_64 GNU/Linux</kbd>

![image-20200430184431008](/home/kun/.config/Typora/typora-user-images/image-20200430184431008.png)



```
如果你恰好对Metagoofil有相关方面的使用（正常使用），或者说是解决方法，请联系:backsunli@yeah.net
```



