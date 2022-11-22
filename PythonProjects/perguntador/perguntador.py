import pandas as pd
import random

dados= [["QUESTÃO: O que é uma Linguagem de Programação?", "A) Uma Batata", "B) É um conjunto de instruções para automatizar tarefas", "C) Arroz", "D) Molho", "b"],
        
            ["QUESTÃO: Quem descobriu o Brasil?", "A) Eisntein", "B) Santos Dumont", "C) Elon Musk", "D) Pedro Alvares Cabral", "d"],
            
            ["QUESTÃO: Qual foi o primiero console inventado?", "A) Magnavox Odyssey", "B) Play Station 5", "C) PSP", "D) Mega Drive", "a"],
            
            ["QUESTÃO: Quantos fusos horários existem na Rússia?", "A) 5", "B) 11", "C) 13", "D) 22", "b"],
            
            ["QUESTÃO: Qual império não possui um idioma escrito?", "A) Egípcio", "B) Azteca", "C) Inca", "D) Romano", "c"],
            
            ["QUESTÃO: Qual a capital da Angola?", "A) Kingston", "B) Maputo", "C) Acra", "D) Luanda", "d"],
            
            ["QUESTÃO: Qual é o rio mais longo do mundo?", "A) Rio Nilo", "B) Rio Tietê", "C) Mar Morto", "D) Rio Amazonas", "a"],
            
            ["QUESTÃO: Quantos anos tem as pirâmides do egito?", "A) 1.200", "B) 4.500", "C) 3.200", "D) 2000", "b"],
            
            ["QUESTÃO: Em que ano a Netflix foi criada?", "A) 2001", "B) 2009", "C) 2015", "D) 1977", "d"],
            
            ["QUESTÃO: Quantas ilhas tem as Filipinas?", "A) 7.640", "B) 1.400", "C) 6.440", "D) 4000", "a"],
            
            ["QUESTÃO: Quem fundou Roma?", "A) Augusto", "B) Reia Sílvia", "C) Caio Júlio César", "D) Rõmulo e Remo", "d"],
            
            ["QUESTÃO: Qual país é conhecido como a “terra do sol nascente”?", "A) China", "B) Porto Rico", "C) Japão", "D) Taiwan", "c"],
            
            ["QUESTÃO: Quantas Copas do mundo o Brasil ganhou?", "A) 5", "B) 4", "C) 6", "D) 3", "a"],
            
            ["QUESTÃO: Qual  foi o ano da última Copa do Mundo do Brasil?", "A) 1994", "B) 1998", "C) 2006", "D) 2002", "d"],
            
            ["QUESTÃO: Qual país não faz parte da África?", "A) Gana", "B) Nepal", "C) Nigéria", "D) Etiópia", "b"],
            
            ["QUESTÃO: Qual é a população atual da Cidade do Vaticano?", "A) 801", "B) 825", "C) 1.801", "D)1,825", "a"],
            
            ["QUESTÃO: Qual o nome do deus da guerra?", "A) Kratos", "B) Ades", "C) Ares", "D) Perseu", "c"],
            
            ["QUESTÃO: Quantos estados fazem parte dos Estados Unidos?", "A) 47", "B) 53", "C) 32", "D 50", "d"],
            
            ["QUESTÃO: Como se chama a camada mais quente da Terra?", "A) Núcleo interno", "B) Núcleo terrestre", "C) Núcleo externo", "D) Crosta terrestre", "b"],
            ]

df = pd.DataFrame(dados, columns=["PERGUNTAS", "Alternativa A", "Alternativa B", "Alternativa C", "Alternativa D", "Alternativas Corretas"])


# Ínicio.

print("")
print("    BEM VINDO AO QUIZ!")
print("")
nome = input("Escreva o seu nome: ")
print("")
print("Bem-vindo, ",nome,"!")

print("")
jogando = input("Vamos começar? (s/n)  \n")

if jogando.lower() != "s":
    quit()

pontos = 0

n=0

while(n <18):
    
    questao = random.randint(0,18) 
    new_question = random.randint(0,18)
  
    if questao == new_question:
        questao = random.randint(0,18)
    else:
        questao = new_question
        
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
        print('CORRETO!')
        print("")
        pontos += 1
    else:
        print("")
        print('INCORRETO!')
        print("")
    n=n+1 

# Fim.
print("")
print("Você conseguiu " + str(pontos) + " pontos!, Parabéns!")
print("Você alcançõu a média de " + str((pontos / 19 ) * 100) + "%.")
print("")