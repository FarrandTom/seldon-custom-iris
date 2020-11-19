from seldon_core.seldon_client import SeldonClient
import numpy as np

endpoint = "0.0.0.0:5001"

data = [
    [6.8,  2.8,  4.8,  1.4],
    [6.0,  3.4,  4.5,  1.6]
    ]

sc = SeldonClient(microservice_endpoint=endpoint)
response = sc.microservice(
    json_data = data,
    method='predict'
)

print(response.request)
print(response.response)