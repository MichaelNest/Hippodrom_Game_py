from tkinter import *
from tkinter import messagebox
from tkinter import ttk



'''Чтение из файла суммы денег'''
def load_money():
    try:
        with open('money.txt') as fr:
            m = int(f.readline())
    except FileNotFoundError:
        print(f'Файла не сущуствует, задано значение {default_money} {valuta}')
        m = default_money
    return m

'''Запись суммы в файл'''
def save_money(money_to_save):
    try:
        with open('money.txt', 'w') as fw:
            fw.write(str(money_to_save))
    except:
        print('Ошибка создания файла. Наш ипподром закрывается!!')
        quit(0)

'''Добавление строки в текстовый блок'''
def insert_text(s):
    text_diary.insert(INSERT, s +'\n')
    text_diary.see(END)

'''Расположение лошадей на экране'''
def horse_in_window():
    horse_1.place(x=int(x_1), y=20)
    horse_2.place(x=int(x_2), y=100)
    horse_3.place(x=int(x_3), y=180)
    horse_4.place(x=int(x_4), y=260)

# -----------------------------------------------------------------------------------
'''Создаем обьект окна'''
root = Tk()
'''Размер окна'''
WIDTH = 1024
HEIGHT = 600

'''Позиции лошадей'''
x_1 = 20
x_2 = 20
x_3 = 20
x_4 = 20

'''Имена лошадей'''
name_horse_1 = 'Конь в Пальто'
name_horse_2 = 'Джокер'
name_horse_3 = 'Петрушка'
name_horse_4 = 'Копытце'

'''Финансовые показатели'''
default_money = 100000
money = 0
valuta = 'грн'
# -------------------------------------------------------------------------------

'''Создаем главное окно - вычисляем координаты главного окна по центру'''
POS_X = root.winfo_screenwidth()//2 - WIDTH//2
POS_Y = root.winfo_screenheight()//2 - HEIGHT//2

'''Запрещаем изменение размеров окна'''
root.resizable(False, False)

'''Устанавливаем заголовок'''
root.title('Ипподром')

'''Устанавливаем ширину, высоту и позицию'''
root.geometry(f'{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}')

'''Загружаем изображения, Устанавливаем их в Label'''
road_image = PhotoImage(file = 'road.png')
road = Label(root, image = road_image)
road.place(x=0, y=17)


horse_1_image = PhotoImage(file = 'horse01.png')
horse_1 = Label(root, image = horse_1_image)

horse_2_image = PhotoImage(file = 'horse02.png')
horse_2 = Label(root, image = horse_2_image)

horse_3_image = PhotoImage(file = 'horse03.png')
horse_3 = Label(root, image = horse_3_image)

horse_4_image = PhotoImage(file = 'horse04.png')
horse_4 = Label(root, image = horse_4_image)

'''Выводим изображения лошадей на экран'''
horse_in_window()

'''Создаем кнопку и выводим ее на экран'''
start_button = Button(text = 'СТАРТ', font = 'arial 20', width = 61, background = '#37AA37')
start_button.place(x=20, y=370)

'''Создаем информационный чат виджитом Text'''
text_diary = Text(width = 70, height = 8, wrap = WORD)
text_diary.place(x=430, y=450)

'''Создаем и прикрепляем к тексту полосу прокрутки'''
scroll = Scrollbar(command = text_diary.yview())
scroll.place(x=990, y=450,  width = 20,  height = 132)
text_diary['yscrollcommand'] = scroll.set

'''Загружаем сумму средств игрока из файла'''
money = load_money()

'''Запрещаем вход на ипподром без денег'''
if(money <=0):
    messagebox.showinfo('Стоп!!', 'Вход на ипподром без средств запрещен!!')
    quit(0)

'''Формируем текстовую строку и выводим в нее оставшуюся сумму средств'''
label_all_money = Label(text = f'Осталось средств: {money} {valuta}', font = 'Arial 12')
label_all_money.place(x=20, y=565)

'''Выводим текстовые метки в левом нижнем углу окна'''
label_horse_1 = Label(text = 'Ставка на лошадь №1')
label_horse_1.place(x=20, y=450)

label_horse_2 = Label(text = 'Ставка на лошадь №2')
label_horse_2.place(x=20, y=480)

label_horse_3 = Label(text = 'Ставка на лошадь №3')
label_horse_3.place(x=20, y=510)

label_horse_4 = Label(text = 'Ставка на лошадь №4')
label_horse_4.place(x=20, y=540)

'''Чекбоксы для лошадей'''
horse_1_game = BooleanVar()
horse_1_game.set(0)
horse_check_1 = Checkbutton(text = name_horse_1, variable = horse_1_game, onvalue = 1, offvalue = 0)
horse_check_1.place(x=150, y=448)

horse_2_game = BooleanVar()
horse_2_game.set(0)
horse_check_2 = Checkbutton(text = name_horse_2, variable = horse_2_game, onvalue = 1, offvalue = 0)
horse_check_2.place(x=150, y=478)

horse_3_game = BooleanVar()
horse_3_game.set(0)
horse_check_3 = Checkbutton(text = name_horse_3, variable = horse_3_game, onvalue = 1, offvalue = 0)
horse_check_3.place(x=150, y=508)

horse_4_game = BooleanVar()
horse_4_game.set(0)
horse_check_4 = Checkbutton(text = name_horse_4, variable = horse_4_game, onvalue = 1, offvalue = 0)
horse_check_4.place(x=150, y=538)

'''Выпадающий список'''
stavka_1 = ttk.Combobox(root)
stavka_2 = ttk.Combobox(root)
stavka_3 = ttk.Combobox(root)
stavka_4 = ttk.Combobox(root)

'''Задаем атрибут - ТОЛЬКО ДЛЯ ЧТЕНИЯ'''
stavka_1['state'] = 'readonly'
stavka_1.place(x=280, y=450)

stavka_2['state'] = 'readonly'
stavka_2.place(x=280, y=480)

stavka_3['state'] = 'readonly'
stavka_3.place(x=280, y=510)

stavka_4['state'] = 'readonly'
stavka_4.place(x=280, y=540)


insert_text('Добро пожаловать на ипподром!!')
for i in range(11):
    insert_text('Бла-бла-бла')
    insert_text('Ла-ла-ла-ла')

'''Выводим главное окно на экран'''
root.mainloop()