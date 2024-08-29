#program-5 check blood group matched or not
bloodGroup = input("Enter blood group:").split()

a = bloodGroup[0]
b = bloodGroup[1]

if(a == b):
    print("*********************************************************************")
    print("Blood group match")
    print("*********************************************************************")
else:
    print("*********************************************************************")
    print("Blood group doesn't match")
    print("*********************************************************************")