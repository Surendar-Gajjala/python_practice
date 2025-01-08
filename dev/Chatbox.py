import openai

openai.api_key = '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'

completion = openai.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)