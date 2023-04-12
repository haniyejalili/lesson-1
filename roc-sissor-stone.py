import random
app_score = 0
user_score = 0

for i in range (6):
    x=random.randint(1,3)
    if x==1:
        app_choice="rock"
    elif x == 2:
        app_choice="paper" 
    elif x == 3: 
        app_choice="scissor" 
    user_choice =input()

    print("💻",app_choice)
    print("🤶 ",user_choice)
    if app_choice =="rock" and user_choice == "paper":
        user_score = user_score + 1
    elif app_choice =="rock" and user_choice == "scissors":
        app_score = app_score + 1
    elif app_choice == "rock" and user_choice == "rock":
        app_score = app_score + 0        
    elif app_choice =="scissors" and user_choice == "rock":
        user_score = user_score + 1
    elif app_choice =="scissors" and user_choice == "paper":
        app_score = app_score + 1
    elif app_choice == "scissors" and user_choice == "scissors":
        app_score = app_score + 0 
    elif app_choice =="paper" and user_choice == "rock":
        app_score = app_score + 1
    elif app_choice =="paper" and user_choice == "scissors":
        user_score = user_score + 1
    elif app_choice == "paper" and user_choice == "paper":
        app_score = app_score + 0   
   

print ("app score is :" , app_score)
print ("User score is :" , user_score)
