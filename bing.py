import g4f
from yf import news

g4f.debug.logging = True  # Enable debug logging
g4f.debug.version_check = False  # Disable automatic version checking
print(g4f.Provider.Bing.params)  # Print supported args for Bing

ticker = input()

response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": f"""Не говори "привет". Просто дайте мне то, что я хочу. Присылайте только текст. Делайте читабельный текст .NEWS summary shortly and in russian.{news(ticker)}.Не обращайте внимания на ссылки """}],
)  


print(response)