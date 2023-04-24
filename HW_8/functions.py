def show_data() -> None:
    '''Выводит инфу из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())

def add_data() -> None:
    '''Добавляет инфу в справочник'''
    id_post = input('Введите ID: ')
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{id_post} | {fio} | {tel_number}')
    print('Успешно')

def find_data() -> None:
    '''Поиск по справочнику'''
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print(search(tel_book, data))
    
# def search(book: str, info: str) -> str:
#     '''Поиск по заданному критерию'''
#     book = book.split('\n')
#     return '\n'.join([post for post in book if info in post])
# print(search(tel_book, data))

def edit_data() -> None:
    '''Изменение данных'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    a = tel_book.split('\n')
    print(a)
    text = input("Введите значение, которое хотите поменять: ")
    b = (search(tel_book, text))
    a[a.index(b)] = edited(b)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(a))

def del_data() -> None:
    '''Удаление данных'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
        a = tel_book.split('\n')
        print(a)
        text = input("Введите значение, которое хотите удалить: ")
        b = (search(tel_book, text))
        a[a.index(b)] = remove(b)
    with open('book.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(a))

def search(book: str, info: str) -> str:
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])

def edited(text: str) -> str:
    fio = input('Введите новое ФИО при необходимости')
    num = input('Введите корректный телефон при необходимости')
    if len(fio) == 0:
        fio = text.split('|')[0]
    if len(num) == 0:
        num = text.split('|')[1]
    return f'{fio} | {num}'

def remove(text: str, remove_text: str) -> str:
    if remove_text.isalpha():
        num = text.split('|')[1]
        return f'| {num}'
    else:
        fio = text.split('|')[0]
        return f'| {fio}'
