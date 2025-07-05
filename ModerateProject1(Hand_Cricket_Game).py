import random

# Function to simulate the toss
def toss_phase():
    print("Welcome to Hand Cricket!")
    
    while True:
        choice = input("Choose Odd or Even: ").strip().lower()
        if choice in ["odd", "even"]:
            break
        print("Invalid input! Please enter 'Odd' or 'Even'.")

    while True:
        try:
            player_a_choice = int(input("You (Player A), choose a number between 1 and 6: ").strip())
            if 1 <= player_a_choice <= 6:
                break
            else:
                print("Invalid input! Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")

    computer_choice = random.randint(1, 6)
    print(f"The computer chose: {computer_choice}")

    # Check if the sum is even or odd
    sum_choices = player_a_choice + computer_choice
    if (choice == "even" and sum_choices % 2 == 0) or (choice == "odd" and sum_choices % 2 != 0):
        print("You win the toss!")
        while True:
            bat_or_bowl = input("Do you want to Bat or Bowl? (Enter 'bat' or 'bowl'): ").strip().lower()
            if bat_or_bowl in ["bat", "bowl"]:
                return bat_or_bowl  # Player chooses batting or bowling
            print("Invalid input! Please enter 'bat' or 'bowl'.")
    else:
        print("Computer wins the toss!")
        print("Computer chooses to Bat.")
        return "bat"  # Computer automatically chooses to bat

# Function for batting phase
def batting_phase(player_name, opponent_name, target=None):
    player_score = 0

    while True:
        while True:
            try:
                player_move = int(input(f"{player_name}, choose a number between 1 and 6: ").strip())
                if 1 <= player_move <= 6:
                    break
                else:
                    print("Invalid input! Please enter a number between 1 and 6.")
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 6.")

        opponent_move = random.randint(1, 6)
        print(f"{opponent_name} chose: {opponent_move}")

        if player_move == opponent_move:
            print(f"{player_name} is OUT! Final score: {player_score}")
            return player_score  # Return score when player is out

        player_score += player_move
        print(f"{player_name}'s current score: {player_score}")

        # If chasing and surpasses target, end the game
        if target is not None and player_score > target:
            print(f"{player_name} has successfully chased the target!")
            return player_score

# Main game function
def play_game():
    user_choice = toss_phase()  # Player chooses to bat or bowl

    if user_choice == "bat":  # Player bats first
        player_a_score = batting_phase("You (Player A)", "Computer")
        print(f"\nYour final score: {player_a_score}")

        print("\nNow it's the computer's turn to bat.")
        computer_score = batting_phase("Computer", "You (Player A)", target=player_a_score)
        print(f"\nComputer's final score: {computer_score}")

    else:  # Computer bats first
        computer_score = batting_phase("Computer", "You (Player A)")
        print(f"\nComputer's final score: {computer_score}")

        print("\nNow it's your turn to bat.")
        player_a_score = batting_phase("You (Player A)", "Computer", target=computer_score)
        print(f"\nYour final score: {player_a_score}")

    # Display final results
    print("\n--- Final Scores ---")
    print(f"Your Score: {player_a_score}")
    print(f"Computer's Score: {computer_score}")

    if player_a_score > computer_score:
        print("🎉 You win!")
    elif player_a_score < computer_score:
        print("😔 Computer wins!")
    else:
        print("🤝 It's a draw!")


play_game()