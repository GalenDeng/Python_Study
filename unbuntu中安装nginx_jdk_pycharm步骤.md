# unbuntu中安装nginx_jdk_pycharm步骤 (2019.07.05)

* [JDK安装步骤](https://blog.csdn.net/smile_from_2015/article/details/80056297)
```
* tar -zxvf jdk-8u171-linux-x64.tar.gz
* cd  /usr/lib
* sudo mkdir jdk
* sudo mv xxx yyy
* sudo vi /etc/profile
* 
export JAVA_HOME=/usr/lib/jdk/jdk1.8.0_171
export JRE_HOME=${JAVA_HOME}/jre    
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib    
export PATH=${JAVA_HOME}/bin:$PATH 
* source /etc/profile 
```

* `pycharm安装`
```
* sudo add-apt-repository ppa:mystic-mirage/pycharm
* sudo apt-get update
* sudo apt-get install pycharm-community
```