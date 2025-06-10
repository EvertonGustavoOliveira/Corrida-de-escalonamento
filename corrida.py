import time
import random
import copy
import os

class Processo:
    def __init__(self, nome, tempo_execucao): 
        self.nome = nome
        self.tempo_execucao = tempo_execucao
        self.progresso = 0
        self.completo = False

    def executar(self):
        i = 0
        while i < self.tempo_execucao:
            self.progresso += 1
            printar([self])
            time.sleep(0.40)
            i = i + 1
        self.completo = True

    def executar_round_robin(self):
        if self.completo == False:
            self.progresso += 1
            printar([self])
            time.sleep(0.40)
            if self.progresso >= self.tempo_execucao:
                self.completo = True
                return True 
        return False

def printar(processos):
    os.system('cls' if os.name == 'nt' else 'clear')
    for processo in processos:
        marcacao = ""
        for i in range(processo.tempo_execucao):
            if i < processo.progresso:
                marcacao += " ✅ ​"
            else:
                marcacao += " ➡️ ​"
        print("========================")
        print(f"{processo.nome}: | {marcacao} | {processo.progresso} de {processo.tempo_execucao}")
        print("========================")
        print("")

def corrida_fifo(processos):
    print("\nCorrida FIFO")
    tempo_total_fifo = 0

    inicio = time.time()
    for processo in processos:
        processo.executar()    
    fim = time.time()
    tempo_total_fifo = fim - inicio

    print("////////////////////////////////")
    print(f"Tempo FIFO: {tempo_total_fifo}s")
    print("////////////////////////////////")

    return tempo_total_fifo


def corrida_round_robin(processos, quantum=3):
    print("\nCorrida Round Robin")

    try:
        quantum = int(input("Digite um valor inteiro para o quantum: "))
        if quantum <= 0:
            print("valor para quantum invalido, sera usado o valor padrão 3")
            quantum = 3
    except ValueError:
        print("valor para quantum invalido, sera usado o valor padrão 3")
        quantum = 3
    
    inicio = time.time()
    processos_ativos = processos[:]
    while processos_ativos:
        for processo in processos_ativos[:]:
            for _ in range(quantum):
                if processo.executar_round_robin():
                    processos_ativos.remove(processo)
                    break

    fim = time.time()
    tempo_rr = fim - inicio 

    print("////////////////////////////////")
    print(f"Tempo ROUND ROBIN: {tempo_rr}s")
    print("////////////////////////////////")
    return tempo_rr 

while True:

    nomes_dos_processos = ["Octane", "Fennec", "Dominus", "Breakout"]


    processos = []
    nomes_carros = random.sample(nomes_dos_processos, 4)

    for i in range(4):
        nome = nomes_carros[i]
        tempo = random.randint(3, 5)
        processo = Processo(nome, tempo)
        processos.append(processo)

    op = input("Selecione uma opção: 1 para jogar // 2 para uma breve explicação da historia // 3 para creditos")


    if op == '1':

        print("Bem-vindo ao sistema de apostas de algoritmos de escalonamento")
        print("Você começa com 10 fichas ​🧿​")
        print("Você fará 3 rodadas de aposta por 3 arenas diferentes")
        print("A rodada 1 acontece no lendário Coliseu Utopia, onde tradição e a tecnologia se enfrentam sob os arcos dourados da arena")
        print("A rodada 2 é uma corrida sob o mar nas profundezas do Aquadome")
        print("A rodada 3 ocorre nos neons de Neo Tokyo, onde tecnologia e velocidade colidem em meio a arranha céus futuristas")

        fichas = 10
        rodada = 1

        while rodada <= 3 or fichas == 0:
            print("\nRodada", rodada)
            print("Suas fichas atuais: ​🧿​", fichas)

            print("Em qual algoritmo você quer apostar?")
            print("1 para FIFO")
            print("2 para Round Robin")

            aposta = input("Digite 1 ou 2: ")

            if aposta != '1' and aposta != '2':
                print("Voce precisa digitar 1 ou 2")
                continue

            valor_aposta_input = input("Digite o valor da aposta: ")

            try:
                valor_da_aposta = int(valor_aposta_input)
            except:
                print("Digite um número inteiro")
                continue

            if valor_da_aposta <= 0 or valor_da_aposta > fichas:
                print("Valor de posta inválido")
                print("Suas fichas atuais são: ", fichas)

                continue

            processos_fifo_copia = copy.deepcopy(processos)
            processos_rr_copia = copy.deepcopy(processos)

            
            tempo_fifo = corrida_fifo(processos_fifo_copia)
            tempo_rr = corrida_round_robin(processos_rr_copia)

            if tempo_fifo < tempo_rr:
                vencedor = '1'
                print("FIFO venceu a rodada🚀​🚀​🚀​🚀​")
            elif tempo_rr < tempo_fifo:
                vencedor = '2'
                print("Round Robin venceu a rodada🚀​🚀​🚀​🚀​")
            else:
                print("Empate!")
            if vencedor == aposta:
                fichas = fichas + valor_da_aposta
                print("Você acertou a aposta! Ganhou", valor_da_aposta, "fichas")
            elif vencedor == 'empate':
                print("Empate")
            else:
                fichas = fichas - valor_da_aposta
                print("Você errou a aposta e perdeu", valor_da_aposta, "fichas")

                if fichas <= 0:
                    print("Você perdeu tudo ​🤦‍♂️​")
                    print("Que pena ​🤡​")
                    print("Mais sorte na rpoxima vez ")

                    break

            rodada = rodada + 1

        print("Fim do jogo")
        print("Suas fichas finais são: ", fichas)
        

    elif op == '2':
        print("Em um mundo onde Rocket League se tornou mais do que um jogo, as arenas não são apenas palcos de espetaculos de velocidade, mas de inteligência algorítmica 👨🏼‍💻")
        print("Por tras de cada carro existe uma polituca de escalonamento\n")
        print("Fifo: Executa os processos na ordem em que são inseridos numa fila\n")
        print("Round Robin:  Distribui o tempo de CPU igualmente entre os processos, alternando entre eles em ciclos fixos chamados quantum\n")
        print("Cada corrida é uma batalha silenciosa entre suas estratégias de execução, mas algo ainda mais arriscado do que competir é APOSTAR")
        print("Milhares de jogadores se reúnem em redes subterrâneas de simulação para testar a sua sorte")
        print("Você é um desses desafiantes. Com apenas 10 fichas e 3 rodadas, sua missão é apostar no algoritmo certo e multiplicar sua fortuna ​​ ​📈​​​📈​​​📈 ​ou perder tudo ​​📉​​​📉​​​📉​")
        print("A arena está pronta. Os processos foram definidos. As apostas estão abertas.")
        print("Escolha com sabedoria ou saia zerado")

    elif op == '3':
        print("Everton Gustavo")
    
    else:
        print("Escolha invalida")