
import random


class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"Your ticket number is {self.trainNo} and you are travelling from {fro} to {to}")

    def getStatus(self):
        print(f"Your ticket for the {self.trainNo} is booked successfully")

    def getfare(self,fro,to):
        print(f"Your ticket fare in {self.trainNo} from {fro} to {to} is Nrs{random.randint(456,6756)}")

t = Train(1895)
t.book("Kathmandu","Mumbai")
t.getStatus()
t.getfare("Kathmandu","Mumbai")
