import os
from openai import OpenAI

client = OpenAI(

)


deployment='gpt-3.5-turbo'


prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(model=deployment, messages=messages)

print(completion.choices[0].message.content)

