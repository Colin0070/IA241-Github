print(1==2)
print(1!=2)
print(1>2)

if 2>1 :
    print("2>1")
    
if 2<1 :
    print("2>1")

#it was false so python didnt run the code

if 2<1 :
    print("2>1")
    print('another 2>1')
    if 3>1:
        print('3>1')
else:
    print('else statement')
    
print('out of if block')
    
#else statement because ation failed, false result

if 2<1 :
    print("2>1")
    print('another 2>1')
    if 3<1:
        print('3>1')
else:
    print('else statement')
    
print('out of if block')

#did not give else statement, conditional test succeded
if 2>1 :
    print("2>1")
    print('another 2>1')
    if 3>1:
        print('3>1')
else:
    print('else statement')
    
print('out of if block')

print('seperation')

if 2>1:
    print('2>1')
    
elif 3>1:
    print('3>1')

print('seperation')

if 2<1:
    print('2>1')
    
elif 3<1:
    print('3>1')
    
else:
    print('else')
    