import flet as ft
from datetime import datetime

def main(page: ft.Page):
    # page.add(ft.Text("Hello world"))
    page.title = 'Мое первое приложение на Flet'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!")

    greeting_history = []
    history_text = ft.Text("Итория приветстий:")


    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Привет, {name}!"
            greet_button.text = "отправить еще раз"
            name_input.value = ""
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f'{timestamp} - {name}')
            history_text.value = "Итория приветстий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйте, введите имя!" 
        
        print(greeting_text.value)
        page.update()
    def clear_history(_):
        greeting_text.clear
        page.update
        clear_button = ft.IconButton()
    name_input = ft.TextField(label="Введите имя: on_sumbit=on_button_click")
    greet_button = ft.ElevatedButton("sell again", on_click=on_button_click)

    page.add(greeting_text, name_input, greet_button, history_text)


ft.app(target=main)