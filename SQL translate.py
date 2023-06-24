import os
import openai

openai.api_key = "your api key"
model_engine = "text-davinci-003"
user_input = input("Insert a text:")
prompt = "Translate natural language to SQL queries" + user_input

response = openai.Completion.create(
  engine=model_engine,
  prompt=prompt,
  max_tokens=2000,
  top_p=1,
  stop=None,
  temperature=0.5
)

r = response.choices[0].text
print("A:"+r)