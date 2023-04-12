
x = 0
y = 0

print("Write exit for calculation average")
while True:
    score = input("Please enter your score:")
    if score == "exit":
        break

    else:
        x = float(score) + x 
        y = y + 1

print("Average score is :",x / y) 
