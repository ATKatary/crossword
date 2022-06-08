cd
mkdir Project
cd Project
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip3 install django
pip3 install djangorestframework
django-admin startproject src 
cd src 
pwd
git clone https://github.com/ATKatary/Crossword.git crossword
rm -rf ../../temp
echo "Now go into Project/src/src/settings.py and add 'rest_framework' and 'crossword' to INSTALLED_APPS" 
read -p "Enter done once you have have added 'rest_framework' and 'crossword' to INSTALLED_APPS in Project/src/src/settings.py: " response
source ../venv/bin/activate
python3 manage.py runserver 

