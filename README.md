# OpenTelemetry Collector Demo

This demo is a sample Python app to build the collector and exercise its tracing functionality.

To build and run the demo, first we will need to deploy the Python app and then the collector.

## Deploying the Python Application
#### 1. Create Docker image for Python app
`docker build -f Dockerfile.python . -t <name:tag>` <br/>
`docker push <name:tag>` <br/>

#### 2. Delete previous deployments
`kubectl delete -f python-deployment.yaml`<br/>

#### 3. Check deployment and related pods are deleted
`kubectl get deployments`<br/>
`kubectl get pods`<br/>

#### 4. Deploy
`kubectl apply -f python-deployment.yaml`<br/>

#### 5. Execute commands from container
`kubectl exec -it <name of pod> /bin/bash`<br/>

###### 6. Generate spans
Once you are in the container, run this command (Note: if the probability sampler is enabled in the otel-collector, you might not see all the spans you send.):
`curl http://localhost:5001`<br/>

Once that has been completed, it is time to deploy the collector.

## Deploying the Collector

#### 1. Create Docker image for collector
`docker build -t <name:tag> .` <br/>
`docker push <name:tag>` <br/>

#### 2. Delete previous deployments
`kubectl delete -f omsagent-otel.yaml`<br/>

#### 3. Check deployment and related pods are deleted
`kubectl get deployments`
`kubectl get pods`<br/>

#### 4. Update & Deploy
Go to omsagent-otel.yaml (in kubernetes folder), and update "image" for the otel-collector deployment to be the docker image you just built. Then, run:
`kubectl apply -f omsagent-otel.yaml`<br/>
