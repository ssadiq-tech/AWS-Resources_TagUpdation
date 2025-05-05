import boto3
import os
from resource_arns import resource_arns  # importing the list from another file

# Initialize tagging client
client = boto3.client('resourcegroupstaggingapi')

# Tags to add/patch
tags_to_update = {
    'Environment': 'Production',
    'Owner': 'DevOps Team',
    'Project': 'CentralizedBackup'
}

# Patch tags for imported resources
response = client.tag_resources(
    ResourceARNList=resource_arns,
    Tags=tags_to_update
)

print("Tagging response:", response)
