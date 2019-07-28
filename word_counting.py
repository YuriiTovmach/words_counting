#! Words counting from files
import os
from g_w import get_words
from g_w_d import get_words_dict



def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print("Кол-во слов: %d" % len(words))
        print("Кол-во уникальных слов: %d" % len(words_dict))
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()