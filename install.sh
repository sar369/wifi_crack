#! bin/bash
sudo apt update && apt upgrade -y
sudo apt install python && apt install python3 -y
sudo apt install python3-pip -y
sudo pip install termcolor
sleep 1 
pip install tqdm
sleep 3
echo Installation completed

