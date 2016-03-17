ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
VENV = venv/bin
ACTIVATE = . venv/bin/activate;

run:
	$(ROOT_DIR)/$(VENV)/python market_maker.py

test:
	$(ROOT_DIR)/$(VENV)/py.test
