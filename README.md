# CameraControlXYRoboticArm
  Description Camera control XY Robotic arm

## Python Version 2.7.12
## How to install python
  - make sure you have `wget` install on your computer
  - `mkdir ~/src`
  - `wget http://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz`
  - `tar -zxvf Python-2.7.12.tgz`
  - `cd Python-2.7.12`
  - `mkdir ~/.localpython`
  - `./configure --prefix=$HOME/.localpython`
  - `make`
  - `make install`
## PIP Version 9.0.1

## OpenCV library.
  - mkdir opencv_workspace
  - Now that we're in here, let's grab OpenCV:
  - sudo apt-get install git
  - git clone https://github.com/Itseez/opencv.git
  - sudo apt-get install build-essential
  - sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
  - sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev
    libdc1394-22-dev
  - sudo apt-get install libopencv-dev


## Set python env
  - clone the repo
  - cd to the project `cd CameraControlXYRoboticArm`
  - `source camera-control/bin/activate`
  - go to the server directory `cd Server`
  - `pip install -r requirements.txt`
  - In order to test that you're on the right path run `which pip` and make sure it points to this directory `CameraControlXYRoboticArm/camera-control/bin/pip' -----("I got:/usr/local/bin/pip")----
  - To start the server just run `./run.sh`

## Guides 
  - Follow this guide: `http://flask.pocoo.org/docs/0.12/tutorial/`
  - Great readme is here: `https://github.com/pallets/flask/tree/master/examples/flaskr`

## Manifest
  - Web server running on RasberryPie
  - The server will be running on the RasberryPie machine and will control the robotic arm
  - Languages: `Python` and `bash`
  - Deployment and version control using `git`
