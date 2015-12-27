#!/bin/bash

# no unset variables
set -u
# exit script on error
set -e

# load v4l2 module
sudo modprobe bcm2835-v4l2

trap "sudo rmmod bcm2835-v4l2; exit" INT TERM EXIT

# set (maximum) frame-rate
v4l2-ctl -p 15
# set auto-exposure (for night-capture)
v4l2-ctl --set-ctrl=exposure_dynamic_framerate=1

echo "opening stream on port 12345"
cvlc v4l2:///dev/video0 --v4l2-width 1920 --v4l2-height 1080 --v4l2-chroma h264 \
     --sout '#std{access=http,mux=ts,dst=0.0.0.0:12345}'

trap - INT TERM EXIT

