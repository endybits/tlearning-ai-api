install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
lint:
	pylint --disable=R,C *.py
test:
	python -m pytest -vv test_*.py
format:
	black *.py app/*.py
all: install lint test format