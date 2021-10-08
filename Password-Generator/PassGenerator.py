import random

def GeneratePassword(Pass,length):
    password = "".join(random.sample(Pass, length))
    print("Generated Password Is : ", password)

lwr_chars = "abcdefghijklmnopqrstuvwxyz"
upr_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
special_chars= "&@!$*_#"

# pattern for password 
pattern = lwr_chars + special_chars + num + upr_chars      

# Ternary operator to fix length of the password, based on user's input

strength = input(" Enter The Strength Of The Password Required - ( Weak | Strong | Very Strong) : ").lower()

if (strength == "weak" or strength == "strong" or strength == "very strong"):
    length = 6 if (strength == "weak") else 12 if (strength =="strong") else 18
    GeneratePassword(pattern,length)

else : print("Please Enter Valid Input( Weak | Strong | Very Strong)")
