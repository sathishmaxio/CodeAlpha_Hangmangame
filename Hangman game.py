import random

def hangman():
    words = ["python", "flower", "cloud", "program", "laptop"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []

    print("🎮 Welcome to Hangman Game!")
    print("Guess the word:")
    print(" ".join(guessed))

    while attempts > 0:
        print(f"\nAttempts left: {attempts}")
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabet letter.")
            continue

        if guess in used_letters:
            print("⚠ You already guessed this letter.")
            continue

        used_letters.append(guess)

        if guess in word:
            print("✔ Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print("❌ Wrong guess!")
            attempts -= 1

        print("Word:", " ".join(guessed))

        if "_" not in guessed:
            print("\n🎉 Congrats! You guessed the word:", word)
            break

    if attempts == 0:
        print("\n💀 Game Over! The word was:", word)

hangman()
