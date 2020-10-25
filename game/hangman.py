import random
import string
from words import animals
from words import python
gallows = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

### La siguiente función, pide al usuario que eleija entre los dos temas disposnibles.
### Una vez seleccionado elegirá una palabra aleatoria de la lista correspondiente.
def randomword(x, y):     
    while True:
        theme = input("Choose theme: "+"\x1b[1;30m"+"ANIMALS,   PYTHON ==>")
        if theme == "PYTHON":
            chosens = random.choice(x)
            count_letters= len(chosens)
            break
        elif theme == "ANIMALS":
            chosens = random.choice(y)
            count_letters= len(chosens)
            break
        else: 
            print("WRONG, please choose a valid option ")           
    return chosens.upper()

chosen_word = randomword(python, animals)

### Esta función rellena una lista, con tantos espacios en blancos como tenga la palabra elegida
def hiding():
    hiding_word = []
    for i in range(len(chosen_word)): 
        hiding_word.append("_ ")
    return hiding_word

hide_word = hiding()

progress = []  ### Lista que se rellenará con espacios en blancos, para luego ir incluyendo las letras acertadas
count_letters= len(chosen_word) ### Esto nos ayuda a pintar el número de letras que tiene la palabra oculta
alphabet= list(string.ascii_uppercase)

for i in range(len(chosen_word)): ### Este bucle rellena la lista de progreso con los espacios en blanco correspondientes
    progress.append("_ ")

### La función CHECKING ayudará más adelante a comproabar sí la palabra escrita coincide con la elegida
def checking():
    check_list= [] 
    for char in chosen_word:
        check_list.append(char+" ")
    return check_list

check_word = checking()        

def game():
    used_letters=[]
    mistake = 0 

    while mistake < 7: ### Mantiene el juego activo hasta que tengamos 7 fallos, el programa pinta al ahorcado
        if mistake == 0:
            print(gallows[0])
        elif mistake == 1:
            print(gallows[1])
        elif mistake == 2:
            print(gallows[2])
        elif mistake == 3:
            print(gallows[3])
        elif mistake == 4:
            print(gallows[4])
        elif mistake == 5:
            print(gallows[5])
        elif mistake == 6:
            print(gallows[6])
            break
    
    
        print("".join(progress)) ###Convertimos la lista, en un string, y la pintamos
        print("The word has ",count_letters, "letters")  ### Con esto ayudamos a ver cuantas letras tiene la palabra oculta
        print("Used letters: ", used_letters)  ### Pinta las letras que ya has usado
        letter= input("Choose a uppercase letter:")
        if letter in used_letters:
            print("You have already used this letter")
        if letter not in alphabet:
            print("This character is not allowed")
        else:
            used_letters.append(letter)

            wrong = True  ##Sí la letra está mal
            for i in range(len(chosen_word)):
                if letter == chosen_word[i]:
                    progress[i]= letter + " "
                    wrong = False

            if wrong:
                mistake += 1
            if mistake == 6:
                print("YOU LOSE, The word was: ", chosen_word.upper())

            if check_word == progress:
                print("".join(progress))
                print("YOU WIN!, The word is: ", chosen_word.upper())
                break
game()