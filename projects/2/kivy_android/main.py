import time
import requests
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.lb1 = Label(text='title')
        self.add_widget(self.lb1)

        self.username = TextInput(multiline=False)
        self.username.text = "posts"
        self.add_widget(self.username)

        self.lb2 = Label(text='body')
        self.add_widget(self.lb2)

        self.password = TextInput(password=False, multiline=False)
        self.add_widget(self.password)

        self.start = Button(text='send to server')
        self.start.background_color = (1, 1, 255, 1)
        self.start.bind(on_press=self.callback_start)
        self.add_widget(self.start)

    def callback_start(self, instance):
        self.start.disabled = True
        self.start.background_color = (1, 255, 1, 255)
        url = f"https://jsonplaceholder.typicode.com/{self.username.text}"
        content = {
            "title": self.username.text,
            "body": self.password.text,
            "userId": 1,
        }
        time.sleep(2.0)
        response = requests.post(url=url, data=content)
        if response.status_code == 200 or response.status_code == 201:
            print("Success")
            self.username.text = ""
            self.password.text = ""
            self.start.background_color = (1, 255, 1, 1)
        else:
            print(response.status_code)
            self.start.background_color = (255, 1, 1, 1)
        self.start.disabled = False


class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
