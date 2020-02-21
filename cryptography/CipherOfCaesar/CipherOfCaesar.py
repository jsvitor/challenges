'''
Here I dedicate to make a version of cipher of Caesar.
This programa will be input a text and transposition value.
By @jszvitor
'''

import sys # biblioteca para funções do sistema - fornecer os comandos do script pelo terminal ou cmd
import string # biblioteca para manipulação de textos - pegaremos o alfabeto


def cipher(message, dir, rot):
    ALPHABET = string.ascii_lowercase
    m = '' # mensagem cifrada
    for caracter in message: # para cada letra no arquivo ele vai executar o bloco de código abaixo
        if caracter in ALPHABET: # se a letra existir no alfabeto ele continua
            caracter_index = ALPHABET.index(caracter) # aqui pegamos a posicao da letra em forma numerica. Também poderia ser o usado o .find() no lugar do .index()
            caracter_index = (caracter_index +(dir*rot)) % 26 # Somamos posicao a rotacao e mod 26 p/ tornar um ciclo em torno do alfabeto
            m += ALPHABET[caracter_index] # concatenamos o resultado na variavel mensagem
        else:
            m += caracter
    return m

def encrypt(message, rot):
    return cipher(message, 1, rot)

def decrypt(message, rot):
    return cipher(message, -1, rot)

def main():
    command = sys.argv[1].lower()
    message = sys.argv[2].lower()
    rot = int(sys.argv[3])

    if command == 'encrypt':
        print(encrypt(message, rot))
    elif command == 'decrypt':
        print(decrypt(message, rot))
    else:
        print(command + ' -> command not found')

if __name__ == '__main__':
    main()