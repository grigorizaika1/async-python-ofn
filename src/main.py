import json
import functions_framework
from functions_framework.event_conversion import marshal_background_event_data
from functions_framework.background_event import BackgroundEvent
from openfunction.function_runtime import OpenFunctionRuntime
from openfunction.function_context import FunctionContext
from openfunction.dapr_output_middleware import dapr_output_middleware

from mqtt_check import message_mqtt

# @functions_framework.event
# def hello_world(event, context):
#     message_mqtt()

#     # runtime = OpenFunctionRuntime.parse(context)
#     # runtime.send("Hello World!", "async-output")

#     return "2. Hello World!"

# @functions_framework.http
def hello_world(request):
    message_mqtt()

    try:
        # request_dict = request.__dict__.copy()
        # response_data = {
        #     attr: str(value)
        #     for attr, value in request_dict.items() 
        #     if attr in ["args", "cookies", "headers", "environ", "form", "json", "values"]
        # }

        # event_data = marshal_background_event_data(request)
        # event = BackgroundEvent(**event_data)
        # context = FunctionContext(**event.context)
        # runtime = OpenFunctionRuntime.parse(context)
        # runtime.send("Hello World!!!", "async-output")

        response_data = {
            "message": "Success?",
            "data": {
                # "outputs": str(runtime.context.outputs)
                # "event_data": str(event_data)
            }
        } 
    except Exception as e:
        response_data = {"error": str(e)}

    return response_data

    # return json.dumps(response_data)