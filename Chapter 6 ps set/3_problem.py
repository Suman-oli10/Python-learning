# This program checks if a comment is a scam or not based on certain keywords.

a=input("Enter comment:")
if("Make a lot of money" in a or "Subscribe" in a or "Buy now" in a):
    print("This is a scam")
else:
    print("This is not a scam")


    #or we can write this prgram in different way:

    p1="Subscribe"
    p2="Buy now"
    p3="Make a lot of money"

    a=input("Enter comment:")
    if(p1 in a or p2 in a or p3 in a):
        print("This is a scam")
    else:
        print("This is not a scam")