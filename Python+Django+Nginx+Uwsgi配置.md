# Python+Django+Nginx+Uwsgi配置教程 （2019.07.03）

* [配置参考过程](https://blog.csdn.net/qq_42314550/article/details/81805328)
* [python django nginx简要说明和配置](https://blog.csdn.net/hkhaik/article/details/80432468)
* [mac下安装nginx](https://www.cnblogs.com/meng1314-shuai/p/8335140.html)

* `流程理解`
```
流程:
    1. 首先客户端请求服务资源，
    2. nginx作为直接对外的服务接口,接收到客户端发送过来的http请求,会解包、分析，
    3. 如果是静态文件请求就根据nginx配置的静态文件目录，返回请求的资源，
    4. 如果是动态的请求,nginx就通过配置文件,将请求传递给uWSGI；uWSGI 将接收到的包进行处理，并转发给wsgi，
    5. wsgi根据请求调用django工程的某个文件或函数，处理完后django将返回值交给wsgi，
    6. wsgi将返回值进行打包，转发给uWSGI，
    7. uWSGI接收后转发给nginx,nginx最终将返回值返回给客户端(如浏览器)。
    *注:不同的组件之间传递信息涉及到数据格式和协议的转换*
作用: 
    1. 第一级的nginx并不是必须的，uwsgi完全可以完成整个的和浏览器交互的流程； 
    2. 在nginx上加上安全性或其他的限制，可以达到保护程序的作用； 
    3. uWSGI本身是内网接口，开启多个work和processes可能也不够用，而nginx可以代理多台uWSGI完成uWSGI的负载均衡； 
    4. django在debug=False下对静态文件的处理能力不是很好，而用nginx来处理更加高效。

直接使用uwsgi启动: （发现static静态文件没生效，需要配置http://uwsgi-docs.readthedocs.io/en/latest/StaticFiles.html）
uwsgi --http :8056 --wsgi-file dirserver/wsgi.py	#自己开http服务
uwsgi --socket :8056 --wsgi-file dirserver/wsgi.py  	#使用nginx配合使用时
或修改uwsgi.ini配置表
uwsgi --ini uwsgi.ini启动

```