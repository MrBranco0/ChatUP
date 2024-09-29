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

# Função de calculadora simples
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

# Função principal do chatbot
def chatbot():
    print("Olá, sou um chatbot!")
    historico = []  # Inicializa o histórico de mensagens

    while True:
        escolha = input("Escolha o chat ('matematica' para calculadora ou 'chatbot' para o assistente de IA): ").lower()
        if escolha == "matematica":
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
