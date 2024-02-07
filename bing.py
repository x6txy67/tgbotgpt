from libretranslatepy import LibreTranslateAPI
from investgpt import main

lt = LibreTranslateAPI("https://translate.terraprint.co/")

print(lt.translate(main(), "en", "ru"))


