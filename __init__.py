import json
import azure.functions as func
import requests  # proves requirements.txt was installed

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"ok": True, "requests_version": requests.__version__}),
        mimetype="application/json",
        status_code=200
    )
