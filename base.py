print('I\'am \"OK\"')
print('\\\\t\\')
print(r'\\\t\\') #r''表示\不转义
print('''
      this is awesome
      '''
      )
print("hello%%, %s ,this is %f and %d" % ("milk",1 , 1))
print("hello%%,{0} ,this is{1:.6f} and {2}" .format("milk",1 , 1))   
# None表示空值

 #字符编码
chr(2133)
'ABC'.encode('ascii')
'中国'.encode('utf-8')
b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf_8',errors='ignore')
len('中国')

clss1 = ["class",0,"1"]
clss1[0]
clss1[-1]
clss1.append("more")
clss1.insert(2,"less")
clss1.pop(-1)

#tuple相当于list，但是一旦定下来就不可以修改
clss2=(1,2)
clss2[1] 
clss3=(1,) #需要一个逗号来消除歧义，显示时也显示逗号但其实是tuple

clss4=(1,"2",[12,"asd"])
clss4[2][1]=213
clss4 #但tuple中的列表元素可以变化

ageinput=input("你的年龄:")
age= int(ageinput)
if age<12:
    print(12)
elif age>12:
    print(13)
else:
    print(14)
   

sum1=0
for t in range(5):
    sum1 += t
    print(sum1)
    
sum2 = 0
n = 2
while sum2 < 7:
    if sum2 == 6:
        break
    sum2 += n
    if sum2 == 2:
        continue #跳过接下来的程序，直接开始下个循环
    print(sum2)

#dict    
temp = {"a" : 2 , "bb" : 3 }
temp['bb']
'c' in temp
temp.get("a")
temp.get('c') #返回None
temp.get('c',-2) #或者自己确定返回什么
temp.pop("bb") 
#dict与list相比插入速度快，但是内存消耗大

#set
tep = ({1,2,"a","b",1,'a'}) #不会有重复值
tep.add(3) #无序添加
tep & set({1,2,"ab"}) #并集
tep | set({1,2,"ab"}) #交集
