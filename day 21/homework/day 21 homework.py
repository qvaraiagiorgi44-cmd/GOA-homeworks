# 1) კომენტარებით ახსენით რას აკეთებს if და else.

# 2) მომხმარებელს შემოატანინეთ ასაკი და ამის მიხედვით დაბეჭდეთ ეს:
#   თუ ასაკი არის 18-ზე ნაკლები მაშინ დაპრინტე "შენ ხარ ... წლის და ხარ არასრულწლოვანი"
#   სხვა შემთხვევაში დაპრინტე "შენ ხარ ... წლის და ხარ სრულწლოვანი"

# 3) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ შეამოწმეთ: 
#   თუ რიცხვი იქნება ლუწი დაპრინტეთ "... არის ლუწი",
#   სხვა შემთხვევაში დაპრინტეთ "... არის კენტი".


# if amowmebs pirobas tu piroba aris swori asrulebs misqvemot daweril kods else musaobs rodesac if arasworia

age = int(input("enter your age " ))
if age < 18:
    print("you are " + str(age) + " years old and you are underage" )
else:
    print("you are " + str(age) + " years old and you ar an adult ")

number = int(input("enter a number:"))
if number % 2 == 0:
    print("ricxvi " + str(number) + " aris luwi")
else:
    print("ricxvi " + str(number) + " aris kenti")
