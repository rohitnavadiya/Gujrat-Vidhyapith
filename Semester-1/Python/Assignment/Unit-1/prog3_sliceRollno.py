#program-3: extracting field and slice roll number
rno = 'CS072024'
sliceDept = rno[0:2]
sliceRno = rno[2:-1]

print("*********************************************************************")
print("After slice Deparment: {}".format(sliceDept))
print("After slice roll no: {}".format(sliceRno))
print("*********************************************************************")