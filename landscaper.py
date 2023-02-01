############ LANDSCAPER Game ##############




game = {
    "tool": 0,
    "money": 0
}

tools = [
    {"name": "Teeth", "profit": 1 , "price": 0 },
    {"name": "Rusty Scissors", "profit": 5 , "price": 5 }
]

def mow_lawn():
    tool=tools[game["tool"]]
    print(f"Mowing the lawn with {tool['name']} for {tool['profit']}")
    game["money"] += tool["profit"]
    
def check_stats():
    print(f"You have {game['money']} $ ")


while(True):
    user_choice = input("[1] Mow Lawn [2] Check stats [Q] Quit Game")
    
    if(user_choice == "1"):
        mow_lawn()
        
    if(user_choice == "2"):
        check_stats()
    
    if(user_choice == "Q"):
        break