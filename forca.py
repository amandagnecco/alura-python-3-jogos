import random

def jogar():

    imprime_abertura()
    palavra_chave = carrega_palavra_chave()

    letras_acertadas = inicializa_letras_acertadas(palavra_chave)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = chute_do_jogador()

        if chute in palavra_chave:
            posiciona_letras_acertadas(chute, letras_acertadas, palavra_chave)

        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_chave)



def imprime_abertura():
    print('********************************')
    print('***Bem vindo ao jogo de Forca***')
    print('********************************')

def carrega_palavra_chave():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_chave = palavras[numero].upper()
    return palavra_chave

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def chute_do_jogador():
    chute = str(input("Digite uma letra: ")).upper().strip()
    return chute

def posiciona_letras_acertadas(chute, letras_acertadas, palavra_chave):
    posicao = 0
    for letra in palavra_chave:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_chave):
    print("x.x Você foi enforcado!")
    print("A palavra era {}".format(palavra_chave))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if __name__ == "__main__":
    jogar()