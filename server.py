import boto3
    from botocore.exceptions import ClientError
    import botocore
    import os
    import sys
    import json
except Exception as e:
    print(e)
import time

import logging

import numpy as np
import skimage.io
import os
import matplotlib.pyplot as plt
from skimage import exposure
import numpy as np
import sys

AWS_SQS_QUEUE_NAME_INPUT = "Inbox"
AWS_SQS_QUEUE_NAME_OUTPUT = "Outbox"
AWS_S3_BUCKET ="mybucket307991"

class worker(object):

    def __init__(self):
        try:
            self.queue = sqs.create_queue(QueueName=AWS_SQS_QUEUE_NAME_OUTPUT)
        except Exception:
            print(e)
        # Get the queue
        self.inputqueue = sqs.get_queue_by_name(QueueName=AWS_SQS_QUEUE_NAME_INPUT)
        print("You are connected to the SQS service ...")

    def upload_image(Self,file_name, bucket, key_name):
        """Upload a file to an S3 bucket
        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        bucket = 'your-bucket-name'
        file_name = 'location-of-your-file'
        key_name = 'name-of-file-in-s3'
        s3 = boto3.client('s3')
        s3.upload_file(file_name, bucket, key_name)
        # Upload the image

        try:
            response = s3.upload_file(file_name, bucket, key_name)
        except ClientError as e:
            logging.error(e)
            # return False
        # return True

    def send(self, message=None):
        try:
            # Create the queue. This returns an SQS.Queue instance
            self.queue = sqs.create_queue(QueueName=AWS_SQS_QUEUE_NAME_OUTPUT)
        except Exception:
            print(e)
        # Create a new message
        response = self.queue.send_message(MessageBody=message)
        #self.upload_file("activity.log",AWS_S3_BUCKET,"logfile")
        print("The new keyname is sent to outbox queue !!")
        #self.logFile()
        return response

    def receive(self):
        try:
            queue = sqs.get_queue_by_name(QueueName=AWS_SQS_QUEUE_NAME_OUTPUT)
            print("You are connected to the response Queue ...")
            queue = self.resource.get_queue_by_name(QueueName=self.QueueName)
            for message in queue.receive_messages():
                data = message.body
                message.delete()
        except Exception:

            return []
        return data

    def transIntoList(self, message=None):
        # input comma separated elements as string
        str = message


        # conver to the list
        list = str.split(",")
        print("list: ", list)

        # convert each element as integers
        li = []
        for i in list:
            li.append(int(i))
        return li
        # print list as integers
        print("list (li) : ", li)

   #Function to process
    #TO DO
    def process(self,keyname):
        newkeyname ="processed"
        #return newkeyname
        I = skimage.color.rgb2gray(Image);
        I = I / np.max(I);
        I2 = exposure.adjust_gamma(I, gamma);
        return I2


   