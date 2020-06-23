# Integrating OpenTelemetry with Azure Monitor

#### Create Docker image for Python app
`<docker build -f Dockerfile.python . -t <name:tag>>` <br/>
`<docker push <name:tag>>` <br/>

#### Delete previous deployments
`<kubectl delete -f python-deployment.yaml>`<br/>

#### Execute commands from container
`<kubectl exec -it <name of pod> /bin/bash>`<br/>
