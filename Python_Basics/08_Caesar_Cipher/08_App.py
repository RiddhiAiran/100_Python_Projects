alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
import art
print(art.logo)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    if encode_or_decode == 'decode':
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f'Here is the {encode_or_decode} Result : {output_text}')

should_continue = True

while should_continue:
    code = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    message = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    caesar(original_text=message,shift_amount=shift,encode_or_decode=code)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == 'no':
        should_continue = False
        print("Okay! Good Bye")