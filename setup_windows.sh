cd
mkdir Project
cd Project
py -m pip install virtualenv
py -m virtualenv -p python3 venv
source venv/Scripts/activate
py -m pip install django
py -m pip install djangorestframework
django-admin startproject src 
cd src 
pwd
git clone https://github.com/ATKatary/Crossword.git crossword
rm -rf ../../temp
clear
echo "Now go into Project/src/src/settings.py and add the following to INSTALLED_APPS"
echo "'rest_framework',"
echo "'crossword'" 
read -p "Enter done once you finish: " response
source ../venv/bin/activate
python manage.py makemigrations
python manage.py migrate
rm src/urls.py
touch src/urls.py 
echo "from django.contrib import admin" >> src/urls.py
echo "from django.urls import path, include" >> src/urls.py
echo "urlpatterns = [" >> src/urls.py
echo "path('admin/', admin.site.urls)," >> src/urls.py
echo "path('', include('crossword.urls'))" >> src/urls.py
echo "]" >> src/urls.py
clear 
python manage.py runserver 

