number1=eval(input("enter the first number:"))
number2=eval(input("enter the second number:"))
operator=input("choose an operator (+,-,*,/):")

if operator=='+':
    print(number1+number2)

elif operator=="-":
     print(number1-number2)

elif operator=='*':
      print(number1*number2)

elif operator=='/':
      print(number1/number2)

else:
      print("invalid operator")




      # Build a simple calculator in Python