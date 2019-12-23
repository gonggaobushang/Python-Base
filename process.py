#切片
list(range(100))[-2:-1] #range从0开始结束于99，[-2:-1]就表示倒数第二个，不包括倒数第一个
list(range(100))[:10:2] #每隔2但不包括10
list(range(100))[::5] #从0开始每隔5
'lebron jordan'[::3]

#迭代
d = {"a":'1' ,"b":'3' ,"c":'2'} #dict
#判断是否为str
isinstance(d['a'],str)
#按key迭代
for i in d:
    print(i)
#按value迭代
for i in d.values():
    print(i)    
 #迭代所有   
for i in d.items():
    print(i)    
    
[a + '!=' + b for a,b in d.items()]
    
# 同时迭代索引和值   
for i,j in enumerate(['air',11,"asd"]):
    print(i,j)

for x,y in [(1,2),(2,3)]:
    print(x,y)
    
L=[]
for i in range(1,11):
    L.append(i*i)
print(L)

#在列表中直接进行判断
[x*x for x in range(1,11) if x%2 ==0]

#多层循环
[x+y+z for x in 'aA' for y in 'SD' for z in '123']

import os
[d for d in os.listdir()]


#不创建完整的list，从而节省大量储存的空间
#生成器generator
[x for x in range(1,11)]
#括号的形式
g = (x for x in range(1,11))
next(g)
# next(g)会对下面的g造成影响
for t in g:
    print(t)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
dt = odd()
#在每次调用next()的时候执行
#遇到yield语句返回
#再次执行时从上次返回的yield语句处继续执行
next(dt)


#判断是否为可迭代对象 Iterable
from collections import Iterable
isinstance([],Iterable)
#判断是否是可以不断被next()调用的迭代器 Iterator
from collections import Iterator
isinstance([],Iterator)

for x in [1,2,3,4,5]:
    pass
#等价于
y = iter([1,2,3,4,5])
#Iterator对象
while True:
    try:
        next(y)
    except StopIteration:
        break
