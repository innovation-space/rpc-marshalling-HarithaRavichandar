import json


class RPCServer:
    def __init__(self):
        self.methods = {}

    def register_method(self, name, func):
        self.methods[name] = func

    def handle_request(self, request_json: str):
        request = json.loads(request_json)

        method_name = request.get("method")
        params = request.get("params")

        if method_name not in self.methods:
            return json.dumps({
                "status": "error",
                "message": "Method not found"
            })

        try:
            result = self.methods[method_name](params)
            return json.dumps({
                "status": "success",
                "result": result
            })
        except TypeError as e:
            return json.dumps({
                "status": "error",
                "message": str(e)
            })


class RPCClient:
    def __init__(self, server: RPCServer):
        self.server = server

    def call(self, method: str, params: dict):
        request = json.dumps({
            "method": method,
            "params": params
        })
        response = self.server.handle_request(request)
        return json.loads(response)
