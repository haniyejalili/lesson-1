import random
print("Welcome")
while True:
    a=input("press a key:")
    t=random.randint(1,6)
    print("🎲 :",t)
    if t==6:
        print(" Great,press key again ")  
