import random
def display(a):
    if(a==-1):
        print("Status : Draw\n")   
    elif(a==1):
        print("You Win in this move\n")   
    else :
        print("You Loss in this move\n")  
       
def user_score(a,userscore):
      
    if(a==1):
        userscore=userscore+1
    return userscore   
def computer_score(a,computerscore):
    
    if(a==0):
        computerscore=computerscore+1
    return computerscore     
def computer_choice_converter(computer_choice):
    if(computer_choice=="Snake"):
        a=0
    elif(computer_choice=="Water"):
        a=1
    else:
        a=2  
    return a          
def user_choice_converter(user_choice):
    if(user_choice=="Snake"):
        b=0
    elif(user_choice=="Water"):
        b=1
    else:
        b=2
    return b   
                         
result = [
    [-1, 1, 0],
    [0, -1, 1],
    [1, 0, -1]
]
userscore=0   
computerscore=0  
a=0
option = ["Snake", "Water", "Gun"] 
print(":::::::Snake-Water-Game ::::::::\n")
move_number=int(input("Enter the times you Want to play : "))
i=0
while(i<move_number):
    print("Move no : ",i+1)
    user_choice=""
    while(user_choice!="Snake" and user_choice!="Water" and user_choice!="Gun" ):
        user_choice=input("Enter your choice : ")
        if(user_choice!="Snake" and user_choice!="Water" and user_choice!="Gun" ):
            print("Wrong Choice")
        
    computer_choice = random.choice(option)
    print("Computer choice : ",computer_choice)
    gameresult=result[user_choice_converter(user_choice)][computer_choice_converter(computer_choice)]
    display(result[user_choice_converter(user_choice)][computer_choice_converter(computer_choice)])
    userscore=user_score(gameresult,userscore)
    computerscore=computer_score(gameresult,computerscore)
    i+=1
print("---------------------------------")    
print("Your Final Score : ",userscore)
print("Computer Final Score : ",computerscore)
if(userscore>computerscore):
    print("You Win the Game")
elif(userscore==computerscore):
    print("Game Draw")
else:
    print("You Lose the Game")    
