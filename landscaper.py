############ LANDSCAPER Game ##############
import random

game = {
    "tool": 0,
    "money": 0
}

tools = [
    {"name": "Teeth", "profit": 1 , "price": 0 },
    {"name": "Rusty Scissors", "profit": 5 , "price": 5 },
    {"name": "Push Lawnmower", "profit": 50  , "price": 25 },
    {"name": "Battery-powered Lawnmower", "profit": 100  , "price": 250 },
    {"name": "Team of Starving Students", "profit": 250  , "price": 500 }
]

def mow_lawn():
    tool=tools[game["tool"]]
    print(f"Mowing the lawn with {tool['name']} for {tool['profit']} $")
    game["money"] += tool["profit"]
    
def upgrade():
    next_tool = tools[game["tool"] + 1] 
    # print(next_tool)
    if(game["money"] <= next_tool["price"]):
        print("Not enouth money for buying this tool")
        return 0 
    if(next_tool == None):
        print("There are no more tools available")
    game["money"] -= next_tool["price"]
    game["tool"] += 1
    print(f"You upgrated to {next_tool['name']}")

    
def check_stats():
    print(f"You have {game['money']} $ ")
    
def check_winner():
    if(game["money"] >= 1000 and game["tool"] == 4):
        print("You Win!")
        choice = input("Dy yoy want to play again? [Y] Yes [N] No --- ")
        if(choice == "Y"):
            reset()
        else:
            return True
    elif(game["money"] >= 1000 and game["tool"] < 4):
        print("You FAILED to use all the resources!")
        choice = input("Dy yoy want to play again? [Y] Yes [N] No ---")
        if(choice == "Y"):
            reset()
        else:
            return True
    return False

def reset():
    game["tool"] = 0
    game["money"] = 0
        
## Game Loop        
while(True):
    user_choice = input("[1] Mow Lawn [2] Check stats [3] Upgrade [R] Reset [Q] Quit Game  --- ")
    
    if(user_choice == "1"):
        mow_lawn()
        
    if(user_choice == "2"):
        check_stats()
        
    if(user_choice == "3"):
        upgrade()
        
    if(user_choice == "R"):
        reset()
    
    if(user_choice == "Q"):
        print("Game Over")
        break

    if(check_winner()):
        break
    
    