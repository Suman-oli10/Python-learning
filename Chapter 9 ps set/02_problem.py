#program to create a number guessing game and store the hiscore in a file(better watch this question in harry notebook)
def game():
    import random
    print("Welcome to the number guessing game!")
    score=random.randint(1,100)
    #fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0

    print(f"Your score is {score}")
    if score>hiscore:
        #write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score
game()