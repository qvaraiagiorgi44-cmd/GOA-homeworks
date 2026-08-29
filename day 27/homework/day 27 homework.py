# 1)

# კომენტარებით ახსენით რას აკეთებს თითოეული:


# name = "Giorgi"

# print(name[0:3])
# print(name[2:])
# print(name[:4])
# print(name[-1])


# რას აკეთებს პირველი ინდექსი სლაისინგის ფრჩხილებში - []
# რას აკეთებს მეორე მნიშვნელობა
# როგორ მუშაობს უარყოფითი ინდექსი

# ---

# 2)

# შექმენით სია, სადაც შეინახავთ 7 ქალაქს:

# მაგალითად:

# cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Gori", "Zugdidi", "Poti"]

# დაპრინტეთ:
# მე-3 ელემენტიდან მე-6 ელემენტის ჩათვლით ქალაქები

# ---

# 3)

# მომხმარებელს შემოატანინეთ სახელი, შემდეგ კი დაბეჭდეთ: პირველი 2 ასოს გარეშე დარჩენილი სახელი

# მაგ.
# Input: Jemali
# Output: mali

# ---

# 4)

# მომხმარებელს შემოატანინეთ სახელი.

# თუ სახელი მთავრდება "ა" ასოზე: დაბეჭდეთ ამ ბოლო ასოს გარეშე

# სხვა შემთხვევაში: პირველი ასოს გარეშე

# ---

# 5)

# მომხმარებელს შემოატანინეთ პაროლი.

# თუ პაროლის პირველი ასო არის "A": დაბეჭდეთ: Correct

# სხვა შემთხვევაში: Wrong

# ---

# 6)

# შექმენით რიცხვების სია:

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# თქვენი დავალებაა, რომ დაპრინტოთ სიის ეს ნაჭერი სლაისინგის გამოყენებით:
# [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


# print(name[0:3]) - gamoitans gio
# print(name[2:]) - gamoitans orgi
# print(name[:4]) - gior
# print(name[-1]) - i
# pirveli indexi slaisis frcxilebsi gansazgvravs tu saidan daiwyos slaisingi
# meore mnisvnelobas gamoaqvs meoredan bolomde yvela aso
# uaryofiti indeqsi aris indeqsi romelic iwereba - it

cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Gori", "Zugdidi", "Poti"]
print(cities[3:6])

name = input("enter your name")
print (name[3:])

name2 = input("enter your name")
if name2[-1] == "a":
    print (name2[:-1])
else:
    print(name[1:])

password = input("enter your name")
if password[0] == "1":
    print("correct")
else:
    print("wrong")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers[3:15])