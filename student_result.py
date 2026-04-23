marks = {}

name = str(input("Enter the name of the student:"))
sub1 = float(input("Enter the marks of subject 1:"))
sub2 = float(input("Enter the marks of subject 2:"))
sub3 = float(input("Enter the marks of subject 3:"))

total =sub1+sub2+sub3
avg = total/3

if avg >= 80:
    print("Grade--> A")
if avg <= 79 and avg >= 60:
    print("Grade--> B")
if avg <=59 and avg >=40:
    print("Grade--> C")
if avg < 40:
    print("Fail")

print(f"Total = {total}\n Average = {avg}\n")

