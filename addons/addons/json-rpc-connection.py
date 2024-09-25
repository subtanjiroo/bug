# import urllib.request
# import json
# import random

# url = 'http://localhost:8069'
# username = 'agencycanhcam@gmail.com'
# password = 'odoo'
# db = 'CanhcamAgency'

# def json_rpc(url, method, params):
#     data = {
#         "jsonrpc": "2.0",
#         "method": method,
#         "params": params,
#         "id": random.randint(0, 1000000)  # Random ID for request
#     }
#     headers = {"Content-Type": "application/json"}

#     req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers=headers)

#     with urllib.request.urlopen(req) as response:
#         response_data = json.loads(response.read().decode("UTF-8"))

#     if 'error' in response_data:
#         raise Exception(response_data["error"])
    
#     return response_data["result"]

# def call(url, service, method, *args):
#     return json_rpc(url, method="call", params={"service": service, "method": method, "args": args})

# # Correct URL for common service
# odoo_common_url = f'{url}/jsonrpc'

# # Login to get user_id
# user_id = call(odoo_common_url, "common", "login", db, username, password)

# vals = {
#     "name":"Property from json",
#     "sales_id":2,
# }

# create_property = call(odoo_common_url, "object", "execute", db, user_id, password, "estate.property", "create", vals)
# print(create_property)