#! /bin/sh
service NetworkManager stop
service wpa_supplicant stop
ifconfig wlan0 down
python3 11.py
ifconfig wlan0 up
gcc 0.c -o 0
./0
python3 3.py
