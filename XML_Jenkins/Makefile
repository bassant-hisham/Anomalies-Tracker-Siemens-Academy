VENV_ACTIVATE = env\Scripts\activate
PIP = env\Scripts\pip



.PHONY: setup
setup:
	python -m venv env
	$(VENV_ACTIVATE) && $(PIP) install -r requirements.txt


.PHONY: capture_requirements
capture_requirements:
	$(PIP) freeze > requirements.txt


.PHONY: clean
clean:
	rmdir /S /Q env
