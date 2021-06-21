https://aws.amazon.com/de/getting-started/hands-on/serve-a-flask-app/
```
bash
aws lightsail create-container-service --service-name flask-service --power small --scale 1

# before executing check https://lightsail.aws.amazon.com/ls/webapp/home/containers
# if the container is ready, continue

aws lightsail push-container-image --service-name flask-service --label flask-container --image flask-container
```

Heureka :)

```
bash
aws lightsail delete-container-service --service-name flask-service

```