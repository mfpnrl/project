#script 1
import boto3 # This imports the boto3 library

dynamodb = boto3.client('dynamodb', region_name='us-east-2') # 


response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Food', # # defines a new attribute named 'Country'
            'AttributeType': 'S', # the data type of the attribute is string
        },
        {
            'AttributeName': 'Group',
            'AttributeType': 'S'
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'Food', # this will be partition key
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'Group', # this will be sort key
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
    TableName='Food_List', # sets the name of the table
)

#script 2
import boto3

# Create an instance of the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Specify the table name
table_name = 'Food_List'

# Get a reference to the table
table = dynamodb.Table(table_name)

# Define the items to be added
items = [
    {
        'FoodID': '1',
        'Food': 'Apple',
        'Group': 'Fruit'
    },
     {
        'FoodID': '2',
        'Food': 'Banana',
        'Group': 'Fruit'
    },
     {
        'FoodID': '3',
        'Food': 'Chicken',
        'Group': 'Protein'
    },
     {
        'FoodID': '4',
        'Food': 'Turkey',
        'Group': 'Protein'
    },
     {
        'FoodID': '5',
        'Food': 'Pepper',
        'Group': 'Vegetable'
    },
     {
        'FoodID': '6',
        'Food': 'Onion',
        'Group': 'Vegetable'
    },
     {
        'FoodID': '7',
        'Food': 'Potato',
        'Group': 'Starches'
    },
     {
        'FoodID': '8',
        'Food': 'Bread',
        'Group': 'Starches'
    },
     {
        'FoodID': '9',
        'Food': 'Yogurt',
        'Group': 'Dairy'
    },
    {
        'FoodID': '10',
        'Food': 'Milk',
        'Group': 'Dairy'
    }
]

# Write items to the table in a batch
with table.batch_writer() as batch:
    for item in items:
        batch.put_item(Item=item)
        print(f"Added item: {item}")

print("Items added successfully.")

#script 3
import boto3

# Create an instance of the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Specify the table name
table_name = 'Food_List'

# Get a reference to the table
table = dynamodb.Table(table_name)

# Scan the table to retrieve all items
response = table.scan()

# Retrieve the items from the response
items = response['Items']

# Process the items
for item in items:
    print(item)
