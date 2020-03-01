# Blog

This project is made with [Python](https://www.python.org/) & [Django](https://www.djangoproject.com/).<br>

The Python version used in this project is 3.8.2.<br>

However you need to have at least Python 3.6 installed because of the use of 'f strings'.

## Installing Python dependencies

All dependencies are listed inside `requirements.txt`<br>

To install the dependencies run:<br>

`pip install -r requirements.txt`

## Starting the sass watcher

There's various methods for compiling sass files.<br>

I used Ruby Sass to compile & watch the files.<br>

`sass --watch styles.sass:styles.css --style compressed`

## Running the project

`python manage.py runserver`

If you Python3 isn't your default set Python version, you need to run a different command.<br>

`python3 ./manage.py runserver`
