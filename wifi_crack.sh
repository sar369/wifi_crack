#! bin/bash

ifconfig wlan0 down
airmon-ng wlan0 kill
iwconfig wlan0 mode monitor
ifconfig wlan0 up
airmon-ng wlan0 start
iwconfig

