def user_input(prompt):
    while True:
        try:
            number=int(input(prompt))
            if number >0:
              return number
        except ValueError:
            print("Invalid number entered please try again")

weight = user_input("Enter your weight in Kilograms :")
height = user_input("Enter your height in centimeters :")


height = height/100

BMI = weight/(height*height)

if BMI > 0:
    if BMI<=16.5:
        print("you are severely under weight")
    elif BMI<=18.5:
        print("you are under weight")
    elif BMI<=25:
        print("you are healthy")
    elif BMI<=30:
        print("you are over weight")
    else:
        print("you are severely over weight")
else:
    print("Invalid details")
