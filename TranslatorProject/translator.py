from translate import Translator

translator = Translator(to_lang="ja")


try:
    with open("./Intro.txt", "r") as my_file:
        translation = translator.translate(my_file.read())
        print(translation)
except FileNotFoundError as err:
    print("file not found.")

