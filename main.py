strok = input("введите кол-во строк: ") #запрос у пользователя кол-во строк

if strok.isdigit() and int(strok) > 0: #проверкан  на ввод
    strok = int(strok)
else:
    print("неправлиьно введено ")

text=[] #иницилиазия 
for i in range(strok): #цикл for
    texts = input(f"введите строку {i + 1}:  ") #ввод строки 
    text.append(texts)

text1 = ' '.join(text) #перекидывание списка в строки
word=text1.split() #разделение на подстроки
word=set(word)#контейнер,где не повторящиеся слова
count=len(word) #подсчет

print(f"кол-во различных слов: {count}")#вывод