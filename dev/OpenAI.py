import openai

openai.api_key = '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'

def poem_on_samosa():
    resonse = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= [
            {"role": "user", "content": 'write apoem on samosa. only 4 lines please.'}
        ]
    )

    print(resonse.choices[0]['message']['content'])


if __name__ == '__main__':
    poem_on_samosa()