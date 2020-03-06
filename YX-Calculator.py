import os
os.system ("clear")
###################
while True :
 Num1 = int (input("Enter Num1: "))
    
 Cl = input ("Enter the Calculation: ")
    
 Num2 = int (input("Enter Num2: "))
    
 if (Cl is "+"):
  print (Num1 + Num2)
    
 if (Cl is "-"):
  print (Num1 - Num2)
    
 if (Cl == "x"):
  print (Num1 * Num2)
    
 if (Cl is "/"):
  print (Num1 / Num2)
    
 Restart = input ("Do You Want To restart [Y/N]: ")
    
 if (Restart is "n") :
  print ("Done")
  exit()