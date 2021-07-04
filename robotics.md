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
4. [Miniconda3](https://www.anegron.site/2020/06/18/how-to-install-conda-and-docker-on-your-raspberry-pi/)
    * [b4 install python=3.6](https://medium.com/linux-on-raspberry-pi4/raspberry-pi%E5%AE%89%E8%A3%9Dopencv%E8%88%87jupyter-%E9%80%8F%E9%81%8Econda%E6%96%B9%E6%B3%95-d0752743478): sudo chown -R pi miniconda3
5. [MQTT](https://blog.gtwang.org/iot/raspberry-pi/raspberry-pi-mosquitto-mqtt-broker-iot-integration/)
6. [OpenCV](https://www.anegron.site/2020/06/18/how-to-install-conda-and-docker-on-your-raspberry-pi/)
   * [Using a standard USB webcam](https://www.raspberrypi.org/documentation/usage/webcams/)
   * [Accessing the Raspberry Pi Camera with OpenCV and Python
](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/) (Step 4+, [swapsize](https://medium.com/ching-i/%E6%A8%B9%E8%8E%93%E6%B4%BE%E5%AE%89%E8%A3%9D-opencv-4-4-0-606900caf370))
7. [Backup](https://www.raspberrypi.org/documentation/linux/filesystem/backup.md)

## [Industry 4.0 Middleware](https://mediatum.ub.tum.de/doc/1470362/1470362.pdf)

1. ROS/DDS
2. MQTT
