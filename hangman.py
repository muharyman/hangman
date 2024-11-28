import random
print("Welcome to Hangman")
print("-----------------------------")

wordDictionary = [
    "sunshine", "butterfly", "mountain", "galaxy", "harmony", "adventure", 
    "umbrella", "rainbow", "whisper", "journey", "puzzle", "balloon", 
    "feather", "treasure", "island", "lantern", "starlight", "echo", 
    "mystery", "miracle", "paradise", "ocean", "glacier", "volcano", 
    "lightning", "forest", "meadow", "garden", "desert", "comet", 
    "sunflower", "castle", "pyramid", "firefly", "twilight", "daydream", 
    "moonlight", "river", "canyon", "harbor", "breeze", "compass", 
    "glimmer", "melody", "serenity", "labyrinth", "sapphire", "twinkle", 
    "seashell", "whirlpool"
]

hiddenWord = random.choice(wordDictionary)

for x in hiddenWord:
    print ("_", end=" ")
print("\n")

hangman_stages = [
    '''
        +---+
            |
            |
            |
           ===
    ''',
    '''
        +---+
        O   |
            |
            |
           ===
    ''',
    '''
        +---+
        O   |
        |   |
            |
           ===
    ''',
    '''
        +---+
        O   |
       /|   |
            |
           ===
    ''',
        '''
        +---+
        O   |
       /|\  |
            |
           ===
    ''',
            '''
        +---+
        O   |
       /|\  |
       /    |
           ===
    ''',
    '''
        +---+
        O   |
       /|\  |
       / \  |
           ===
    ''',
]

def print_hangman(wrong):
    print(hangman_stages[wrong])
    
def print_word(guessed_letters):
    remaining_blanks = 0
    displayed_word = []
    for char in hiddenWord:
        if char in guessed_letters:
            displayed_word.append(char)
        else:
            displayed_word.append("_")
            remaining_blanks += 1
    print(" ".join(displayed_word))
    return remaining_blanks

wrong_guesses = 0
guessed_letters = set()

while wrong_guesses < 6:
    print("\nLetters guessed so far :", " ".join(sorted(guessed_letters)))
    guess = input("Guess a letter:").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    
    guessed_letters.add(guess)
    
    if guess in hiddenWord:
        remaining_blanks = print_word(guessed_letters)
        if remaining_blanks == 0:
            print("\n You won! the word was: ", hiddenWord)
            break
    else:
        wrong_guesses +=1
        print_hangman(wrong_guesses)
        print_word(guessed_letters)

if wrong_guesses == 6:
    print('\n You lost! the word was:', hiddenWord)