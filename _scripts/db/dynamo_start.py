import boto3

connection_str = "http://localhost:8888"
table_name = 'contacts'
driver = boto3.resource('dynamodb', endpoint_url=connection_str)

driver.create_table(
    TableName='Devices',
    KeySchema=[
        {
            'AttributeName': 'device_id',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'datacount',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'device_id',
            # AttributeType defines the data type. 'S' is string type and 'N' is number type
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'datacount',
            'AttributeType': 'N'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10  # WriteCapacityUnits set to 10 writes per second
    }
)
