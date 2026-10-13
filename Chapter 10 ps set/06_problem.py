#if we use slf instead of self,whether it affects the program or not:
#Answer: No, it does not affect the program because self is just a convention and we can use any name instead of self.
import random

class Train:

    def __init__(slf,trainNo):
        slf.trainNo = trainNo

    def book(slf,fro,to):
        print(f"Your ticket number is {slf.trainNo} and you are travelling from {fro} to {to}")

    def getStatus(slf):
        print(f"Your ticket for the {slf.trainNo} is booked successfully")

    def getfare(slf,fro,to):
        print(f"Your ticket fare in {slf.trainNo} from {fro} to {to} is Nrs{random.randint(456,6756)}")

t = Train(1895)
t.book("Kathmandu","Mumbai")
t.getStatus()
t.getfare("Kathmandu","Mumbai")
