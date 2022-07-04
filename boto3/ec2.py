import boto3

ec2 = boto3.client('ec2')

################# CREATE AN INSTANCE ################
response = ec2.run_instances(ImageId='ami-0f8048fa3e3b9e8ff',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    TagSpecifications=[
        {
            'ResourceType':'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Python-boto3'
                },
            ]
        },
    ])















# # response = s3.describe_instances('')

# # def start_ec_instances():
# #         global response
# #         response = s3.describe_instances(InstanceIds=['i-046c44579ac45959a'])
# #         # print(response)

# # start_ec_instances()

# response = s3.terminate_instances(InstanceIds=['i-046c44579ac45959a'])

# # print(type(response))
# # A1 = response['Reservations']
# # A2 = A1[0]
# # A3= A2['Instances']
# # b = A3[0]
# # print(b['State'])