import json
import os
from datetime import datetime

notes = []

def load_notes():
    global notes
    if os.path.exists('notes.json'):
        with open('notes.json', 'r') as file:
            notes = json.load(file)

def save_notes():
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

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

    note_id = int(input("Введите ID заметки для редактирования: "))
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

    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            print(f"Заметка с ID {note_id} успешно удалена.")
            return

    print(f"Заметка с ID {note_id} не найдена.")

def display_notes():
    if not notes:
        print("Список заметок пуст")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст заметки: {note['text']}")
            print(f"Дата/время: {note['timestamp']}")
            print()

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