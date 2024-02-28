set -e 

echo "Deployment Start"

#Pull the latest version of the app
git pull origin main
echo "New changes Copied to Server"

#Activate Virtual environment
Source env/Scripts/activate
echo "Virtual Env Activated"

echo "Installing Dependencies"
pip install -r requirements.txt 

echo "serving Static Files"
python manage.py collectstatic 

echo "Running Database Migrations"
python manage.py makemigrations
python manage.py migrate

#Deactivate Virtual Environment
deactivate
echo "Virtual env Deactivated"

#Reloading Application So new Changes detect
pushd devalaya
touch asgi.py
popd

echo "Deoployment Finished"

