from fabric.api import local

@task
def checkout():
    """ Run Test """
    local("ifconfig")

@task
def install():
    print 'install ing...'

@task
def test():
    """ Run Test """
    local("ifconfig")

@task
def deploy():
    print 'deploy ing...'

