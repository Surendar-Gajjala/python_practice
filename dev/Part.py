from openai import OpenAI

OpenAI.api_key ='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'

client = OpenAI()
def gsr(): 
    stream = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=[{"role": "user", "content": "Say this is a test"}],
       stream=True,
    )
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
          print(chunk.choices[0].delta.content, end="")

if __name__ == '__main__':
     gsr()
             