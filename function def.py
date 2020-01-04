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

#闭包
def count():
    def f(j):
        def g():
            return j*j
        return g #返回的是这个函数，在必要的时候再进行计算
    fs = []
    for i in range(1, 4):
        print(f(i))
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
        print(fs)
    return fs

f1,f2,f3 = count()
f2()
f1()
f3()

#匿名函数
#lambda表示匿名函数，冒号前面的x表示函数参数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
f = lambda x:x*x
f(4)
#__name__函数的名字
f.__name__
