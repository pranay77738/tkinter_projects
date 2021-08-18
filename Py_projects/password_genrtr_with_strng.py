import random
import string as s
def passwrd_genrator(prompt):
    number=None
    while True:
        try:
            number=int(input(prompt))
            if 8<=number<=16:
              return number
            else:
                print("Invalid length try again")

        except ValueError:
            print("Invalid Number try again")

pas=s.ascii_lowercase + s.ascii_uppercase +s.digits +s.punctuation
password = "".join(random.sample(pas,(passwrd_genrator("Enter your password length between 8 to 16 :"))))

print(password)

