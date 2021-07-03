# Python
## Framework for AutoTests

### run pytest example:
pytest -v -m smoke
#####
pytest -v -m "not smoke"

### with allure
pytest -s -q -v -m smoke --alluredir ../reports --disable-pytest-warnings

### install requirements
pip install -r requirements.txt

### upgrade pip
pip install --upgrade pip
