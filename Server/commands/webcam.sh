
#!/bin/bash
timestamp() {
  date +"%T"
}
DATE=timestamp

fswebcam -r 640x480 --no-banner ~/webcam/$DATE.jpg