import random

print("🎮 Number Guessing Game!")
print("=" * 40)

secret_number = random.randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100...")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("📈 Too LOW! Try higher.")
        elif guess > secret_number:
            print("📉 Too HIGH! Try lower.")
        else:
            print(f"\n🎉 CORRECT! The number was {secret_number}!")
            print(f"🏆 You won in {attempts} attempts!")
            break
            
    except ValueError:
        print("❌ Please enter a valid number!")

print("\nThanks for playing! 🎮")
