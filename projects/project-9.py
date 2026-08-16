# 🧩 Task: Student Eligibility Checker
# Write a Python program that decides whether a student is eligible for a scholarship
#  based on these rules:

# The student must have marks ≥ 80 AND attendance ≥ 75%.

# OR, if the student has marks ≥ 90, they are eligible regardless of attendance.

# BUT, if the student has any disciplinary warning, they are not eligible
#  (even if other conditions are true).
percent=int(input(" PLEASE ENTER YOUR PERCENTAGE MARKS::-   "))
attain=int(input("  ENTER YOUR ATTENDENCE PERCENTAGE::-      "))
warn=input("TELL US IF YOU ARE GIVEN ANY DISCIPLINARY WARNING::(YES/NO)::-  ").upper()
if warn=="YES":
    print("SORRY, TO SAY TAHT YOU ARE NOT ELIGIBLE TO AVAIL THE SCHOLARSHIP PROGARM\nONCE AGAIN SORRY")
else:    
   if percent>=90:
       print("YOU ARE ELIGIBLE TO AVAIL THE SCHOLORSHIP PROGRAM\n          CONGRATULATIONS")
   elif percent>=80 and attain>=75:
       print("YOU ARE ELIGIBLE TO AVAIL THE SCHOLORSHIP PROGRAM\n          CONGRATULATIONS")
   else:
       print("SORRY, TO SAY TAHT YOU ARE NOT ELIGIBLE TO AVAIL THE SCHOLARSHIP PROGARM\nONCE AGAIN SORRY")
       
       
       
     
