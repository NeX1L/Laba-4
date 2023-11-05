class String:
    string = "NULL"

    def __init__(self, string):
        self.string = string

    def Size(self):
        return len(self.string)

    def WordСount(self, word):
        return self.string.count(word)

    def BigLetters(self):
        return self.string.upper()

    def LittleLetters(self):
        return self.string.lower()

    def OneSpace(self):
        string = ' '.join(self.string.split())
        self.string = string
        return string

if __name__ == '__main__':
    check = 0
    while(1):
        try:
            print("\tМеню работы со строками")
            print("1. Введите строку чтобы с ней работать")
            print("2. Вывод размера этой строки")
            print("3. Нахождение конкретного слова в подстроке")
            print("4. Вывод строки только с заглаными буквами")
            print("5. Вывод строки только с маленькими буквами")
            print("6. Вывод строки с один пробелом между словами")
            print("7. Завершить работу программы")
            chislo = input("Ваш выбор: ")
            number = int(chislo)
            if number < 0:
                print("Нельзя вводить отрицательные числа!!!")
            else:
             if number == 1:
                check = 1
                word = input("Введите строку: ")
                a = String(word)
             elif number == 2:
                if check == 1:
                    print("Размер данной строки равен: ", a.Size())
                else:
                    print("Введите сначала строку чтобы с ней работать")
             elif number == 3:
                if check == 1:
                    while(1):
                        print("Введите слово которое хотите подсчитать в строке ", a.string)
                        word = input("Введите слово: ")
                        if " " in word:
                            print("Слово должно быть без пробела")
                        else:
                            chislo = int(a.WordСount(word))
                            if chislo == 0:
                                print("Такого слова нету")
                            else:
                                print(f" Слово '{word} найдено в кол-ве '{a.WordСount(word)}' штук'")
                            break
                else:
                    print("Введите сначала строку чтобы с ней работать")
             elif number == 4:
                 if check == 1:
                     print("Все буквы заглавные", a.BigLetters())
                 else:
                     print("Введите сначала строку чтобы с ней работать")
             elif number == 5:
                 if check == 1:
                     print("Все буквы маленькие", a.LittleLetters())
                 else:
                     print("Введите сначала строку чтобы с ней работать")
             elif number == 6:
                 if check == 1:
                     print(f"Теперь в строке '{a.OneSpace()}' один пробел между словами")
                 else:
                     print("Введите сначала строку чтобы с ней работать")
             elif number == 7:
                exit(1)
        except ValueError:
            print("Неккоректный ввод, попробуйте еще раз")