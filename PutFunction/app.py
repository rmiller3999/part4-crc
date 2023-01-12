import json
import boto3

# Connect to DynamoDB resource
dynamodb = boto3.resource('dynamodb')
# Select the table within DynamoDB
table = dynamodb.Table('cloud-resume-challenge')
#

def lambda_handler(event, context):
    # Get the record with id '0'
    response = table.get_item(Key={
        'record_id':'0'
    })
    # Increment the record count
    record_count = response['Item']['record_count']
    # Update the record count in the record
    record_count = record_count + 1
    print("visitors:", record_count)

    response = table.put_item(Item={
        'record_id':'0',
        'record_count': record_count
    })

    # Convert the record_count variable to a string or an integer
    record_count_str = str(record_count)
    # record_count_int = int(record_count)

    # Return the response object with the appropriate headers set
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Records added successfully!",
            "count": record_count_str
        }),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        }
    }

#This will allow any origin to make cross-origin requests to this Lambda function, using any method and any headers.

"""
def lambda_handler(event, context):
# Get the record with id '0'
    response = table.get_item(Key={
            'record_id':'0'
    })
# Increment the record count
    record_count = response['Item']['record_count']
# Update the record count in the record
    record_count = record_count + 1
    print("Visitors:",record_count)

    response = table.put_item(Item={
            'record_id':'0',
            'record_count': record_count
    })

    return "Records added successfully!"
"""
