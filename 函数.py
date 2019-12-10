def myabs(x):
    if not isinstance(x ,(int,float)):
        raise TypeError("no number!!!!!!")
    if x >= 0:
        return x,"OK"
    else:
        pass #空函数

myabs(2000.1)
myabs(-0000.1)
myabs("sad")




# *可以任意个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(2,1)
calc()

# **可以任意关键词参数
def another(a,**kw):
    print('a=',a,'another=',kw)
another(a=1)
another(1, bl="bad")
#dict形式传入
temp = {"this":123}
another(123,This=temp['this'])
another(123, **temp)


# 参数定义的顺序必须是必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1,2,3)
f1(1, 2, 3, 'a', 'b', x=99)
f1(1, 2, 3, 'a', 'b', x=99)

#递归函数 
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

fact(1)
fact(2)
fact(3)
# 过深的调用会导致栈溢出