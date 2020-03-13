import random

SPECIAL_CHARS = " ,.-;:_?!="

ALPHABET = "abcdefghijklmnopqrstuvwxyz.,!' " # Note the space at the end, which I kept missing.
# You could generate the key below using makeKey (i.e. key=makeKey(ALPHABET))
#key = makeKey(ALPHABET)
plaintext = "kkkkkkkkkk hhhhhh jjjj uu"
# v! zmhvxdmxdmo!nll mikbg


def makeKey(ALPHABET):
   ALPHABET = list(ALPHABET)
   random.shuffle(ALPHABET)
   return ''.join(ALPHABET)

def encrypt(plaintext, key, ALPHABET):
    keyIndices = [ALPHABET.index(k.lower()) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def decrypt(cipher_text, key, ALPHABET):
    distribution_dict = analyse_letter_distribution(cipher_text)

    keyIndices = [key.index(k) for k in cipher_text]
    return ''.join(ALPHABET[keyIndex] for keyIndex in keyIndices)

def analyse_letter_distribution(cipher_text):
    distribution_dict = {}
    for letter in cipher_text:
        if letter in SPECIAL_CHARS:
            continue
        if letter not in distribution_dict:
            distribution_dict[letter] = 1
        else:
            distribution_dict[letter] += 1
    return sorted(distribution_dict,key=distribution_dict.get, reverse=True)

key = makeKey(ALPHABET)
cipher_text = encrypt(plaintext, key, ALPHABET)

if __name__ == "__main__":
    print(analyse_letter_distribution(cipher_text))
    print("PLAIN TEXT: " + plaintext)
    print("-------KEY: " + key)
    print("-ENCRYPTED: " + cipher_text)
    print("-DECRYPTED: " + decrypt(cipher_text, key, ALPHABET))