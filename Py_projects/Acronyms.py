user_input = str(input("Enter a phrase :"))
text = user_input.split()

Acr=""

for i in text:
    Acr = Acr + (i[0]).upper()

print(Acr)    