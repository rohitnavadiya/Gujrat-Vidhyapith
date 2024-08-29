birthDates = {'ramesh':'10/02/05','keval':'06/12/03','hiten':'25/08/03','bhargav':'01/01/01','jayesh':'12/12/12'}

months = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}

print("*********************************************************************")
for name,date in birthDates.items():
    # print(name,date)
    getMonth = date.split('/')

    if getMonth[1] in months:
        print(name,":",months.get(getMonth[1]))
    
print("*********************************************************************")

