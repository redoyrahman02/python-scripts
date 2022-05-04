import json
import boto3
from botocore.exceptions import ClientError


def sendEmail(event, context):

    fromName = event['Records'][0]['messageAttributes']['fromName']['stringValue']
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    if fromName:
        SENDER = fromName + "<no-reply@deenconnect.io>"
    else:
        SENDER = "DeenConnect<no-reply@deenconnect.io>"

    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = event['Records'][0]['messageAttributes']['email']['stringValue']

    # Specify a configuration set. If you do not want to use a configuration
    # set, comment the following variable, and the
    # ConfigurationSetName=CONFIGURATION_SET argument below.
    # CONFIGURATION_SET = "ConfigSet"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-1"

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    # The subject line for the email.
    SUBJECT = event['Records'][0]['messageAttributes']['subject']['stringValue']

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = event['Records'][0]['messageAttributes']['message']['stringValue']

    # The HTML body of the email.
    BODY_HTML = event['Records'][0]['messageAttributes']['message']['stringValue']

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION)

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,

        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!"
    }

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    
    """
