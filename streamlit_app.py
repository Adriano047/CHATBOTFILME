import streamlit as st
from openai import OpenAI

#Alterando o titulo da pagina
st.set_page_config(page_title="CineGuru", page_icon="🎬")


# Importação correta da biblioteca OpenAI
client = OpenAI(api_key=st.secrets["openai"]["OPENAI_API_KEY"])  

system_mensagem = {
    "role": "system",
    "content": (
        "Você é um chatbot especializado exclusivamente em filmes e séries. "
        "**NÃO** deve responder perguntas sobre outros assuntos. "
        "Se perguntarem algo fora desse tema, apenas diga que é um CHATBOT focado em falar sobre filmes e séries. "
        "Se o usuário perguntar sobre um filme ou série específica, forneça informações detalhadas sobre ela, incluindo enredo, diretor e elenco. "
        "Se pedirem uma recomendação, sugira filmes ou séries populares dentro do gênero que o usuário gosta. "
        "Se o usuário enviar uma saudação, responda normalmente e pergunte o que ele quer assistir."
        "Caso o usuário digite o nome de um filme ou série e você não encontrar, tente sugerir algo com o nome parecido."
    )
}
# Configuração da chave da API OpenAI
st.title("CineGuru")
# Definir um modelo padrão
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Inicializar histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir as mensagens do histórico do chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Aceitar entrada do usuário
if prompt := st.chat_input("Faça uma Pergunta relacionado a filmes e series"):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Exibir a mensagem do usuário na interface
    with st.chat_message("user"):
        st.markdown(prompt)

    # Enviar mensagem para o modelo OpenAI
    response = client.chat.completions.create(
    model=st.session_state["openai_model"],
    messages=[
        system_mensagem,  # Inclui a mensagem do sistema primeiro
        *st.session_state.messages  # Desempacota as mensagens do usuário e do assistente
    ]
)
    # Obter a resposta do assistente e exibir
    assistant_message = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    # Exibir a resposta do assistente
    with st.chat_message("assistant"):
        st.markdown(assistant_message)
