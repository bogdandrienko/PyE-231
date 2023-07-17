import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('1.9.0')

"""
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt search openjdk
sudo apt update -y
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
python3 -m venv env
pip3 install -r requirements.txt
pip3 install --upgrade Cython==0.29.33 virtualenv
export PATH=$PATH:~/.local/bin/
buildozer -v android debug
"""



class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 2000))


class RandomNumber(App):
    def build(self):
        return MyRoot()


randomApp = RandomNumber()
randomApp.run()
