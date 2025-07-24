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
            current_hour = datetime.now().hour
            if 6 <= current_hour < 12:
                greeting = "Доброе утро"
                greeting_text.color = ft.colors.YELLOW
            elif 12 < current_hour < 18:
                greeting = "Добрый день"
                greeting_text.color = ft.colors.ORANGE
            elif 18 < current_hour < 24:
                greeting = "Добрый вечер"
                greeting_text.color = ft.colors.RED
            else:
                greeting = "Доброй ночи"
                greeting_text.color = ft.colors.BLUE
            greeting_text.value = f"{greeting}, {name}!"
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
    def on_toogle_history(_):
        nonlocal history_visible
        history_visible = not history_visible
        history_text.visible = history_visible
        toggle_history_button.text = "показать историю" if not history_visible else "скрыть историю"
        page.update()



    name_input = ft.TextField(label="Введите имя: on_sumbit=on_button_click")
    greet_button = ft.ElevatedButton("sell again", on_click=on_button_click)
    toggle_history_button = ft.ElevatedButton("показать/скрыть историю", on_click=on_toogle_history)

    page.add(greeting_text, name_input, greet_button, history_text, toggle_history_button)


ft.app(target=main)