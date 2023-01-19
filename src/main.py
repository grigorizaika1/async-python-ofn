import functions_framework
from openfunction.function_runtime import OpenFunctionRuntime
from mqtt_check import message_mqtt

@functions_framework.event
def hello_world(event, context):
    message_mqtt()

    # runtime = OpenFunctionRuntime.parse(context)
    # runtime.send("Hello World!", "async-output")

    return "2. Hello World!"

