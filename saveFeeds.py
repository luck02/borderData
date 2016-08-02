import json
import feedparser
import boto3
import time
import schedule


def save_border_feed_data():
    print('***************************** starting ******************************************')
    feed_data = feedparser.parse('http://apps.cbp.gov/bwt/customize_rss.asp?portList=070801,300401,300402,300403,090104,090101,090102,090103,011501,011503,011502,071201,020901,380001,380002,021201,010601,360401,010401,302301,010901,070401,021101,070101,340101,380201,380301,300901,331001,250201,535501,535504,535503,535502,250301,250302,240601,230201,260101,230301,230302,240201,240202,240204,240203,240401,l24501,230503,230501,230502,230401,230402,230403,230404,260201,260301,260401,260402,260403,250602,250601,250603,240301,230902,230901,230701,231001,260801,260802,250401,250407,240801,250501&lane=all&action=rss&f=html')
    print(feed_data)

    client = boto3.client('s3')

    timestamp = time.time()
    bucketDate = time.strftime('%Y-%m-%d', time.gmtime())

    response = client.put_object(
        ACL='private',
        Body=json.dumps(feed_data),
        Bucket='border-wait-times',
        CacheControl='string',
        ContentDisposition='string',
        ContentEncoding='string',
        ContentLanguage='string',
        # ContentLength=123,
        # ContentMD5='string',
        ContentType='json',
        # Expires=datetime(2015, 1, 1),
        # GrantFullControl='string',
        # GrantRead='string',
        # GrantReadACP='string',
        # GrantWriteACP='string',
        Key='usBorder/' + bucketDate + '/' + str(timestamp),
        # Metadata={
        #    'string': 'string'
        # },
        # ServerSideEncryption='AES256'|'aws:kms',
        # StorageClass='STANDARD'|'REDUCED_REDUNDANCY'|'STANDARD_IA',
        # WebsiteRedirectLocation='string',
        # SSECustomerAlgorithm='string',
        # SSECustomerKey='string',
        # SSEKMSKeyId='string',
        # RequestPayer='requester'
    )
    print(response)
    print('*********************** complete *****************************')

schedule.every(10).minutes.do(save_border_feed_data)


while True:
    schedule.run_pending()
    time.sleep(30)
