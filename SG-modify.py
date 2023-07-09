import boto3

# Replace the values with your AWS credentials and region
access_key = 'YOUR_ACCESS_KEY'
secret_key = 'YOUR_SECRET_KEY'
region_name = 'us-west-2'

# Replace the values with your security group details
security_group_id = 'YOUR_SECURITY_GROUP_ID'
protocol = 'tcp'
port_range_min = 80
port_range_max = 80
cidr_ip = '0.0.0.0/0'

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region_name
)

# Create a client for EC2
ec2_client = session.client('ec2')

# Add the inbound rule to the security group
response = ec2_client.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': protocol,
            'FromPort': port_range_min,
            'ToPort': port_range_max,
            'IpRanges': [
                {
                    'CidrIp': cidr_ip
                }
            ]
        }
    ]
)

# Check the response
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print('Inbound rule added successfully.')
else:
    print('Failed to add inbound rule.')
