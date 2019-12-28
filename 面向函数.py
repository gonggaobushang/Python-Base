def f(x):
    return x*x
# map返回一个Iterator
a = map(f,[1,2,3,4])
list(a)


#filter 过滤序列
def odd(x):
    return x % 2 == 1
#把符合的偶数删除
list(filter(odd,[1,2,3,4,5]))
#返回的也是Iterator
def empty(x):
    return x and x.strip()
#删除空字符串
list(filter(empty,['1','',None,'  ']))

    
def _odd_iter_1():
    n = 1
    while True:
        n = n + 2
        return n #返回
_odd_iter_1()

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n #返回,但是创建的是generator
_odd_iter()    

#排序
sorted([-12,32,2])
sorted([-12,32,2],key=abs)
#对字符串排序，是按照ASCII的大小比较的，Z' < 'a'
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower,reverse=True)

