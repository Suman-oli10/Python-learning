#program to print 3rd,5th and 7th element from list using enumerate function:

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index, item in enumerate(my_list):
    if index == 2:
        print("3rd element is:", item)
    elif index == 4:
        print("5th element is:", item)
    elif index == 6:
        print("7th element is:", item)