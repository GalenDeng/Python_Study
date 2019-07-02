# coding=UTF-8
# 判断是否为一个大于8的数
a=45
if a>=8:
	print("Yes")
else:
	print("No")	
# \ : 为转义字符	
b="hello \'两点睡\'"
list4 = [x * x for x in range(1,10)]
print(list4)
#for i in range(1, 10):
 #       for j in range(1, i+1):
            # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
 #           print('{}x{}={}\t'.format(i, j, i*j), end='')  
 #       print()

print(b)
tuple1 = ("galen","is","a","good","man")
print(tuple1)
tuple2 = ("hello",)
print(tuple2)
dict = {"name":"galen","sex":"boy"}
print(dict)
dict["name"] = "Gogo"
print(dict)
list1=[ "两点水",'twowter','liangdianshui',123]
print(list1)
# 通过索引对列表的数据项进行修改或更新
list1[2]=456
print(list1)
# 使用 append() 方法来添加列表项
list1.append('hello');
print(list1)
