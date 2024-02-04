import g4f
from yf import news

g4f.debug.logging = True  # Enable debug logging
g4f.debug.version_check = False  # Disable automatic version checking
print(g4f.Provider.Bing.params)  # Print supported args for Bing

ticker = input()

response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": f"""Do not say hello. Just give me what i want.Send only text. Do readable text .NEWS summarize shortly and in russian.{news(ticker)}.Ignore the links"""}],
)   


print(response)