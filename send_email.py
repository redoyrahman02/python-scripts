import boto3

def send_email(to_address, subject, body):
    # Create an SES client
    client = boto3.client('ses')

    # Send the email
    response = client.send_email(
        Source='sender@example.com',
        Destination={
            'ToAddresses': [
                to_address,
            ]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': body
                }
            }
        }
    )
    
    return response
