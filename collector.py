import flask
import requests
import sys

from opentelemetry import trace
from opentelemetry.ext.flask import FlaskInstrumentor
from opentelemetry.ext.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.ext.opencensusexporter.trace_exporter import (
  OpenCensusSpanExporter,
)

my_port = 5001
# my_port = 0
# if len(sys.argv) > 1:
#     my_port = int(sys.argv[1])
# else:
#     print("need to specify port number as first parameter")

exporter = OpenCensusSpanExporter(
    service_name="basic-service-%s" % my_port, endpoint="otel-collector:55678"
)
trace.set_tracer_provider(TracerProvider())
span_processor = BatchExportSpanProcessor(exporter)
# span_processor = SimpleExportSpanProcessor(exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# forward_port = 5000
# forward_port = 0
# if len(sys.argv) > 2:
#     forward_port = int(sys.argv[2])

app = flask.Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.route("/")
# def hello():
#     tracer = trace.get_tracer(__name__)
#     with tracer.start_as_current_span("example-request"):
#         requests.get("http://www.example.com")
#     return "hello"

def pull_requests():
    # Fetch a list of pull requests on the opentracing repository
    github_url = "https://api.github.com/repos/opentracing/opentracing-python/pulls"
    r = requests.get(github_url)

    json = r.json()
    pull_request_titles = map(lambda item: item['title'], json)

    # if forward_port:
    #     requests.get("http://localhost:%s" % forward_port)

    return 'OpenTracing Pull Requests: ' + ', '.join(pull_request_titles)

app.run(debug=True, port=my_port)
