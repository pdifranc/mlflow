from mlflow.gateway import MlflowGatewayClient

gateway_client = MlflowGatewayClient("http://localhost:5001")

routes = gateway_client.search_routes()

for route in routes:
   print(route)

route_name = route.name

def main():
    import json
    response = gateway_client.query(
        route_name, data = {
            'prompt': 'I believe the meaning of life is',
            'parameters': {
                "max_new_tokens": 64,
                "top_p": 0.9,
                "temperature": 0.4,
                "return_full_text": False
            }
        }
    )
    json_formatted = json.dumps(response, indent=1)
    print(json_formatted)


if __name__ == "__main__":
    main()
