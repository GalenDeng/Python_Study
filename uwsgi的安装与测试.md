# uwsgi的安装与测试 (2019.07.02)

* [Python+Django+Nginx+Uwsgi](https://blog.csdn.net/qq_42314550/article/details/81805328)

1. `install`
* pip3 install uwsgi

2. `test`
* 在任意目录下，touch  test.py, add the following content 
```
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]
```
* uwsgi --http :8009 --wsgi-file test.py  // 8009 （可 set arbitrary port）

3. `浏览器上访问验证`
* input localhost:8009, then we can see "Hello World"