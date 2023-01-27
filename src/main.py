import json

def hello_world(request):
    response_data = {
        "message": "hello, world",
        "form": str(request.form),
        "data": str(request.data),
        "args": str(request.args)
    }
    
    return json.dumps(response_data)
