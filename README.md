1) Build image for linux/amd64 and push it to Docker Hub.

docker buildx build --platform linux/amd64 -t therealsangwoohan/hello:latest --push .

2) Create hello-deployment

kubectl create -f kubernetes-manifests/hello-deployment.yaml

3) Create hello-service

kubectl create -f kubernetes-manifests/hello-service.yaml

4) Get the external ip and the port

kubectl get services