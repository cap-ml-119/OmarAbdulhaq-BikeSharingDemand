run:
    python app/main.py

setup: requirements.txt
    pip install -r requirements.txt

clean:
    rm -rf __pycache__

python3 -m venv venv

python3 app/main.py
./venv/bin/python3
./venv/bin/activate

venv/bin/activate: requirements.txt
 python3 -m venv venv
 ./venv/bin/pip install -r requirements.txt

 run: venv/bin/activate
 ./venv/bin/python3 app/main.py

 clean:
 rm -rf __pycache__
 rm -rf venv

 touch requirements.txt
 VENV = venv

 VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

run: $(VENV)/bin/activate
 $(PYTHON) app/main.py


$(VENV)/bin/activate: requirements.txt
 python3 -m venv $(VENV)
 $(PIP) install -r requirements.txt


clean:
 rm -rf __pycache__
 rm -rf $(VENV)

 make VENV=my_venv run
 .PHONY: run clean