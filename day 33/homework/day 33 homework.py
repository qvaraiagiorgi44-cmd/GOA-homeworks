# 1)
# function aris kodis bloki romelic segvizlia ramdenjerme gamoviyenot
# def
# argument aris raime funqciashi chawerili informacia
# parameter aris is sadac argument inaxeba
# return gamoiyeneba rom funqciidan monacemi davabrunot da tavidan gamoviyenot
# print - ubralod gamoaqvs terminalze
# return - kods abrunebs ro sxvaganac gamoiyeno
# funqcias vizaxebt magalitad greet(gamarjoba)

# 2)
def findMax(a, b):
    if a > b:
        return a
    else:
        return b
print(findMax(10, 7))

# 3)
def checknumber(number):
    if number % 2 == 0:
        return "luwia"
    else:
        return "kentia"
print(checknumber(5))


# 4)
def checkAge(age):
    if age >= 18:
        return "შეგიძლია შესვლა"
    else:
        return "შესვლა აკრძალულია"
print(checkAge(18))