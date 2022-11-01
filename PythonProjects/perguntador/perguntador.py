#ÍNICIO

nome = input("Escreva o seu nome: ")
print("")
print("Bem-vindo,",nome,"!")

print("")
jogando = input("Vamos começar? (s/n)  \n")

if jogando.lower() != "s":
    quit()

print("")
print("| ÓTIMO! |")
print("")
pontos = 0


#PRIMEIRA PERGUNTA
print("")
print("| PRIMEIRA PERGUNTA |")
print("")
print("PYTHON É UMA: \n")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print('1. Linguagem de Programação')
print('2. Uma cobra')
print('3. Streamer')
print('4. Nenhum destes')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("")
resposta=int( input('PYTHON É UMA: (1, 2, 3 or 4) \n'))
print("")

if (resposta==1) or (resposta==2):
    print("")
    print('Correto!')
    print("")
    pontos += 1
else:
    print("")
    print('Incorreto!')
    print("")
    

#SEGUNDA PERGUNTA


print("")
print("| SEGUNDA PERGUNTA |")
print("")
anwer = input("HTML é uma linguagem de progamação? (s/n) \n")
if anwer.lower() == "n":
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
print("| TERCEIRA PERGUNTA |")
print("")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print('1. Um profissional de T.I')
print('2. Uma pessoa que mexe com Python')
print('3. Um Nerd')
print('4. Nenhum destes')
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("")
resposta=int( input('O PROGRAMADOR É: (1, 2, 3 or 4) \n') )
print("")

if (resposta==1):
    print("")
    print('Correto! (+1 PONTO)')
    print("")
    pontos += 1
else:
    print("")
    print('Incorreto! (-1 PONTO)')
    print("")
    pontos -= 1


#FINAL


print("")
print("Você conseguiu " + str(pontos) + " pontos!, Parabéns!")
print("Você alcançõu a média de " + str((pontos / 4 ) * 100) + "%.")
print("")