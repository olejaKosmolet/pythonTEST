import json
import os
from datetime import datetime


notes = []

def load_notes():
    global notes
    file_path = os.path.join('notes', 'notes.json')
    if os.path.exists('notes/notes.json') and os.path.getsize('notes/notes.json') > 0:
        with open('notes/notes.json', 'r') as file:
            notes_data = json.load(file)
            if isinstance(notes_data, list):
                notes = notes_data
            else:
                print("Файл содержит некорректные данные. Создан новый список заметок.")
                notes = []
    else:
        print("Файл с заметками пуст или не существует. Создан новый список заметок.")

def save_notes():
    root_path = os.path.dirname(os.path.abspath(__file__))
    notes_path = os.path.join(root_path, 'notes/notes.json')
    if 'notes' in globals() and isinstance(notes, list):
        with open(notes_path, 'w') as file:
            json.dump(notes, file, indent=4)
        print("Заметки успешно сохранены в файл notes.json в папке notes")
    else:
        print("Не удалось сохранить заметки. Переменная 'notes' не найдена или содержит некорректные данные.")
        

def add_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_note = {
        'id': len(notes) + 1,
        'title': title,
        'text': text,
        'timestamp': timestamp
    }

    notes.append(new_note)
    print("Заметка успешно добавлена!")

def edit_note():
    if not notes:
        print("Список заметок пуст. Нечего редактировать.")
        return

    
    note_id = input("Введите ID заметки для редактирования: ")
    if not note_id.isdigit():
        print("Пожалуйста, введите числовое значение для ID заметки.")
    else:
        note_id = int(note_id)        

    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_text = input("Введите новый текст заметки: ")
            note['title'] = new_title
            note['text'] = new_text
            note['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Заметка с ID {note_id} успешно отредактирована.")
            return

    print(f"Заметка с ID {note_id} не найдена.")

def delete_note():
    if not notes:
        print("Список заметок пуст. Нечего удалять.")
        return

    while True:
        note_id = input("Введите ID заметки для удаления: ")
        if not note_id.isdigit():
            print("Пожалуйста, введите числовое значение для ID заметки.")
        else:
            note_id = int(note_id)
            break

    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            print(f"Заметка с ID {note_id} успешно удалена.")
            return

    print(f"Заметка с ID {note_id} не найдена.")

def display_notes():
    if not notes:
        print("Список заметок пуст.")
    else:
        while True:
            filter_date_str = input("Введите дату для фильтрации (ДД-ММ-ГГГГ): ")
            try:
                filter_date = datetime.strptime(filter_date_str, "%d-%m-%Y").date()
                break  # Правильный формат даты введен, выходим из цикла
            except ValueError:
                print("Некорректный формат даты. Пожалуйста, введите дату в формате ДД-ММ-ГГГГ.")

        filtered_notes = [note for note in notes if datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S").date() == filter_date]

        if filtered_notes:
            for note in filtered_notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст заметки: {note['text']}")
                print(f"Дата/время: {note['timestamp']}")
                print()
        else:
            print("Нет заметок для указанной даты.")

def main():
    load_notes()
    while True:
        command = input("Введите команду: ")
        if command == "add":
            add_note()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "display":
            display_notes()
        elif command == "exit":
            save_notes()
            break

if __name__ == "__main__":
    main()