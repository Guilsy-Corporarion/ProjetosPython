print("")
nome = input("Escreva o seu nome: ")
print("Bem-vindo,",nome,"!")

print("")
jogando = input("Vamos começar? ")

if jogando.lower() != "sim":
    quit()

print("")
print("Ótimo!")
pontos = 0

#PRIMEIRA PERGUNTA
print("")
anwer = input("O que é uma linguagem de programação? ")
if anwer.lower() == "um conjunto de instruções que criam progamas de computador para automatizar tarefas.":
    print("")
    print("Correto!")
    print("")
    pontos += 1
else:
    print("")
    print("incorreto!")
    
#SEGUNDA PERGUNTA
anwer = input("HTML é uma linguagem de progamação? ")
if anwer.lower() == "não":
    print("")
    print("Correto!")
    print("")
else:
    print("")
    print("Incorreto!")
    print("")

#TERCEIRA PERGUNTA
anwer = input("HTML é uma linguagem de progamação? ")
if anwer.lower() == "não":
    print("")
    print("Correto!")
    print("")
else:
    print("")
    print("Incorreto!")
    print("")

#QUARTA PERGUNTA
anwer = input("HTML é uma linguagem de progamação? ")
if anwer.lower() == "não":
    print("")
    print("Correto!")
    print("")
else:
    print("")
    print("Incorreto!")
    print("")
    
#QUINTA PERGUNTA
anwer = input("HTML é uma linguagem de progamação? ")
if anwer.lower() == "não":
    print("")
    print("Correto!")
    print("")
else:
    print("")
    print("Incorreto!")
    print("")

print("")
print("Você conseguiu " + str(pontos) + " pontos!, Parabéns!")
print("Você alcançõu a média de " + str((pontos / 4 ) * 100) + "%.")
