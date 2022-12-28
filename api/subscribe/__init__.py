import logging
import uuid
import json 


import os
import openai
import azure.functions as func


def main(req: func.HttpRequest, outputTable: func.Out[str]) -> func.HttpResponse:
    logging.info('createPage HTTP trigger function processed a request.')

    email = req.params.get('emailaddress')
    rowKey = str(uuid.uuid4())

    if email:
        data = {
            "emailaddress": f"{email}",
            "PartitionKey": "email",
            "RowKey": rowKey
        }

        # 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

        outputTable.set(json.dumps(data))
        
        try:
            openai.api_key = "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"
            openai.Completion.create(
            model="text-davinci-003",
            prompt="Schreibe ein expose for eine 40qm wohnung in Köln mit Garage",
            max_tokens=7,
            temperature=0
            )
        except: errorAI = "klappt nicht"

        return func.HttpResponse(
            f"Subscribed with {errorAI}!",
            status_code=201
        )
    else:
        return func.HttpResponse(
             "Please provide an emailaddress",
             status_code=400
        )
