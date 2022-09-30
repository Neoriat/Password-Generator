
# passWord Generator


import secrets

import time









def generate(): # Main Function

    
    
    while True:  # User Input loop
        try:
            length = int(input("What Length Your Password Should Be?:"))

        except ValueError:
            print("Please Enter A Number:")
            continue

        characters =  "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@!#$%^&*()_"
        # This Characters Will Be Used To Make A Password 


        password = ""

        result = ""

        for i in range(length): # Generate The Password



            password += secrets.choice(characters)

        result += "".join(password)

        return result

        

finalResult = generate()

print("Generating....")

time.sleep(3) # Just Because It Is Cool

print(f"Your PassWord Is {finalResult}") # Final Result





        

        















    




