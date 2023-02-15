import openai

openai.api_key = "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"

model_engine = "text-davinci-003"
print("I am your Intelligent RCAI bot, you can ask me anything.")
print("///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ")
while(1):
    prompt = input()
    completion = openai.Completion.create(
   engine=model_engine,
   prompt=prompt,
   max_tokens=1024,
   n=1,
   stop=None,
   temperature=0.5,
)

    response = completion.choices[0].text
    print(response)
    print("///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ")
    print("anyother question >>>")