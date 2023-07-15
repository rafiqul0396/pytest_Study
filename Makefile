install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=greeting tests
	python -m pytest --nbval notebook.ipynb	#tests our jupyter notebook

debug:
	python -m pytest -vv --pdb	#Debugger is invoked when a test fails

one-tests:
	python -m pytest -vv tests/test_greetings.py::test_my_name1

format:
	black *.py


lint:
	pylint --disable=R,C hello.py

all: install lint test format