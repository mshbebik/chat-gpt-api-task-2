import openai
import os 


openai.api_key = "API-TOKEN"

path = input("Введіть ім'я файлу:")
file = open(f"{path}", "r")
content = file.read()

messages = [{"role": "user", "content": f"Прочитай этот текст и выведи статистику по количеству слов, предложений и именованных сущностей в этом тексте: {content}"}]
    
completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')
messages.append({"role": "assistant", "content": chat_response})

