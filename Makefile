all: main

main:
	venv/bin/python udpn.py

init:
	python3 -m venv venv

install:
	venv/bin/pip install -r requirements.txt

upgrade:
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade -r requirements.txt
