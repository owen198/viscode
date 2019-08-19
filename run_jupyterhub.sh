docker run -p 8000:8000 -d --name jupyterhub \
	-v /home/owen/Documents/viscode/jupyter_data:/src/jupyterhub \
	-v /home/owen/Documents/viscode/jupyter_config:/srv/jupyterhub \
	-v /home/owen/Documents/viscode/jupyter_logs:/logs \
	jupyterhub/jupyterhub jupyterhub
