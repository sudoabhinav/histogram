Running on local?, try the following steps:

1. Clone the repo using ssh/https.
2. Create a virtual environment (python 3.x) and activate it (I've used [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)):
    - ```cd hypothizer```
    - ```mkvirtualenv hypothizer --python=/usr/bin/python3```
    - ```workon hypothizer```
3. Install required libraries: ```pip install -r requirements.txt```.
4. run ```./manage.py migrate```
5. run ```./manage.py runserver``` to start the local dev server
6. Browse to http://localhost:8000/app/home to access the histogram.
