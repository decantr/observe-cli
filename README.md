# observe-cli
### blurb
A terminal based home security program written in python for the Raspberry Pi 2

### operaton
Run the program from the cli with;

```
sudo python observe.py
```

### info
Ensure that python is aliased to python2.7

IR events will output a picture into a 'pics' folder alongside the program

> pics/monthdayhoursecond.jpg

### required python modules
* os
* time
* RPi.GPIO
* picamera
