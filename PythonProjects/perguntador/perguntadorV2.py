import time

perguntas = {
    '1-Pergunta': {
        'pergunta': 'Qual é a síndrome que ataca mais pessoas no mundo atualmente?',
        'alternativas': {'a': 'Síndrome do pânico', 'b': 'Síndromes Genéticas', 'c': 'Síndrome do pensamento acelerado'},
        'correta': 'c',
    },
    '2-Pergunta': {
        'pergunta': 'Qual a linguagem de programação com maior ascensão na atualidade?',
        'alternativas': {'a': 'Java', 'b': 'C++', 'c': 'Javascript', 'd': 'Python'},
        'correta': 'd',
    },
    '3-Pergunta': {
        'pergunta': 'Qual nome da IA com capacidade de atuar no âmbito jurídico?',
        'alternativas': {'a': 'ROSS', 'b': 'WATSON', 'c': 'IBM', 'd': 'Amazon'},
        'correta': 'a',
    },
}
resposta_correta, resposta_errada, totalpontos = 0, 0, 0 
print("")
print("")
print("   \033[1;33mBem vindo ao QUIZ sobre conhecimentos gerais\033[m")
print("")
while True:
    print("""
    Instruções antes de começar o jogo:

    Digite: P - para acessar painel de dicas;
    Digite: j - para começar a jogar;
    Digite: S - se quiser sair sem iniciar o jogo;

    """)
    instru = input("Escolha uma das opções acima: ").strip().upper()[0]
    if instru not in 'PJS':
        continue
    if instru in 'P':
        print("""
        Painel de dicas:

            O jogo irá passar questões relacionado a atualidade do mundo e colocará três alternativas para você escolher.
        Caso você acertar uma alternativa você ganhará um ponto para passar de nível, e se perder irá voltar de nível.
        Os temas são: Tecnologia, Psicologia, Direito, Crimes, Política.

        """)
    elif instru in 'J':
        print("O jogo irá começar em... ")
        for i in range(0, 4):
            print(i)
            time.sleep(0.50)
        print("")
        break
    if instru in 'S':
        quit()

print("           QUIZ")
print(" - PERGUNTAS E RESPOSTAS - ")
print("")
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")
    print()
    print("Alternativas:")
    for ak, av in pv['alternativas'].items():
    
        print(f" {ak}) {av}")

    print()
    while True:
        resposta_user = input("Escolha uma alternativa: ").strip()[0]
        if resposta_user in pv['alternativas'].keys():
            break
    if resposta_user == pv['correta']:
        print("")
        print("Parabéns meu caro, você acertou essa questão!")
        print("")
        resposta_correta += 1
        totalpontos += 1
    else:
        print("")
        print("Você errou e perdeu um ponto!")
        print("")
        resposta_errada += 1
        totalpontos -= 1
print("")
print("Computando os resultados...")
time.sleep(2)
print("")
print(f"De {len(perguntas)} Você acertou {resposta_correta} e errou {resposta_errada}")
print("")
print(f"Sua pontuação atual é: {totalpontos}")
print(f"A porcentagem de acertos foi: {resposta_correta / len(perguntas) * 100}%")
print("")