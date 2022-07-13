# femmyte-stack

stack overflow clone `python-decouple` this is used to create python environment
variable witout exposing it to the public

## PROJECT SETUP

1.  Create a virtual environment
2.  Install django and other python packages (check the requirement.txt file)
3.  setup python project
4.  store secrete key/config keys in environment variables CREATE .env file in
    the project folder ADD django_extension to INSTALLED_APPS RUN (python
    manage.py generate_secrete_key) to get th environment keys, copy and paste
    it to the .env file CHANGE the secerete key in settings.py file
5.  create apps
6.  configure templates and static folders
7.  push to github

to use any css, javascript and images in html file we need to first load static
file {% load static %} then we need to add STATICFILES_DIRS =
[BASE_DIR/'static'] in our Settings.py file after then we create a static folder
where we will put all the files in the project folder if we want to link link
css we do it like `<link rel="stylesheet" href="{% static 'css/style.css' %}">`
the style.css is inside the css folder which is inside the static folder
