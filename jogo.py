import time
import random
palavra = ('mesa', 'livro', 'tabule')
palavra_secreta = random.choice(palavra)
letras_escolhidas_pela_pessoa = []
underline1= ["_", "_", "_", "_"]
underline2 = ["_", "_", "_", "_", "_"]
underline3 = ["_", "_", "_", "_", "_", "_"]
tentativas = 6
acertos = 0


print("ta pronto??")
jogar = str(input("Sim ou jamais: ")).strip().upper()

if jogar in 'SIM':

    print("\033[31mPensando em palavra...")
    time.sleep(3)
    print("\033[30mPalavra escolhida com sucesso!")
    print(" A palavra tem {} letras".format(len(palavra_secreta)))
    print("_"*len(palavra_secreta))
else:
    print("༼ಢ_ಢ༽ perdeu!")
    exit()

while True:
    print("Qual letra voce acha que a palavra tem? ")
    letra = str(input("Letra:"))
    letras_escolhidas_pela_pessoa.append(letra)
    print('letras tentadas: {}'.format(letras_escolhidas_pela_pessoa))

    if palavra_secreta == 'mesa':
        if letra in palavra_secreta:
            print("Voce acertou uma letra na {} posição!".format(palavra_secreta.index(letra)))
            underline1[palavra_secreta.index(letra)] = (letra)
            print(underline1)
            acertos += 1
        else:
            print("Voce errou uma letra :( . Tente novamente")
            tentativas -= 1
            print("Agora você tem {} chances".format(tentativas))
            if tentativas <= 0:
                print("_(ಠ_ಠ)_ perdeu")
                break
        if acertos == 4:
            print('(๑´ڡ`๑) voce ganhou 🥳!')
            break

    if palavra_secreta == 'livro':
        if letra in palavra_secreta:
            print("Voce acertou uma letra na {} posição!".format(palavra_secreta.index(letra)))
            underline2[palavra_secreta.index(letra)] = (letra)
            print(underline2)
            acertos += 1
        else:
            print("Voce errou uma letra :( . Tente novamente")
            tentativas -= 1
            print("Agora você tem {} chances".format(tentativas))
            if tentativas <= 0:
                print("囧 perdeu")
                break
        if acertos == 5:
            print('(/◕ヮ◕)/ voce ganhou 🥳!')
            break

    if palavra_secreta == 'tabule':
        if letra in palavra_secreta:
            print("Voce acertou uma letra na {} posição!".format(palavra_secreta.index(letra)))
            underline3[palavra_secreta.index(letra)] = (letra)
            print(underline3)
            acertos += 1
        else:
            print("Voce errou uma letra :( . Tente novamente")
            tentativas -= 1
            print("Agora você tem {} chances".format(tentativas))
        if tentativas <= 0:
            print("(T_T) perdeu")
            break
        if acertos == 6:
            print('(๑˃̵ᴗ˂̵)ﻭ voce ganhou 🎉!')
            break

print("(・へ・) JOGO FINALIZADO")