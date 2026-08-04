marks = int(input("enter marks:\n"))

if(marks >=0 and marks <=39):
    print("your score is fail!")

elif(marks >=40 and marks <=49):
    print("your score is pass!!")

elif(marks >=50 and marks <=69): 
    print("your score is credit!!!")  

elif(marks >=70 and marks <=100):
    print("your score is distinction!!!!")

else:
    print("invalid mark!!!")       


"""if 0 <= marks <= 39:
    print("Your score is fail!")
elif 40 <= marks <= 49:
    print("Your score is pass!!")
elif 50 <= marks <= 69:
    print("Your score is credit!!!")
elif 70 <= marks <= 100:
    print("Your score is distinction!!!!")
else:
    print("Invalid mark!!!")"""
