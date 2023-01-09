import boto3
import json 
import base64
import re
import time
import os

def lambda_handler(event, context):
    
    userid = event['headers']['userid']
    
    # Get the base64 encoded image from the event
    body_data = json.loads( event['body'] ) 
    
    encoded_image = body_data['image']
    env_data = body_data['env']
    
    param_name = f"{env_data.upper()}_BUCKET_NAME"
    
    bucket_name = os.getenv( param_name )
    
    ext = encoded_image.split(';')[0].split('/')[1]
    
    #clean the extra information at the start of the string
    cleaned_string = re.sub(r'^data:image\/\w+;base64,', '', encoded_image)
    
    try:
        # Decode the base64 encoded image
        decoded_image = base64.b64decode( cleaned_string , validate = True)
        current_time_epoch = int(time.time())
        image_key = f"{userid}/{current_time_epoch}.{ext}" 
        print( image_key)
        
        # Save the image to S3
        s3 = boto3.client('s3')
        s3.put_object(Bucket= bucket_name , Key=image_key, Body=decoded_image)
        
        # Return the URL of the uploaded image
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'applicaton/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': f"https://{bucket_name}.s3.ap-southeast-1.amazonaws.com/{image_key}"
        }
        
    except Exception as e:
        print( e )
        
    
    
