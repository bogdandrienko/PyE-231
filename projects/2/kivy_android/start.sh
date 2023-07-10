sudo apt-get update -y
sudo apt-get install -y git zip unzip openjdk-17-jdk python3-dev python3-venv python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
cd Downloads
mkdir kivy_android && cd kivy_android
python3 -m venv env && source env/bin/activate
pip install kivy buildozer Cython==0.29.19 virtualenv
pip freeze > requirements.txt
export PATH=$PATH:~/.local/bin/
buildozer init
buildozer -v android debug
