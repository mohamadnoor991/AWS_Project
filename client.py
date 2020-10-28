import boto3
import botocore.exceptions as bx
from sys import argv
import publicip
import logging
import time
import random

logFormat = "%(levelname)s   %(asctime)-15s %(filename)s[%(lineno)d] : %(message)s"
logging.basicConfig(level=logging.INFO,format=logFormat)

logger = logging.getLogger()




author  = ''

class main():
    def __init__(self):
        self.sqs = boto3.resource('sqs')
        logger.info("Starting AWS service SQS....")
        try:
            if not self.sqs.get_queue_by_name(QueueName='requestQueue'):
                self.request_Queue = self.sqs.create_queue(QueueName='requestQueue')
            else:
                print("The request queue is already exist!")
        except bx.ClientError as e:
            logger.debug(e)
            
    
