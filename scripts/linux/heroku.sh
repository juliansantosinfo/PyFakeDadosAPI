#! /bin/bash

# login in heroku
read -p "Login in Heroku? : " login
if [[ $login == "y" ]]
    then
        heroku login
fi

# Push changes to heroku.
read -p "Deploy changes in Heroku? : " deploy
if [[ $deploy == "y" ]]
    then
        git checkout main
        git push heroku main
fi

# Migrate  database.
heroku run ./manage.py makemigrations backend && ./manage.py migrate

# Create superuser.
heroku run ./manage.py admin_initialize

# Show app info
heroku apps:info

# fakedatabase
read -p "Open app in browser? : " open
if [[ $open == "y" ]]
    then
        heroku apps:open
fi