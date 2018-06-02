with open("ozhegov.txt", "r", encoding='utf-8') as f:
    text = f.read()
    text = text.split("\n")
    i = 0
    words = input ("Введите слова: ")
    words = words.split(" ")
    for line in text:
        line = line.split("|")
        if len(line) > 2:
            if line[2] != "":
                i += 1
        if line[0][0:3]=="кин" and line[0][-1:]=="т":
            print(line)
    for word in words:
        a = []
        f = 0
        for line in text:
            line = line.split("|")
            if word != "":
                if word == line[0]:
                    f = 1
                    if len(line) > 2:
                        print(word,":",len(word),":",line[1],":",line[3])
        if f == 0:
            print("Слово",word,"не найдено")
    print(i," слов с антонимами")
