a=5.3
t=type(a)
print(t)

a="67"
t=type(a)
print(t) #Note: anything inside quotes("...") is considered as string but without quotes it is a integer
#So here a is string not integer


a="41.2"
b=float(a)
t=type(b)
print(t) #Here a is string but we converted it to float using float() function and assigned it to b
#Now b is float not string

#For more understanding see in note copy.

