import json
import boto3
import os


def execute(event, context):

    serverId = os.environ['SERVER_ID']

    type = os.environ['TYPE']

    client = boto3.client('transfer')

    if(type == 'start'):
        response = client.start_server(
            ServerId=serverId
        )
    else:
        response = client.stop_server(
            ServerId=serverId
        )

    return response
