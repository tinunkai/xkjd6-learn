all: main

%: %.py
	@.venv/bin/python $<

jm:
	@.venv/bin/python main.py --jm

init:
	python3 -m venv .venv

install:
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

fmt:
	.venv/bin/black .
