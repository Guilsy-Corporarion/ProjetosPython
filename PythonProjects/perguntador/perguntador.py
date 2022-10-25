print("")
nome = input("Escreva o seu nome: ")
print("Bem-vindo,",nome,"!")

print("")
jogando = input("Vamos começar? (s/n) ")

if jogando.lower() != "s" or "sim" or "Sim":
    quit()

print("")
print("Ótimo!")
pontos = 0

#PRIMEIRA PERGUNTA
print("")
print('1. Linguagem de Programação')
print('2. Uma cobra')
print('3. Streamer')
print('4. Nenhum destes')
print("")
resposta=int( input('Python é uma (1, 2, 3 or 4): ') )
print("")

if (resposta==1):
    print("")
    print('Correto!')
    print("")
    pontos += 1
else:
    print("")
    print('Incorreto!')
    print("")
    
#SEGUNDA PERGUNTA
anwer = input("HTML é uma linguagem de progamação? (s/n) ")
if anwer.lower() == "n" or "nao" or "Nao" or "Não":
    print("")
    print("Correto!")
    print("")
    pontos += 1
else:
    print("")
    print("Incorreto!")
    print("")

#TERCEIRA PERGUNTA
print("")
print('1. Um profissional de T.I')
print('2. Uma pessoa que mexe com Python')
print('3. Streamer')
print('4. Nenhum destes')
print("")
resposta=int( input('O programador é (1, 2, 3 or 4): ') )
print("")

if (resposta==1):
    print("")
    print('Correto!')
    print("")
    pontos += 1
else:
    print("")
    print('Incorreto!')
    print("")

print("")
print("Você conseguiu " + str(pontos) + " pontos!, Parabéns!")
print("Você alcançõu a média de " + str((pontos / 4 ) * 100) + "%.")
