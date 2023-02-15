import openai
import wget

print("I am your Intelligent RCAI Image Generator bot, you can ask me anything.")
print("///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ")
while(1):
    PROMPT = input()
    openai.api_key = "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"
    response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="1024x1024",
)
    print(response["data"][0]["url"])
    file = wget.download(response["data"][0]["url"])
    print(file + " successfully downloaded")

    print("///// ///// ///// ///// ///// ///// ///// ///// ///// ///// ")
    print("anyother other image >>>")