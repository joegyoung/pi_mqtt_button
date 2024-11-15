sudo apt install python3-pip
sudo pip3 install paho-mqtt
#sudo pip3 install rpi

sudo cp test.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable  test.service 
