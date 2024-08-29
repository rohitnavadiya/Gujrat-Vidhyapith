#6 find the student from roll number may be in capital or small letter

student = input("Enter your Roll no:")

if(student[0]=='c' or student[0]=='C' and student[1]=='s' or student[1]=='S'):
    print("*********************************************************************")
    print("This is Computer Science student")
    print("*********************************************************************")
else:
    print("*********************************************************************")
    print("This is not Computer Science student")
    print("*********************************************************************")