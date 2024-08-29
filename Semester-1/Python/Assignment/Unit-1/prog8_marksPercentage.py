#program-8 input subject marks and if student pass then find percentage
sub1=int(input("Enter subject 1 marks:"))
sub2=int(input("Enter subject 2 marks:"))
sub3=int(input("Enter subject 3 marks:"))
sub4=int(input("Enter subject 4 marks:"))
sub5=int(input("Enter subject 5 marks:"))

if(sub1<40 or sub2<40 or sub3<40 or sub4<40 or sub5<40):
    print("Student is fail...")
else:
    percentage = (sub1+sub2+sub3+sub4+sub5)/5
    print("Student is pass...")
    #print(percentage)
    print("Percentage of student:{}".format(percentage))