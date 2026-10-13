mylist=[1,2,5,7,8]
# squaredlist=[]
# for item in mylist:
#     squaredlist.append(item*item)

# print(squaredlist)

# we can achieve the same result using list comprehension in a more easy way
squaredlist = [item * item for item in mylist]
print(squaredlist)
