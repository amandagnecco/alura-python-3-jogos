from random import randint

def jogar():

    print('********************************')
    print('Bem vindo ao jogo de Adivinhação')
    print('********************************')

    numero_secreto = randint(1,100)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual seu nível de dificuldade:")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Escolha o nível de dificuldade: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1, (total_de_tentativas+1)):

        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou ', chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto 
        menor = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos!" .format(pontos))
            break
        else:
            if (maior):
                print("Você errou. O número é maior que o número secreto")
            elif(menor):
                print("Você errou. O número é menor que o numero secreto")
            pontos_perdidos = numero_secreto - chute
            pontos = pontos - pontos_perdidos

    print("O número secreto era {}" .format(numero_secreto))
    print("Fim do jogo")

if __name__ == "__main__":
    jogar()