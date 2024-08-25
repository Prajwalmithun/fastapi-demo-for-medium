# This is main branch 

# warehouse-fastAPI-microservice 

Pre-requisites:
- Docker Desktop
- Minikube
- Kubectl
- Git
- gcloud

## Deploy to minikube

Get the IP of the minikube cluster

1. Create a minikube cluster 
```
# minikube start
```
2. Create k8s resources
```
# kubectl apply -f k8s-manifest/deployment.yaml
# kubectl apply -f k8s-manifest/service.yaml
# minikube service warehouse-fastapi-microservice
```

Default username and password for Grafana is 
```
admin/prom-operator
```

## Deploy to GKE 

### Build and push the docker image to Artifact Registry

* Authenticate Google Artifact Registry
```
# gcloud auth configure-docker us-west1-docker.pkg.dev
```

* Tagging the local docker image
```
# docker tag SOURCE-IMAGE LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG
```

Eg: 
```
# docker tag prajwal3498/warehouseapi:latest us-west1-docker.pkg.dev/<project-id>/
python-repo/warehouseapi:amd64 
```

* Push the docker image to Artifact Registry
```
# docker push LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE
```
Eg:
```
# docker push us-west1-docker.pkg.dev/<project-id>/python-repo/warehouseapi:amd64
```


### GKE cluster

* Create a GKE cluster
```
gcloud container clusters create-auto gke-cluster-01 --location=us-west1
```

* Authenticate kubectl with GKE cluster
```
gcloud container clusters get-credentials gke-cluster-01 --region <region> --project <project-id>
```
* Verifify using the kubectl command 
```
kubectl get nodes
```
Wait till you see the status as Ready

* Create k8s resources
```
kubectl apply -f k8s-manifest/gke/deployment.yaml
kubectl apply -f k8s-manifest/gke/service.yaml
```

* Get the external IP of the service
```
kubectl get svc
```

* Access the service using the external IP
```
http://<external-ip>:6789/docs
```

