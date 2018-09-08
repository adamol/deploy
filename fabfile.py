from __future__ import with_statement
from fabric.api import cd, run, env
from fabric.decorators import task

env.use_ssh_config = True
env.hosts = ['deployprod-user', 'deployprod-user-2']

@task
def deploy():
    with cd('/home/deploy/current'):
        run('git pull origin master')
        run('composer install')
        run('sudo service php7.1-fpm reload')
