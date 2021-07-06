# Robotics

## Raspberry Pi

1. [System](https://www.raspberrypi.org/software/)
   * [Raspbian + OpenCV pre-configured and pre-installed](https://www.pyimagesearch.com/2016/11/21/raspbian-opencv-pre-configured-and-pre-installed/)
2. sudo raspi-config
   1. System: hostname (respberrypi -> eltonpi), autologins, preference: desktop pix
   2. Interface: ssh, vnc, Remote GPIO
   3. (Display: resolution 1280x1024, Advanced: Expand Filesystem)
3. change browser srch engine,
"mega.nz download” → Desktop Apps: Raspbian 10 (32 bits), apt install gdebi, sudo gdebi …
   * ps1, alias ls=‘ls -GFh —color=auto’
4. [Jupyter Notebook](https://www.instructables.com/Jupyter-Notebook-on-Raspberry-Pi/)
5. [MQTT](https://blog.gtwang.org/iot/raspberry-pi/raspberry-pi-mosquitto-mqtt-broker-iot-integration/)
6. [OpenCV](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/) (Step 2+; #4a tried: 4.5.2.52, 4.4.0.46, 4.5.1.48)
   * [Object detection with Raspberry Pi and Python](https://medium.datadriveninvestor.com/object-detection-with-raspberry-pi-and-python-bc6b3a1d4972)
     * [Using a standard USB webcam](https://www.raspberrypi.org/documentation/usage/webcams/)
     * [Working with Webcam using OpenCV](https://subscription.packtpub.com/book/hardware_and_creative/9781785285066/7/ch07lvl1sec41/working-with-webcam-using-opencv)
7. [Backup](https://www.raspberrypi.org/documentation/linux/filesystem/backup.md)

## [Industry 4.0 Middleware](https://mediatum.ub.tum.de/doc/1470362/1470362.pdf)

1. ROS/DDS
2. MQTT

## Jetson Nano

* [YOLOv4 on Jetson Nano](https://jkjung-avt.github.io/yolov4/)
  * [Yolo-Tiny](https://www.pyimagesearch.com/2020/01/27/yolo-and-tiny-yolo-object-detection-on-the-raspberry-pi-and-movidius-ncs/)
    * [Object detection with Raspberry Pi and Python](https://medium.datadriveninvestor.com/object-detection-with-raspberry-pi-and-python-bc6b3a1d4972)
      * [TensorFlow 2 Detection Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) 
      * [Hosted models | TensorFlow Lite](https://www.tensorflow.org/lite/guide/hosted_models)
      * [Model Zoo](https://modelzoo.co/)
   * [YOLO-fastest + NCNN on Raspberry Pi 4 教學](https://medium.com/ching-i/yolo-fastest-ncnn-on-raspberry-pi-4-f44143b44e45)
   * [OpenVINO, OpenCV, and Movidius NCS on the Raspberry Pi](https://www.pyimagesearch.com/2019/04/08/openvino-opencv-and-movidius-ncs-on-the-raspberry-pi/)

