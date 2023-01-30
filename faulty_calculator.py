"""Design a calculator which will correctly solve all the problems except the following ones:
45 * 3 = 555, 56+9 = 77, 56/6 = 4
Your program should take operator  and the two numbers as input from the user and then return the result"""


num1=int(input("Enter the 1st number:-"))
num2=int(input("Enter the 2nd number:-"))
op=input("Enter + for add\n\t\tor\n- for subtract\n\t\tor\n* for multiplication\n\t\tor\n/ for devision you want to calculete\nEnter your choice:-")

if op=="+":
 if (num1==56 and num2==9) or (num1==9 and num2==56):
  print(num1,"+",num2," = 77")
 else:
  print(num1,"+",num2," = ",num1+num2)
elif op=="-":
 print(num1,"-",num2,"=",num1-num2)
elif op=="*":
 if (num1==45 and num2==3) or (num1==3 and num2==45):
  print(num1,"*",num2,"=555")
 else:
  print(num1,"*",num2,"=",num1*num2)
elif op=="/":
 if (num1==56 and num2==6):
  print(num1,"/",num2,"=4")
 else:
  print(num1,"/",num2,"=",num1/num2)
else:
 print("You Enter wrong input")