import pandas as pd
import random

questao = random.randint(0,4)

capitais = [["O que é uma Linguagem de Programação?", "Uma Batata", "É um conjunto de instruções para automatizar tarefas", "Arroz", "Molho", "B"],
            ["Quem descobriu o Brasil?", "Ainsten", "Santos Dumont", "Elon Musk", "Pedro Alvares Cabral", "D"],
            ["Qual foi o primiero console inventado?", "Magnavox Odyssey", "Play Station 5", "PSP", "Mega Drive", "A"],
            ["Quantos fusos horários existem na Rússia?", "5", "11", "13", "22", "B"]]

df = pd.DataFrame(capitais, columns=["PERGUNTAS", "Alternativa A", "Alternativa B", "Alternativa C", "Alternativa D", "Alternativas Corretas"])


print(df["PERGUNTAS"][questao])