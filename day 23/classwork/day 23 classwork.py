# 1)კომენტარებით ახსენით რას აკეთებს elif

# 2) მომხმარებელს შეაყვანინე რიცხვი:
# თუ რიცხვი მეტია 10-ზე — დაბეჭდე "დიდია";
# თუ ტოლია 10-ის — დაბეჭდე "ზუსტად 10-ია";
# სხვა შემთხვევაში — დაბეჭდე "პატარაა".

# 3) მომხმარებელს შემოაყვანინეთ რიცხვი:
# თუ რიცხვი დადებითია, შეამოწმეთ:
#   თუ არის ეს რიცხვი ლუწი, დაპრინტეთ "დადებითია და არის ლუწი",
#   თუ კენტი იქნება ეს დადებითი რიცხვი "დადებითია და არის კენტი"
# თუ არის უარყოფითი დაპრინტეთ "უარყოფითია".


#elif gamoiyeneba masin rodesac if-is piroba arasworia magram gvinda sxva pirobis semowmeba

number = int(input("enter a number:"))
if number > 10:
    print("didia")
elif number == 10:
    print("zustad atia")
elif number < 10:
    print("pataraa")

number2 = int(input("enter a number:"))
if number2 > 0:
    if number2 % 2 == 0:
        print("dadebitia da aris luwi")
    else:
        print("dadebitia da aris kenti")
else:
    print("uaryofitia")