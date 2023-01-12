import json
import boto3

# Connect to DynamoDB resource
dynamodb = boto3.resource('dynamodb')
# Select the table within DynamoDB
table = dynamodb.Table('cloud-resume-challenge')

def lambda_handler(event, context):
    # Get the record with id '0'
    response = table.get_item(Key={
       'record_id':'0'
    })
    # Convert record_count and record_id to strings
    record_count_str = str(response['Item']['record_count'])
    record_id_str = str(response['Item']['record_id'])
    # Return the record count and id
    return {
        "statusCode": 200,
        "body": json.dumps({
            "count": record_count_str,
            "id": record_id_str
        }),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
        }
    }


"""
This code combines the two pieces of code.
Retrieving the item from the DynamoDB table and
returning the record_count value in the response body as a JSON string,
along with the appropriate HTTP headers for CORS.
"""
"""
import json
import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('cloud-resume-challenge')

def lambda_handler(event, context):
    response = table.get_item(Key={
       'record_id':'0'
    })
    return response['Item']['record_count']

"""
