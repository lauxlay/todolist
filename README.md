# Local

## Local with postgres container 

### Requirements 
* Python 3.7.5
* Docker

### Execution 

1. Launch postgres container `docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres`

2. Go to env folder then activate the virtualenv `source bin/activate` (dev) will appear before the prompt

You can now run the script entrypoint.sh

### Test

run `sh request.sh $HOST`. (Ex : sh request.sh 35.239.83.105)

## Local with Minikube (k8s)

### Requirements 
* Registry private
* Minikube
* Kubectl 

### Execution

1. Build the Dockerfile and push the image to a registry (Docker, GCR, ECR, ...)
2. Start Minikube with `minikube start`
3. Run `kubectl -n todolist apply -k kustomize/overlays/dev`

### Test

Run `kubectl -n todolist port-forward svc/todolist 8080` then do the same test as for "Local with postgres container"

# Cloud platform

## Google Cloud Platform

### Requirements
* Terraform 
* Registry private
* gcloud
* Kubectl
 
### Terraform (version >= 0.14.3)

1. Go to terraform folder
2. Run `terraform init`
3. Run `terraform plan -output plan.out` and then `terraform apply plan.out`
4. To connect to the created cluster run `gcloud container clusters get-credentials todolist-302506-gke --region=us-central1`

### Deploy Kustomize

To deploy the project I use kustomize because it's full integrated with kubectl and Helm is to big for our usage.

1. Create a namespace `kubectl create ns todolist`
2. Run `kubectl -n todolist apply -k kustomize/overlays/test`
3. Get the service of the todolist with `kubectl -n todolist get svc`

### Test

1. Run `sh request.sh $(kubectl -n todolist get svc | grep todolist | awk '{ print $4 }')`

# API Route

/api/actuator : test URL (GET)
/api/todos    : todos (GET, POST)