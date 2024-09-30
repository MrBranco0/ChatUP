from groq import Groq

# Inicializa o cliente Groq 
client = Groq(
    api_key="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"
)

def mandar_mensagem(historico):
    # Tenta enviar o histórico de mensagens para o chatbot
    chat_completion = client.chat.completions.create(
        messages=historico,
        model="llama3-8b-8192",  # Verifique se esse modelo está disponível na sua API
    )
    return chat_completion

def matematica():
    while True:
        pergunta = str(input("Selecione a operação (adição, subtração, multiplicação, divisão): ")).lower()
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))

        if pergunta == "adiçao":
            resultado = a + b
            print(f"O resultado é {resultado}")
        elif pergunta == "subtraçao":
            resultado = a - b
            print(f"O resultado é {resultado}")
        elif pergunta == "divisao":
            if b != 0:
                resultado = a / b
                print(f"O resultado é {resultado}")
            else:
                print("Erro, impossível dividir por zero.")
        elif pergunta == "multiplicaçao":
            resultado = a * b
            print(f"O resultado é {resultado}")
        else:
            print("Operação inválida.")

        resposta = input("Continuar? (s/n): ").lower()
        if resposta == "n":
            print("Fechando e voltando ao menu principal...")
            break

def conversor_unidades():
    print("Conversor de unidades.")
    while True:
        tipo = input("Escolha a unidade (Comprimente/peso): ")

        if tipo == "comprimento":
            valor = float(input("Valor em metros: "))
            print (f"{valor} metros é igual a {valor * 100} centímetros.")
            print(f"{valor} metros é igual a {valor * 2.20462} polegadas.")
        elif tipo == "peso":
            valor = float(input("Valor em quilogramas: "))
            print(f"{valor} kg é igual a {valor * 1000} gramas.")
            print(f"{valor} kg é igual a {valor * 2.20362} libras")
        else:
            print("Tipo invalido")

        continuar = input("Continuar?(s/n)").lower()

        if continuar == "n":
            break

def rotina():
    compromissos = []
    while True:
        print("\nAgenda: ")
        print("1. adicionar compromisso")
        print("2. Ver compromisso")
        print("3. Apagar compromisso")
        print("4. Sair da Agenda")

        escolha = input("escolha o numero: ")

        if escolha == "1":
            compromisso = input("Fale um compromisso: ")
            compromissos.append (compromisso)
            print("compromisso adicionado!")
        elif escolha == "2":
            if compromissos:
                print ("Compromissos: ")
                for i, c in enumerate(compromissos, start=1):
                    print(f"{i}. {c}")
            else:
                print("Nenhum compromisso indentificado")

        elif escolha == "3":
            if compromissos:
                for i, c in enumerate(compromissos, start=1):
                    print(f"{i}. {c}")
                excluir = input("Selecione o número do compromisso a ser deletado: ")
        
                if excluir.isdigit():
                    indice = int(excluir) - 1
                    if 0 <= indice < len(compromissos):
                        removido = compromissos.pop(indice)
                        print(f"Compromisso '{removido}' removido.")
                    else:
                        print("Número inválido. Por favor, selecione um número da lista.")
                else:
                    print("Entrada inválida. Por favor, insira um número.")
            else:
                print("Não há compromissos para deletar.")

        elif escolha == "4":
            break
        else:
            print("nao indentificado")
                        
def chatbot():
    print("Olá, sou um chatbot!")
    historico = []  # Inicializa o histórico de mensagens

    while True:
        escolha = input("Escolha o chat ('matematica' para calculadora, 'chatbot' para o assistente de IA, 'conversor' para converter kg, 'rotina' para acessar sua agenda): ").lower()
        if escolha == "conversor":
            conversor_unidades()
        elif escolha == "rotina":
            rotina()
        elif escolha == "matematica":
            matematica()
        elif escolha == "chatbot":
            while True:
                mensagem_usuario = input("Você: ")
                if mensagem_usuario.lower() in ["sair", "exit"]:
                    print("Voltando ao menu principal...")
                    break
                
                # Adiciona a mensagem do usuário ao histórico
                historico.append({"role": "user", "content": mensagem_usuario})
                
                # Envia o histórico para o chatbot
                try:
                    mensagem = mandar_mensagem(historico)
                    
                    # Captura e imprime a resposta do chatbot
                    resposta_chatbot = mensagem.choices[0].message.content
                    print("ChatBot:", resposta_chatbot)
                    
                    # Adiciona a resposta do chatbot ao histórico
                    historico.append({"role": "assistant", "content": resposta_chatbot})
                
                except Exception as e:
                    print(f"Ocorreu um erro: {e}")
        elif escolha == "sair":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

# Inicia o chatbot
chatbot()
