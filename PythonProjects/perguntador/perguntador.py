import pandas as pd
import random

dados= [["O que é uma Linguagem de Programação?", "Uma Batata", "É um conjunto de instruções para automatizar tarefas", "Arroz", "Molho", "B"],
            ["Quem descobriu o Brasil?", "Ainsten", "Santos Dumont", "Elon Musk", "Pedro Alvares Cabral", "D"],
            ["Qual foi o primiero console inventado?", "Magnavox Odyssey", "Play Station 5", "PSP", "Mega Drive", "A"],
            ["Quantos fusos horários existem na Rússia?", "5", "11", "13", "22", "B"]]

df = pd.DataFrame(dados, columns=["PERGUNTAS", "Alternativa A", "Alternativa B", "Alternativa C", "Alternativa D", "Alternativas Corretas"])


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

n=0

while(n <4):
    questao = random.randint(0,4)
    print("")
    #print("| PRIMEIRA PERGUNTA |")
    print("")
    print(df["PERGUNTAS"][questao])
    print(df["Alternativa A"][questao])
    print(df["Alternativa B"][questao])
    print(df["Alternativa C"][questao])
    print(df["Alternativa D"][questao])
    print("")
    resposta=input('PYTHON É UMA: (A, B, C or D) \n')
    resposta.upper()
    print("")

    if (resposta==df["Alternativas Corretas"][questao]):
        print("")
        print('Correto!')
        print("")
        pontos += 1
    else:
        print("")
        print('Incorreto!')
        print("")
    n=n+1
    
#FINAL


print("")
print("Você conseguiu " + str(pontos) + " pontos!, Parabéns!")
print("Você alcançõu a média de " + str((pontos / 4 ) * 100) + "%.")
print("")