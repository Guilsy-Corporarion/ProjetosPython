import pandas as pd
import random

dados= [["Questão: O que é uma Linguagem de Programação?", "A) Uma Batata", "B) É um conjunto de instruções para automatizar tarefas", "C) Arroz", "D) Molho", "b"],
            ["Questão: Quem descobriu o Brasil?", "A) Eisntein", "B) Santos Dumont", "C) Elon Musk", "D) Pedro Alvares Cabral", "d"],
            ["Questão: Qual foi o primiero console inventado?", "A) Magnavox Odyssey", "B) Play Station 5", "C) PSP", "D) Mega Drive", "a"],
            ["Questão:Quantos fusos horários existem na Rússia?", "A) 5", "B) 11", "C) 13", "D) 22", "b"]]

df = pd.DataFrame(dados, columns=["PERGUNTAS", "Alternativa A", "Alternativa B", "Alternativa C", "Alternativa D", "Alternativas Corretas"])


# Ínicio.

print("")
print("")
nome = input("Escreva o seu nome: ")
print("")
print("Bem-vindo,",nome,"!")

print("")
jogando = input("Vamos começar? (s/n)  \n")

if jogando.lower() != "s":
    quit()

pontos = 0

n=0

while(n <4):
    questao = random.randint(0,4)
    print("")
    print("")
    print(df["PERGUNTAS"][questao])
    print("")
    print(df["Alternativa A"][questao])
    print(df["Alternativa B"][questao])
    print(df["Alternativa C"][questao])
    print(df["Alternativa D"][questao])
    print("")
    resposta=input('Escolha uma alternativa: (A, B, C or D) \n')
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

# Fim.
print("")
print("Você conseguiu " + str(pontos) + " pontos!, Parabéns!")
print("Você alcançõu a média de " + str((pontos / 4 ) * 100) + "%.")
print("")