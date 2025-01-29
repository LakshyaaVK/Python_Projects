import random

print("🎯 Welcome to the Guess the Number Game! 🎯")

# Set the range for the number
low = 1
high = 100
secret_number = random.randint(low, high)  # Generate a random number
attempts = 0

print(f"\nI've picked a number between {low} and {high}. Can you guess it?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))  # Get user input
        
        if guess < low or guess > high:
            print(f"⚠️ Please enter a number between {low} and {high}!")
            continue

        attempts += 1  # Increment attempts

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts. 🎉")
            break  # Exit loop when guessed correctly

    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")

print("\nThanks for playing! 🎮")
