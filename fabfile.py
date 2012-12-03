from fabric.api import local
def addrepo():
	local('heroku git:remote -a diskas-dev')
	local('git remote add priv https://github.com/balaplumpat/diskas')
def deploy():
    local('git push heroku master')
    local('heroku run ./manage.py syncdb')
    local('heroku run ./manage.py migrate')
    local('git push')