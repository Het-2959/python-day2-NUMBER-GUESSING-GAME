import random

secret = random.randint(1, 100)

chances = 5

for i in range(chances):
    guess = int(input(f"Guess a number (1-100) | Chances left: {chances - i}: "))

    if guess < secret:
        print("Too low!")

    elif guess > secret:
        print("Too high!")

    else:
        print("🎉 Correct! You win!")
        break
else:
    print(f"😢 Game Over! The number was {secret}")