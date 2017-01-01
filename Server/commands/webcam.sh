#!/bin/bash
touch $(date +%s).txt
fswebcam -r 640x480 --no-banner ~/webcam/$(date +%s).jpg