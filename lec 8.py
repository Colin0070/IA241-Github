'''
Function
'''

def cal_plus(input1, input2):
#return input1+input2

    result= input1+input2

    return result

print(cal_plus(1,3))


def cal_abs(a):
    
    if a >0:
        return a
    else:
        return -a
        
#print(cal_abs('0'))


def cal_sigma(m,n):
    result = 0
    for i in range (n, m+1):
         result=result+i
 #n+ n+1 + n+2 .. +m
    return(result)

print(cal_sigma(10,1))

def cal_pi(m,n):
    result=1
    for i in range(n,m+1):
         result = result *i
        
    return(result)

print(cal_pi(10,3))

def cal_f(m):
    if m ==0:
        return 1
    else:
        return m* cal_f(m-1)
print(cal_f(5))

def cal_p(m,n):
    return cal_f(m)/cal_f(m-n)
    
print(cal_p(5,3))