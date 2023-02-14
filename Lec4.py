'''
lec4
dict and tuple
'''
my_tuple=('a','b','c','d','e')

#cannot reasign tuple values, tuple has a comma, if no comma its a string  my_tuple[0]='f'
print(my_tuple)

my_car = { 
'color': 'red',
'maker':'toyota',
'year': 2015
         }
print(my_car)

print(my_car['year'])

print(my_car.items())

print(my_car.get('color'))
print(my_car['color'])

my_car['model']= 'venza'
print(my_car)

my_car['year']=2020
print(my_car)

print( len(my_car))

print( 'color' in my_car)

print('red' in my_car.values())