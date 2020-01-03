# python

1. `use sublime Text进行python 编写`
```
* 选择语言是 python
* command + B : 可以看到运行的结果
```
2. `动态语言和静态语言`
```
* 这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量
时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如 Java 是静态语言
```
3. `赋值`
```
* a, b, c = 1, 2, "liangdianshui"
* 两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "liangdianshui" 分配给变量 c。
```
4. `python中的可更改对象和不可更改对象` 
```
* 在 Python 中，字符串，整形，浮点型，tuple 是不可更改的对象，而 list ， dict 等是可以更改的对象
* 实质是 值传递(copy值传递，参数本身没改变) 和 实参传递的区别
```
5. `内置函数isinstance()进行数据类型检查，检查调用函数时参数是否是整形和浮点型`
```
# -*- coding: UTF-8 -*-

def sum(num1,num2):         // def : 定义一个函数
    # 两数之和
    if not (isinstance (num1,(int ,float)) and isinstance (num2,(int ,float))):
        raise TypeError('参数类型错误')     // 提示错误
    return num1+num2

print(sum(1,2))
```
6. `object 是python中所有类的基类 : 测试同一性,也正好利用这个特性，来判断是否有值输入`
```
_no_value =object()

def print_info( a , b = _no_value ):
    if b is _no_value :
        print('b 没有赋值')
    return;
```
7. `迭代器`
```
* 迭代器是一个可以记住遍历的位置的对象
* 迭代器只能往前不会后退
* 迭代器对象可以使用常规for语句进行遍历，也可以使用next()函数来遍历
```
```
* 创建迭代器 ： iter()

list1 = [1,2,3,4]
iter2 = iter ( list1 )
```
8. `map 和 lambda 的使用方式`
```
>>> x  = [1,2 ,3]
>>> y = map(lambda x : x +1 ,x)
>>> print(list(y))
[2, 3, 4]
```