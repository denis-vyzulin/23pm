#!/bin/bash
# USE FROM: ../public_html/

# Install virtualenv and activate it
cd ../
if ! [ -d ./venv/ ]; then
    if ! [ -f virtualenv.pyz ]; then
        wget https://bootstrap.pypa.io/virtualenv/3.6/virtualenv.pyz
    fi
    python3 virtualenv.pyz venv
fi
. venv/bin/activate
echo "Virtual environment successfully activated!"

# Export variables to environment
if [ -f env.sh ]; then
    . env.sh
    echo "Environ variables successfully exported!"
else
    echo "WARNING! Environ variables failed to load!"
fi

# Change hosting settings-file
if [ -f server.py ]; then
    cp ./server.py ./public_html/config/server.py
fi

# Change settings-file
if [ -f prod.py ]; then
    cp ./prod.py ./public_html/config/settings/prod.py
fi

# Install dependencies
cd public_html/
pip install -r requirements.txt

# Deploy website, activate database and run server
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver --settings='config.settings.prod'
