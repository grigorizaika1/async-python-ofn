import json

def hello_world(request):
    response_data = {
        "message": "hello, world",
        "form": request.form,
        "data": request.data,
        "args": str(request.args)
    }
    
    return json.dumps(response_data)
