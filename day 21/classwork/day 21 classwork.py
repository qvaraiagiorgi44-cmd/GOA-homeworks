# 1) მომხმარებელს შემოატანინეთ ასაკი და რიცხვი, თუ მათი ასაკი არის 20ზე მეტი და არჩეული რიცხვი არის ლუწი გამოიტანეთ "Cong
age = int(input("enter your age"))
number = int(input("enter the number"))
if age > 20 and number % 2 == 0:
    print ("congrats!")
else:
    print("try again")