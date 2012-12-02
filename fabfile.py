from fabric.api import local

def deploy():
    local('git push heroku master')
    local('heroku run ./manage.py syncdb')
    local('heroku run ./manage.py migrate')