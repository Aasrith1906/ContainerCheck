
minikube docker-env 
docker build -t aasrith1906/cc-website-image:latest ./flask-app/
docker build -t aasrith1906/rest-api-image:latest ./rest-api/
docker push aasrith1906/cc-website-image:latest 
docker push aasrith1906/rest-api-image:latest
cd kubernetes 
kubectl create -f rest-api-deployment.yml --record 
kubectl create -f website-deployment.yml --record 
kubectl expose rest-api-deploy --type=NodePort 
kubectl expose cc-website-deploy --type=NodePort 
minikube service --url cc-website-deploy 
minikube service --rul rest-api-deploy 