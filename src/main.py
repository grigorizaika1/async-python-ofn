import functions_framework

@functions_framework.event
def hello_world(event, context):
    return "Hello World!"