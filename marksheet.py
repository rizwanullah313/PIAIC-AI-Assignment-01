####################### Mark Sheet ###############################

name = input("Enter Student Name: ")
rollno = int(input("Enter Student Roll Number: "))
Math = float(input("Enter Math Marks of "+name+" : "))
Physics = float(input("Enter Math Marks of "+name+" : "))
Chemisrty = float(input("Enter Math Marks of "+name+" : "))
English = float(input("Enter Math Marks of "+name+" : "))

MathGrade=" "
ph_Grade =" "
chemistry_Grade = " "
englishGrade = " "

if(Math>50):
    MathGrade = "pass"
elif(Math<50):
    MathGrade = "fail"
else:
    "Wrong Input"

if(Physics>50):
    ph_Grade = "pass"
elif (Physics<50):
    ph_Grade = "fail"
else:
    "Wrong Input"

if(Chemisrty>50):
    chemistry_Grade = "pass"
elif(Chemisrty<50):
    chemistry_Grade = "fail" 
else:
    "Wrong Input"

if(English>50):
    englishGrade = "pass"
elif(English<50):
    englishGrade = "fail"
else:
    "Wrong Input"

total = ((Math+Physics+Chemisrty+English)/400)*100

if(MathGrade=="fail" or ph_Grade=="fail" or chemistry_Grade=="fail" or englishGrade=="fail"):
    result = "fail"
else:
    result = "pass"

print("----------------------------------- Mark Sheet ------------------------------")
print("Student Name: "+name)
print("Roll No: "+str(rollno))
print("Subject   "+"Totla Marks "+"  "+"obtained marks"+"  "+"Grade")
print("Math      "+"100         "+"  "+str(Math)+"             "+MathGrade)
print("Physics   "+"100         "+"  "+str(Physics)+"          "+ph_Grade)
print("Chemistry "+"100         "+"  "+str(Chemisrty)+"        "+chemistry_Grade)
print("English   "+"100         "+"  "+str(English)+"          "+englishGrade)
print("##################################################################################")
print("Total     "+"400         "+"  "+str(total)+"%           "+result)
print("##################################################################################")