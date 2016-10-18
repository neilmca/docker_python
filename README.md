# docker_python

development python docker container

1. Setup cmd line environment
	docker-machine env --shell cmd my-newmachine
	@FOR /f "tokens=*" %i IN ('docker-machine env my-newmachine') DO @%i

2. Create image from docker file
	docker build -t neilmca/python-webapp2 .

3. Get IP address of machine
	docker-machine ip my-newmachine

3. Run image
	docker run -p 8080:8080 -d neilmca/python-webapp2

4. Inspect logs
	docker logs 3f87bc11a1c4

