import random
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
      ''')

words_list = ["cat","camel","elephant","tiger","lion"]

chosen_word = random.choice(words_list)
print(chosen_word)

placeholder = ''
for position in range(len(chosen_word)):
    placeholder += "_"

print(f"Word to Guess : {placeholder}")

lives = 6
correct_letters = []
game_over = False
while not game_over:
    guess = input("Guess a letter : ").lower()
    display =''
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter 
        else:
            display += '_'

    if guess not in correct_letters:
        lives -= 1
        print(f"You Guessed {guess}, Not in the word. You Loose a Life")
    print(f'*****************  {lives}/6 LIVES LEFT  ********************')
    print(display)
    if ('_' not in display) or lives == 0:
        game_over = True