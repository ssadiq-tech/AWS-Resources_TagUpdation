import boto3

client = boto3.client('resourcegroupstaggingapi')

# Filter by resource types
response = client.get_resources(
    ResourceTypeFilters=[
        'ec2:instance',
        's3:bucket',
        'dynamodb:table',
        'rds:db',
        'ec2:vpc'
    ]
)

# Extract ARNs
resource_arns = [resource['ResourceARN'] for resource in response['ResourceTagMappingList']]

print("Filtered Resource ARNs:", resource_arns)
