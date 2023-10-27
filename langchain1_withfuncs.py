import os
from decouple import config
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')
def main():
    while True:
        sentence, target_language = get_user_input()
        translation = translate_to_language(sentence, target_language)
        print(translation)


def get_user_input():
    sentence = input("Enter the sentence that you want translated: ")
    target_language = input("Which language do you wanna translate to? ")
    return sentence, target_language


def translate_to_language(sentence, output_language):
    chat = ChatOpenAI()
    template = "You are a helpful assistant that translates the user's input to {output_language}"
    chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", template),
            ("human", sentence),
        ])
    messages = (chat_prompt.format_messages(output_language=output_language))
    return chat.predict_messages(messages)


if __name__ == '__main__':
    main()
