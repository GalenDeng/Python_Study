# python 常用命令行
1. `python3`
```
* pip3 install --upgrade pip 升级pip3的version
* pip3 install xxx : install software
* pip3 install mysqlclient : 有可能有些库的路径错了，要 whereis/which 出 mysql_config 的文件路径 ，vim this file , use -L / -l 定位
* -lssl 是在 openssl 中的
* pip3 list : 列出已安装的模块
```
2. `常用命令及操作`
```
* `tab键`
如果只是编辑某个文件时候想一个tab=4个空格，那么在打开文件后，
:set   softtabstop=4

* `vim模式下`
1） uu 撤销
```
3. `Mysql`
```
* mysql -u root -p : 连接数据库
```
4. `前后端分离`
```
前后端不分离: 前端看到的页面效果是由后端进行控制的，后端进行模板渲染，返回渲染之后完整页面。
前后端分离 : 后端只返回前端所需要的数据，至于数据在前端怎么展示，由前端自己控制
```
5. `序列化`
```
* 序列化: 在上面例子中，把模型对象转换为python字典或json数据过程，就叫做序列化过程。

* 反序列化: 在上面例子中，把字典数据和json数据转换保存到模型对象中过程，就叫做反序列化过程。
```
