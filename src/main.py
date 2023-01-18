import functions_framework

@functions_framework.event
def hello_world(event, context):
    # context.logger.info("Event ID: %s", context.event_id) # this is a suggestion from copilot
    context.send("1. Hello World!")
    return "2. Hello World!"


