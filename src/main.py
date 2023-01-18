import functions_framework
from openfunction.function_runtime import OpenFunctionRuntime

def hello_world(event, context):
    runtime = OpenFunctionRuntime.parse(context)
    runtime.send("Hello World!", "async-output")

    return "2. Hello World!"

