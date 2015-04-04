from fabric.api import local, sudo, env, put, cd, settings, task
from fabric.colors import red, green, blue


# GLOBAL VALUES
env.user = 'deploy'
env.key_filename = '~/.ssh/id_rsa_deploy'
env.remote_tmp_dir = '/tmp'
env.remote_web_dir = '/var/www'
env.remote_avail_dir = '/etc/nginx/sites-available'
env.remote_enab_dir = '/etc/nginx/sites-enabled'

env.app_name = 'TechNotes'
env.app_prefix = 'gorauskas.org'
env.code_artifact = '%s.tar.gz' % env.app_prefix


# ENVIRONMENTS
@task
def production():
    env.hosts = ['gorauskas.org']
    env.config_artifact = '%s.prod.nginx' % env.app_prefix
    env.open_port = False
    env.app_port = ''


@task
def testing():
    env.hosts = ['typhoon']
    env.config_artifact = '%s.test.nginx' % env.app_prefix
    env.open_port = True
    env.app_port = '8060'


# DEPLOY LOGIC
@task
def deploy():
    print blue(' ### Deploying %(app_name)s to %(host)s as %(user)s' % env)

    pack()
    push_code()
    deploy_code()

    if env.open_port:
        openport()

    reload()
    clean()


def pack():
    print green(' --- Package code')
    local('tar -zcf %s %s/' % (env.code_artifact, env.app_prefix),
          capture=False)


def push_code():
    print green(' --- Push artifacts to server')
    put(env.code_artifact, '%s/%s' % (env.remote_tmp_dir, env.code_artifact))
    put(env.config_artifact, '%s/%s.nginx' % (env.remote_tmp_dir,
                                              env.app_prefix))


def deploy_code():
    print green(' --- Deploy code')
    with cd(env.remote_web_dir):
        sudo('tar -zxf %s/%s -C %s' % (env.remote_tmp_dir, env.code_artifact,
                                       env.remote_web_dir))
        sudo('chown -R www-data:www-data %s/' % env.app_prefix)
        sudo('mv %s/%s.nginx %s/%s' % (env.remote_tmp_dir, env.app_prefix,
                                       env.remote_avail_dir, env.app_prefix))
        sudo('chown root:root %s/%s' % (env.remote_avail_dir, env.app_prefix))
        sudo('rm %s/%s; ln -s %s/%s %s/%s' %
             (env.remote_enab_dir, env.app_prefix, env.remote_avail_dir,
              env.app_prefix, env.remote_enab_dir, env.app_prefix))


def reload():
    print green(' --- Reload web server configuration')
    sudo('service nginx reload')


def clean():
    print green(' --- Cleanup packages')
    local('rm %s' % env.code_artifact, capture=False)
    sudo('rm %s/%s' % (env.remote_tmp_dir, env.code_artifact))


def openport():
    print green(' --- Open firewall port')

    with settings(warn_only=True):
        print green(' --- Checking if needed')
        result = local('nc -z -w 3 %s %s' % (env.host, env.app_port),
                       capture=True)

    if result.failed:
        print red(' --- opening port %(app_port)s for %(app_name)s' % env)
        sudo('iptables -I INPUT -p tcp --dport %s -j ACCEPT' % env.app_port)
    else:
        print blue(' --- Not needed; port already open')
