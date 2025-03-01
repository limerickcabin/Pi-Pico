# Pi Pico
 Various microPython experiments with my Pi Pico

 Note that the wifi examples requires a creds.txt file with your accesspoint credentials in the form of a JSON string such as: 

 {"site": "web.com", "ssid": "wifiSSID", "pwd": "wifiPWD"}
# Raspberry Pi Pico
Very cool little processor that costs only $5 (if you can find one). 
# MicroPython
Detailed instructions are here:
https://www.raspberrypi.com/documentation/microcontrollers/micropython.html
## In short:
Download the image:
https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2

Get the Pico into bootloader mode by powering it on with BOOTSEL pressed

Pico will look like a drive to your computer

Drag the image over and reboot
## Thonny
Thonny is an IDE that runs on your computer allowing you to interact with microPython running on the Pico. 

It is very similar to the regular IDE you use with Python running on your PC. You can save files on the device or on your computer. Open a .py file (from your PC or Pico) and clicking the run icon will cause the Pico to run that script. You can also interact with it directly at the command line (just like regular Python). 

I forgot how to enable the remote device. After fooling around, this was the trick: 

Tools > Options > Interpreter > Port > USB Serial Device (COMx)

New version of Thonny is different: 
 


