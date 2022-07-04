from fileinput import filename
import boto3

s3 = boto3.client('s3')


################### CREATING A BUCKET ##################

# response = s3.create_bucket(
#     Bucket='vikrant1200vikrant',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'ap-northeast-1'
#     })

################# UPLOADING A FILE ################

sss = boto3.resource('s3')

data = open('index.html', 'rb')
sss.Bucket('vikrant1200vikrant').upload_file(Key='index.html', Filename= 'index.html' )
