alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
        new_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
        for char in start_text:
            if char >= 'a' and char <= 'z':
                position = alphabet.index(char)
                new_position = position + shift_amount
                new_text += alphabet[new_position]
            else: 
                new_text += char
        print(f"The {cipher_direction}d message is {new_text}")

        
continue_typing = True
while continue_typing:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt.")
    text = (input("Type your message.")).lower()
    shift = int(input("How much you want to shift the message?"))
    shift = shift % 26

    caesar(text, shift, direction)

    decision = input("Do you want to continue? Type 'yes' or 'no'")
    if decision == "no":
        continue_typing = False
        print("Goodbye..")

