<a id="readme-top"></a>
# 🍿 CineGuru
Um chatbot desenvolvido com a interface intuitiva do Streamlit, integrado à poderosa API da OpenAI, focado em fornecer tudo sobre filmes e séries! 🎬📺 Seja para descobrir curiosidades, recomendações ou informações detalhadas.

## ⚙️ Recursos 

- **Histórico:** Mantém o registro das conversas enquanto a página não for recarregada. Isso permite uma interação contínua e personalizada, adaptando-se às preferências do usuário durante a sessão.
- **Interface simples:** Utilizando o design intuitivo e clean do Streamlit, a interface do CineGuru apresenta um título destacado e um campo de entrada de conversa, proporcionando uma interação direta e sem complicações. O layout minimalista garante uma experiência       agradável, permitindo que o usuário se concentre no bate-papo sem distrações.
- **Respostas Temáticas:** Fornece informações completas e detalhadas sobre filmes e séries. Caso a pergunta fuja do tema, ele educadamente informa que não é um chatbot para esse tipo de assunto, mantendo o foco no universo do entretenimento. 
- **Assistência na Correção de Nomes:** Tenta ajudar quando o nome de um filme ou série é escrito de forma errada. Caso haja uma possível confusão, o chatbot sugere que o usuário estava se referindo ao título correto, oferecendo uma correção amigável para manter a conversa fluida e precisa.
  
## 💻 Estrutura 
### Interface Simples:
![Interface](https://github.com/user-attachments/assets/67a16a33-0aa7-4b42-9546-ceda4f317fe2)

### Historico:
![Historico](https://github.com/user-attachments/assets/c47fc488-8642-4c05-a853-9ef6ffcd87ae)

### Assistência na Correção de Nomes::
![Corrigindo](https://github.com/user-attachments/assets/6040920e-6a8a-4216-bfa7-03f897f8fcaa)

### Respostas Temáticas:
![Respostas](https://github.com/user-attachments/assets/265e3a95-0b46-4cf3-8c00-bc7ce14b0ec7)

### Codigo que restringe o conteudo:
![CodigoRestrincao](https://github.com/user-attachments/assets/8ad5077a-32f4-4f57-8867-ccb3e2683253)

## 💻 Rodando o Programa
https://github.com/user-attachments/assets/298b7638-6843-49a5-a6ce-10fcc26c2796

## ⚠️ Avisos:

### Como executá-lo em sua própria máquina

1. Dentro da pasta .streamlit crie um arquivo com o nome: "secrets.toml"
 ```
   # O conteudo do arquivo "secrets.toml"
   # Substitua "SUA_CHAVE" por uma chave valida da OPENAI
   [openai]
   OPENAI_API_KEY = "SUA_CHAVE" 
   ```
1. Instale os requisitos

   ```
   $ pip install -r requirements.txt
   ```

2. Executando o projeto

   ```
   $ streamlit run streamlit_app.py
   ```

## :octocat: Faça o clone do projeto

```bash
# Clone este repositório
$ gh repo clone Adriano047/CHATBOTFILME

# Acesse a pasta do projeto no terminal/cmd
$ cd me

```
## 👨🏻‍🚀 Sobre mim
"Conecte-se comigo no LinkedIn para explorar minha trajetória profissional e colaborar em projetos incríveis."
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/cardosodev047/"><img src="https://media.licdn.com/dms/image/v2/D4D03AQFRff9YjluTHQ/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1713879990636?e=2147483647&v=beta&t=AIThEkfC267uJ_bVz5bpXdPbuvQlDzdWdeb4JgeSkxQ" width="100px;" alt="Kent C. Dodds"/><br /><sub><b>Adriano Cardoso Santos</b></sub></a><br />
    </tr>
  </tbody>
</table>

<p align="right">(<a href="#readme-top">Voltar ao topo</a>)</p>
