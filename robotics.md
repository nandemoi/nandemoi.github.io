# Robotics

## Raspberry Pi

1. [System](https://www.raspberrypi.org/software/)
2. sudo raspi-config
   1. System: hostname (respberrypi -> eltonpi), autologins, preference: desktop pix
   2. Interface: ssh, vnc, Remote GPIO
   3. (Display: resolution 1280x1024, Advanced: Expand Filesystem)
3. change browser srch engine, 
"mega.nz download” → Desktop Apps: Raspbian 10 (32 bits), apt install gdebi, sudo gdebi …
   1. apt install code (python, verilog ![verilog1](https://i.imgur.com/3a5QbtN.png =20x20)![verilog2](https://i.imgur.com/2zUvdSz.png =20x20), teros, wavetrace), iverilog, yosys
   2. ps1, alias ls=‘ls -GFh —color=auto’
1. [Jupyter Notebook ](https://www.instructables.com/Jupyter-Notebook-on-Raspberry-Pi/)
2. [MQTT](https://blog.gtwang.org/iot/raspberry-pi/raspberry-pi-mosquitto-mqtt-broker-iot-integration/)
3. [OpenCV](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/) (Step 2+; #4a tried: 4.5.2.52, 4.4.0.46, 4.5.1.48)
   * [Using a standard USB webcam](https://www.raspberrypi.org/documentation/usage/webcams/)
   * [Working with Webcam using OpenCV](https://subscription.packtpub.com/book/hardware_and_creative/9781785285066/7/ch07lvl1sec41/working-with-webcam-using-opencv)
4. [Backup](https://www.raspberrypi.org/documentation/linux/filesystem/backup.md)

## [Industry 4.0 Middleware](https://mediatum.ub.tum.de/doc/1470362/1470362.pdf)

1. ROS/DDS
2. MQTT
