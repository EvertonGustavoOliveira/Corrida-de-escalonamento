# Corrida-de-escalonamento

Este é um jogo interativo de apostas que une o universo de Rocket League com conceitos de escalonamento de processos. Sua missão é simples: com 10 fichas iniciais, aposte em qual algoritmo será mais eficiente em 3 rodadas, cada uma ocorrendo em uma arena diferente. Use sua intuição, conhecimento e um pouco de sorte para sair vitorioso!

-----------------------------------------------------

## Como Rodar o Jogo

### Pré-requisitos
- Python 3 instalado em sua máquina e um terminal ou prompt de comando

### Rodando o jogo
1. Baixe o arquivo `.py` contendo o código.
2. No terminal, navegue até o diretório onde o arquivo está salvo.
3. Execute com o comando:

```bash
python corrida.py
```

-----------------------------------------------------

##  Como Funciona o Jogo

Ao iniciar o programa, você ira aparecer um menu com 3 opções:

```
1 - Jogar
2 - Breve explicação da história
3 - Créditos
```

### Se escolher "1 - Jogar":
- Você começará com 10 fichas.
- E Terá 3 rodadas de apostas em arenas temáticas:
  - Coliseu Utopia (clássico)
  - Aquadome (subaquático)
  - Neo Tokyo (futurista)
- Em cada rodada, você apostará fichas no algoritmo que acredita que será mais rápido.
- Os algoritmos simularão a execução de processos com tempos variáveis.
- Se acertar, voce ganha fichas. Mas se errar, perde.

-----------------------------------------------------

## Algoritmos de Escalonamento Implementados

### FIFO (First-In, First-Out)
Executa os processos na ordem em que chegam e cada processo é executado por completo antes do próximo. É simples, mas pode causar ineficiências com processos muioto longos.

### Round Robin
Distribui o tempo de CPU igualmente entre os processos de maneira alternada entre eles em ciclos fixos chamados quantum. É um bom algoritmo para sistemas que priorizam a igualdade.

-----------------------------------------------------

## Informações Técnicas do jogo

- Cada processo recebe o nome de um carro aleatório do Rocket League: `Octane`, `Fennec`, `Dominus`, `Breakout`.
- Os tempos de execução são gerados aleatoriamente entre 3 e 5 segundos.
- A execução visual é vista com delay com time.sleep() e a tela é atualizada com os.system('cls'/'clear')

-----------------------------------------------------
##  Referências Utilizadas

### Vídeos:
- **Domine essas 10 Funções Obrigatórias em Python**  
  https://www.youtube.com/watch?v=NB9pdUDNAJ4&t=1701s  
- **Como usar def no Python - Funções Explicadas em 10min**  
  https://www.youtube.com/watch?v=u8piwlScXT8&t=310s  
- **Como Sair do Zero em Classes no Python - Self e Init Explicados**  
  https://www.youtube.com/watch?v=gomDSZaay3E&t=2800s  
- **Como Funcionam Classes e Programação Orientada a Objetos em Python - Aprenda em 10 Minutos!**  
  https://www.youtube.com/watch?v=97A_Cyyh-eU&t=590s  

### Documentação:
- [Documentação Oficial do Python](https://docs.python.org/3/tutorial/index.html)

### Ferramentas:
- Visual Studio Code  
- ChatGPT 
- Emojikeyboard.top

-----------------------------------------------------

## Uso da Inteligência Artificial

A IA foi utilizada principalmente para:

- Sugerir a criação da classe `Processo` para organizar melhor o código.
- Recomendação do uso das bibliotecas `time` e `os` para simulação e visualização do progresso e demonstração de como implementar.
- Tirar duvidas se implementações realizadas no codigo estão corretas.
- Solucionar de problemas relacionados ao uso de objetos compartilhados entre algoritmos. Recomendou a biblioteca `copy` e o uso de `deepcopy()` para garantir que os processos fossem executados de forma independente em cada algoritmo. Foi pedido tambem a implementação dessas bibliotecas na função corrida round_robin para faze-la funcionar.

---

## Extra

- O tempo de execução real dos algoritmos é medido com `time.time()` para comparação justa.
- `copy.deepcopy()` garante que cada algoritmo trabalhe com cópias independentes dos processos, evitando interferência entre as execuções.
- A interface é simples e intuitiva via terminal mesmo.
