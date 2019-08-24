# Configuration file for Jupyter Hub

c = get_config()

# spawn with Docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# Spawn containers from this image
c.DockerSpawner.image = 'dhso/jupyter_lab_singleuser:latest'

# JupyterHub requires a single-user instance of the Notebook server, so we
# default to using the `start-singleuser.sh` script included in the
# jupyter/docker-stacks *-notebook images as the Docker run command when
# spawning containers.  Optionally, you can override the Docker run command
# using the DOCKER_SPAWN_CMD environment variable.
c.DockerSpawner.extra_create_kwargs.update({ 'command': "start-singleuser.sh --SingleUserNotebookApp.default_url=/lab" })

# Connect containers to this Docker network
network_name = 'jupyterhub_network'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
# Pass the network name as argument to spawned containers
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }

# Explicitly set notebook directory because we'll be mounting a host volume to
# it.  Most jupyter/docker-stacks *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention.
notebook_dir = '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = { '/home/owen/Documents/jupyterhub/jupyterhub_data/jupyterhub-user-{username}': notebook_dir }

# volume_driver is no longer a keyword argument to create_container()
# c.DockerSpawner.extra_create_kwargs.update({ 'volume_driver': 'local' })
# Remove containers once they are stopped
c.DockerSpawner.remove_containers = True
# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True

# The docker instances need access to the Hub, so the default loopback port doesn't work:
# from jupyter_client.localinterfaces import public_ips
# c.JupyterHub.hub_ip = public_ips()[0]
c.JupyterHub.hub_ip = '0.0.0.0'

# IP Configurations
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000


from oauthenticator.google import LocalGoogleOAuthenticator
c.JupyterHub.authenticator_class = LocalGoogleOAuthenticator
c.LocalGoogleOAuthenticator.oauth_callback_url = 'http://jupyterhub.viscode.org/hub/oauth_callback'
c.LocalGoogleOAuthenticator.client_id = ''
c.LocalGoogleOAuthenticator.client_secret = ''
c.LocalGoogleOAuthenticator.create_system_users = True
c.LocalGoogleOAuthenticator.login_service = 'Google'
# OAuth with GitHub
#c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'

#c.Authenticator.whitelist = whitelist = set()
#c.Authenticator.admin_users = admin = set()

c.Authenticator.whitelist = {'@gmail.com', '@gmail.com'}
c.Authenticator.admin_users = {'gmail.com'}
c.Authenticator.add_user_cmd = ['adduser', '-q', '--gecos', '""', '--disabled-password', '--force-badname']

#import os
#os.environ['GITHUB_CLIENT_ID'] = 'cf256bdf0e9f3cae70f0'
#os.environ['GITHUB_CLIENT_SECRET'] = '18b436c776a77931d07ed0de34c3e007d1364e2b'
#os.environ['OAUTH_CALLBACK_URL'] = 'http://jupyterhub.viscode.org/hub/oauth_callback'
#c.GitHubOAuthenticator.oauth_callback_url = 'http://jupyterhub.viscode.org/hub/oauth_callback'


c.JupyterHub.extra_log_file = '/logs/jupyterhub.log'
c.Application.log_datefmt = '%Y-%m-%d-%H:%M:%S'
c.Application.log_format = '|%(asctime)s|%(levelname)s|%(name)s|%(message)s|'
c.Application.log_level = 'INFO'
