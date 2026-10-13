# Write a program to take marks of 3 subjects from the user and calculate the total percentage and print the final result as pass or fail. (pass>=40% and should have minimum 33% in each subject)

marks1=int(input("Enter the marks of science: "))
marks2=int(input("Enter the marks of mathematics: "))
marks3=int(input("Enter the marks of english: "))
Total_percentage =(100*(marks1+marks2+marks3)/300)

if(Total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congratulations! You have passed the examination.",Total_percentage)
else:    
    print("Sorry! You have failed the examination.",Total_percentage)   