cd
mkdir Project
cd Project
pip3 install virtualenv
virtualenv -p python3 venv
source env/bin/activate
pip3 install django
pip3 install djangorestframework
django-admin startproject src 
cd src
git clone https://github.com/ATKatary/Crossword.git
mkdir crossword 
cp Crossword crossword
rm -rf Crossword
rm -rf ../Crossword
echo "Now go into Project/src/src/settings.py and add 'restframework' and 'crossword' to INSTALLED_APPS\nAfter that run python3 manage.py runserver" 

