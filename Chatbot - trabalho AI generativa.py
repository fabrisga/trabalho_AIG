import openai


openai.api_key = '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' #chave OpenAI

def eliza_simulator(prompt):
    persona = "Você é um chatbot de psicologia. Responda de modo cômico para as pessoas que buscam por ajuda."
    instructions = f"{persona}\nUsuário: {prompt}\nChatbot:"

    response = openai.Completion.create(
        engine="text-davinci-002",  # mecanismo GPT-3.5
        prompt=instructions,
        max_tokens=200  
    )

    return response.choices[0].text.strip()

# Interação com o chatbot
print("Olá! Sou a terapia cômica. Do que você precisa hoje?")
while True:
    user_input = input("Usuário: ")
    if user_input.lower() == "adeus":
        print("Chatbot: Espero que tenha sido útil. Cuide-se!")
        break
    response = eliza_simulator(user_input)
    print("Chatbot:", response)


