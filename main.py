import string
import random

ENCRYPTED_CHARACTERS = list(string.punctuation + string.digits + string.ascii_uppercase + string.ascii_lowercase + string.whitespace)
DECRYPTED_CHARACTERS = ENCRYPTED_CHARACTERS.copy()

random.shuffle(DECRYPTED_CHARACTERS)

def main():
    while True:
        prompt = input("Would you like to encrypt or decrypt a message (e/d/q)? ").lower()
        if prompt != "e" and prompt != "d" and prompt != "q":
            print("ERROR! Please type, 'e' or a 'd'.")
            continue

        if prompt == "e":

            message = input("Enter a message to be encrypted: ")
            encrypted_message = ""
            for x in message:
                encrypted_message += DECRYPTED_CHARACTERS[ENCRYPTED_CHARACTERS.index(x)]

            print(encrypted_message)

        elif prompt == "d":
            message = input("Enter a message to be decrypted: ")
            decrypted_message = ""
            for x in message:
                decrypted_message += ENCRYPTED_CHARACTERS[DECRYPTED_CHARACTERS.index(x)]

            print(decrypted_message)

        else:
            print("Thanks for using this program!")
            exit()



if __name__ == "__main__":
    main()