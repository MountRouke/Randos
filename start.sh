#!/bin/sh
Xvfb :99 -screen 0 1024x768x24 +extension GLX +render > xvfblog.txt 2>&1 &
DISPLAY=:99.0 python3 main.py