#! bin/bash
sudo apt update && apt upgrade -y
sudo apt install python && apt install python3 -y
sudo apt install python3-pip -y
sudo pip install termcolor
sudo apt-get install gnome-terminal
which gnome-terminal
export PATH="/usr/bin:$PATH"
sleep 1 
pip install tqdm
sleep 3
echo Installation completed

