try:
    Name = "Abbas Tinwala"
    print(Name)

    value = 10/0
except ZeroDivisionError:
    print("You cannot devide number by 0")
except:
    print("Exception caught")
finally:
    print("Thank you for using our application")