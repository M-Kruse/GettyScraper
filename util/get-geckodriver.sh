#!/bin/sh
#You may need to adjust the version here depending on which Firefox version you have
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
sudo tar -xvf geckodriver-v0.24.0-linux64.tar.gz -C /usr/local/bin/
rm -f geckodriver-v0.24.0-linux64.tar.gz
