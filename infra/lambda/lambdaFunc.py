import json
import boto3
from decimal import Decimal

# Custom JSON encoder for Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)  # Convert Decimal to int
        return super(DecimalEncoder, self).default(obj)

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresume-test')

def lambda_handler(event, context):
    # Fetch current views
    response = table.get_item(Key={'id': '0'})

    # Check if item exists, otherwise initialize views to 0
    if 'Item' in response:
        views = response['Item'].get('views', 0)
    else:
        views = 0

    # Ensure views is an integer (handle Decimal type)
    views = int(views) if isinstance(views, Decimal) else views

    # Increment the view count
    views += 1

    # Update the table with new views count
    table.put_item(Item={'id': '0', 'views': views})

    # Return a valid JSON response using custom DecimalEncoder
    return {
        'statusCode': 200,
        'body': json.dumps({'views': views}, cls=DecimalEncoder)
    }
