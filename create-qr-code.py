from fileinput import filename
import qrcode
import boto3

ACCESS_KEY_ID = 'AAAA'
SECRET_ACCESS_KEY = 'SER'

img = qrcode.make('https://give.deenfund.com/masjid-umme-hani')

filename = 'deenfund-masjid-umme-hani-florida-donate.png'

bucket = 'org-qr-codes-2022'


img.save(filename)

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID,
                  aws_secret_access_key=SECRET_ACCESS_KEY)

s3.upload_file(filename, bucket, filename)
# print(img.size)
