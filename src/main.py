# import functions_framework
# from functions_framework.event_conversion import marshal_background_event_data
# from functions_framework.background_event import BackgroundEvent
# from openfunction.function_runtime import OpenFunctionRuntime
# from openfunction.function_context import FunctionContext
# from openfunction.dapr_output_middleware import dapr_output_middleware

from mqtt_check import message_mqtt

# @functions_framework.event
# def hello_world(event, context):
#     message_mqtt()

#     # runtime = OpenFunctionRuntime.parse(context)
#     # runtime.send("Hello World!", "async-output")

#     return "2. Hello World!"

# @functions_framework.http
def hello_world(request):
    # message_mqtt()

    # event_data = marshal_background_event_data(request)
    # event = BackgroundEvent(**event_data)
    # context = FunctionContext(**event.context)
    # runtime = OpenFunctionRuntime.parse(context)
    # runtime.send("Hello World!!!", "async-output")

    return "2. Hello World!"