import azure.functions as func

app = func.FunctionApp()

# @app.function_name(name="HttpTrigger1")
# @app.route(route="hello") # HTTP Trigger
# def test_function(req: func.HttpRequest) -> func.HttpResponse:
#     return func.HttpResponse("HttpTrigger1 function processed a request!!!")

@app.function_name(name="mytimer")
@app.schedule(schedule="0 */5 * * * *", arg_name="mytimer", run_on_startup=True,
              use_monitor=False) 
def test_function(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
