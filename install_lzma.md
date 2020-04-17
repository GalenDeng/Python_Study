# install lzma的方法 （2020.04.17）

* [python3安装pandas库出现Could not import the lzma module](https://blog.csdn.net/sunxiaoju/article/details/103671548)
* 最好在 venv 虚拟环境下 install package
* pip install pandas   // pandas 需要 lzma 包， 不然在linux上 import pandas 会失败
* yum install -y xz-devel
* pip install backports.lzma