# Integrating OpenTelemetry with Azure Monitor

#### Create Docker image for Python app
`docker build -f Dockerfile.python . -t <name:tag>` <br/>
`docker push <name:tag>` <br/>

#### Delete previous deployments
`kubectl delete -f python-deployment.yaml`<br/>

#### Check deployment and related pods are deleted
`kubectl get deployments`
`kubectl get pods

#### Deploy
`kubectl apply -f python-deployment.yaml`<br/>

#### Execute commands from container
`kubectl exec -it <name of pod> /bin/bash`<br/>

###### Generate spans
`curl http://localhost:5001`<br/>

###### Check what python app is doing 
`kubectl logs <name of pod>`

*same process for deploying collector, except with ot-ai.yaml*
