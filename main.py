import random
import string
import time

print(""" ______                                     _                                                       
(_____ \                                   | |                                      _               
 _____) )___  ___  ___ _ _ _  ___   ____ _ | |    ____  ____ ____   ____  ____ ____| |_  ___   ____ 
|  ____/ _  |/___)/___) | | |/ _ \ / ___) || |   / _  |/ _  )  _ \ / _  )/ ___) _  |  _)/ _ \ / ___)
| |   ( ( | |___ |___ | | | | |_| | |  ( (_| |  ( ( | ( (/ /| | | ( (/ /| |  ( ( | | |_| |_| | |    
|_|    \_||_(___/(___/ \____|\___/|_|   \____|   \_|| |\____)_| |_|\____)_|   \_||_|\___)___/|_|    
                                                (_____|                                             """)
print("github.com/saow")

time.sleep(2)
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all_characters = lower + upper + num + symbols

length = 16

while True:
    password = "".join(random.sample(all_characters, length))
    print("")
    print(password)
    more = input("Press Enter to generate more passwords or press ctrl + c to exit.")
    print("")
    if more == "":
        continue
    else:
        break
