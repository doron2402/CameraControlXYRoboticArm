
#!/bin/bash
timestamp() {
  date +"%T"
}
DATE=$(date+%s)

fswebcam -r 640x480 --no-banner ~/webcam/$DATE.jpg