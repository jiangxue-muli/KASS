# Docker 容器管理

---

| docker ps |      |
| --------- | ---- |
| 查看容器  |      |

---



###### 一，查找容器

```
docker search mysql
查找mysql容器
```



###### 二，获取镜像

```
docker pull mysql 
获取Mysql镜像
```



###### 三，启动容器

```
# ------------------------------------------------------------+
# -i 交互式操作 -t 终端 镜像容器 /bin/bash 进入后可以使用exit退出    /
# ------------------------------------------------------------+

docker run -it mysqldb /bin/bash
进入Mysql交互式终端
```



###### 四，后台运行

```
# ------------------------------------------------------------+
# -d 指定运行模式 “-d”参数默认不会进入容器，可使用 docker exec 进入  /
# ------------------------------------------------------------+

docker run -itd --name [NAMES] [IMAGE] /bin/bash	
```



###### 五，停止/重启容器

```
# ------------------------------------------------------------+
# docker stop 停止容器				docker restart 重启容器     /
# ------------------------------------------------------------+

docker stop [CONTAINER ID]
docker restart [CONTAINETR ID]
```



###### 六，进入容器

````
# -------------------------------------------------------------+ 
# docker attach 退出了容器也会停止	docker exec 退出后容器正常运行  /
# -------------------------------------------------------------+

docker attach [CONTAINNER ID]
docker exec -it [CONTAINER ID] [COMMAND]
````



###### 七，导入/出容器

```
# ---------------------------------------------------------------+
# docker export [CONTAINER ID] > [文件名]	 			  /  导出  /
# ---------------------------------------------------------------+
# cat docker/[文件名] | docker import -test [REPOSITORY]:[TAG] /入/
# ---------------------------------------------------------------+
# docker import [HTTPS/HTTP] example.com/imagerepo	   / URL导入 /
# ---------------------------------------------------------------+
```



###### 八，删除容器

```
docker rm -f [CONTAINER ID]
```





