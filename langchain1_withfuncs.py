import os
from decouple import config
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')

def main():
    sentence, target_language = get_user_input()
    while True:
        translation = translate_to_language(sentence, target_language)
        print(translation)

        while True:  # This nested loop will keep asking for choice until a valid one is provided.
            choice = input("Would you like to: \n1) Enter a new sentence\n2) Change translation language\n3) Exit\nChoose [1/2/3]: ").strip()

            if choice == "1":
                sentence, target_language = get_user_input()
                break  # Break out of the choice loop to continue with main translation loop.
            elif choice == "2":
                target_language = input("Which language do you wanna translate to? ")
                break  # Break out of the choice loop to continue with main translation loop.
            elif choice == "3":
                print("Goodbye!")
                return  # Exit the main function completely.
            else:
                print("Invalid choice. Please select 1, 2, or 3.")


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
