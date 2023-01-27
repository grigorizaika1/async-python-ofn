def hello_world(request):
    return {
        "message": "hello, world",
        "form": request.form,
        "data": request.data,
        "args": request.args
    }
