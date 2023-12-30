class Widget():
    def __init__(self, title_text, x_num, y_num):
        self.title = title_text
        self.x = x_num
        self.y = y_num

    def print_info(self):
        print('Напис:', self.title)
        print('Розташування:', self.x, self.y)

class Button(Widget):
    def __init__(self, title_text, x_num, y_num, is_clicked_bool):
        super().__init__(title_text, x_num, y_num)
        self.is_clicked = is_clicked_bool
    def click(self):
        self.is_clicked = True
        print('Ви зареєстровані')
lotery_button = Button('Брати участь', 100, 100, False)
lotery_button.print_info()
answer = input('Бажаєте зареєструватися? (так / ні): ')
if answer == 'так':
    lotery_button.click()
else:
    print('А шкода!')