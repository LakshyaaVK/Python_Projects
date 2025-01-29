import random  

user_score = 0
computer_score = 0
moves = ['stone', 'paper', 'scissors']

while True:
    user_input = input("Enter (stone/paper/scissors) or 'q' to quit: ").lower().strip()
    
    if user_input == "q":
        print("BYE-BYE! Thanks for playing.")
        print(f"Final Score: You {user_score} - {computer_score} Computer")
        break  
    
    if user_input not in moves:
        print("❌ Invalid Move! Please enter 'stone', 'paper', or 'scissors'.")
        continue  
    

    random_number = random.randint(0, 2)
    computer_move = moves[random_number]

    print(f"\nYou picked: {user_input}")
    print(f"Computer picked: {computer_move}")

    if user_input == computer_move:
        print("🤝 It's a tie!")
    elif (user_input == "stone" and computer_move == "scissors") or \
         (user_input == "paper" and computer_move == "stone") or \
         (user_input == "scissors" and computer_move == "paper"):
        print("🎉 You win!")
        user_score += 1
    else:
        print("💻 Computer wins!")
        computer_score += 1

    print(f"Score: You {user_score} - {computer_score} Computer\n")
