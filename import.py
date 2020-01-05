'注释'
__author__ = 'name'

import sys

def _crazy1(tik): #内部函数
    tik += 1
    return tik
def crazy2(tik):
    tik =_crazy1(tik)
    return tik

if __name__=='__main__':
    print(crazy2(23))
    
#sys.path.append()
#不是永久

    
