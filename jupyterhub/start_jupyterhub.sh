docker run -d --name jupyterhub -p 8001:8000 \
	--network jupyterhub_network \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v /home/owen/Documents/jupyterhub/jupyterhub_logs:/logs \
	-v /home/owen/Documents/jupyterhub/jupyterhub_config:/srv/jupyterhub \
	dhso/jupyterhub:latest
