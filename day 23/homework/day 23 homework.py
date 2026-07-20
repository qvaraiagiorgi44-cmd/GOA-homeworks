
# if amowmes pirobas tu piroba wesmaritia asrulebs kods
# elif amowmebs sxva pirobas tu if ar sesrulda
# else sruldeba masin rodesac arc if da arc elif ar sesrulda

# if da else - aqvs ori varianti
# if elif else - aqvs sami varianti

age = int(input("შეიყვანე ასაკი: "))

if age >= 0 and age <= 12:
    print("ბავშვი")
elif age >= 13 and age <= 19:
    print("თინეიჯერი")
else:
    print("ზრდასრული")

score = int(input("enter your score: "))
if score >= 90:
    if score <= 100:
        print("A")
elif score >= 80:
    if score <= 89:
        print("B")
elif score >= 70:
    if score <= 79:
        print("C")
elif score >= 60:
    if score <= 69:
        print("D")
else:
    print("F")
