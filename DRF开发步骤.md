# DRF开发步骤 (2019.10.29)

1. `DRF一般开发流程`
```
新建工程 ---> 配置Settings ---> Models ---> Serialization ---> Views / Viewsets ---> Urls&Router
```
2. `开发案例介绍`
* [基于Django前后端分离开发-新闻管理系统 ](https://github.com/Cherish-sun/NEWS/tree/master)

3. `party案例过程`
```
* cd xxx目录
* django-admin startproject partygaosan5backend // create project
* cd partygaosan5backend
* django-admin startapp     signuprecord        // create app
* python3 -m venv venv  // create separate env : 为了与笔记本本来的系统的bin程序区分隔离
* source venv/bin/active : 进入到这个 separate env
* pip3 install -U pip   // 更新包管理工具
* pip3 install xxx      // install xxx package 

// install package
pip3 install django==2.0.3
pip3 install djangorestframework==3.8.2
pip3 install pymysql

pip3 list // 查看 installed packages + version
```