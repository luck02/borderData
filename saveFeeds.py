import json

import feedparser
import boto3
import time

d = feedparser.parse('http://apps.cbp.gov/bwt/customize_rss.asp?portList=070801,300401,300402,300403,090104,090101,090102,090103,011501,011503,011502,071201,020901,380001,380002,021201,010601,360401,010401,302301,010901,070401,021101,070101,340101,380201,380301,300901,331001,250201,535501,535504,535503,535502,250301,250302,240601,230201,260101,230301,230302,240201,240202,240204,240203,240401,l24501,230503,230501,230502,230401,230402,230403,230404,260201,260301,260401,260402,260403,250602,250601,250603,240301,230902,230901,230701,231001,260801,260802,250401,250407,240801,250501&lane=all&action=rss&f=html')
print(d)



# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('RawUSBorderRss')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)


table.put_item(
   Item={
        'ScrapeTime': time.time(),
        'data': json.dumps(d)
    }
)