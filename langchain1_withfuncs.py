import os
from decouple import config
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')
def main():
    while True:
        print(translate())


def translate():
    chat = ChatOpenAI()
    user_input = input("Enter the sentence that you want translated: ")
    output_lang = input("Which language do you wanna translate to? ")
    template = "You are a helpful assistant that translates the user's input to {output_language}"
    human_template = user_input
    chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            ("human", human_template),
        ])
    messages = (chat_prompt.format_messages(output_language=output_lang))
    return chat.predict_messages(messages)


if __name__ == '__main__':
    main()
