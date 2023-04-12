
import random

app_number = random.randint(20,50)
x = 0
while True :
    user_number = int(input())
    x = x + 1
    if app_number == user_number:
        print("🌺awsume-🌺")
        print("✨✨✨✨you win✨✨✨✨")
        print("👌")
        break
    elif app_number > user_number:
        print("❌wrong❌") 
        print("go up") 
        print("👆")
    elif app_number < user_number:
        print("❌wrong❌")
        print("go down")
        print("👇")
print("guess number = " , x)  