try:
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

# Variable global pour les noms des queues d'entrée et de sortie.
AWS_SQS_QUEUE_NAME_INPUT = "Inbox"
AWS_SQS_QUEUE_NAME_OUTPUT = "Outbox"
AWS_S3_BUCKET ="mybucket307991"

class worker(object):

    def __init__(self):
        try:
            # Create the queue. This returns an SQS.Queue instance
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

   #Fonction du process
    #TO DO
    def process(self,keyname):
        newkeyname ="processed"
        #return newkeyname
        I = skimage.color.rgb2gray(Image);
        I = I / np.max(I);
        I2 = exposure.adjust_gamma(I, gamma);
        return I2


    def logFile(self):
        # création de l'objet logger qui va nous servir à écrire dans les logs
        logger = logging.getLogger()
        # on met le niveau du logger à DEBUG, comme ça il écrit tout
        logger.setLevel(logging.DEBUG)

        # création d'un formateur qui va ajouter le temps, le niveau
        # de chaque message quand on écrira un message dans le log
        formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
        # création d'un handler qui va rediriger une écriture du log vers
        # un fichier en mode 'append', avec 1 backup et une taille max de 1Mo
        file_handler = RotatingFileHandler('activity.log', 'a', 1000000, 1)
        # on lui met le niveau sur DEBUG, on lui dit qu'il doit utiliser le formateur
        # créé précédement et on ajoute ce handler au logger
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # création d'un second handler qui va rediriger chaque écriture de log
        # sur la console
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG)
        logger.addHandler(stream_handler)

        # Après 3 heures, on peut enfin logguer
        # Il est temps de spammer votre code avec des logs partout :
        logger.info('Log file ')
        logger.warning('Testing %s', 'foo')


if __name__ == "__main__":
    # Get the service resource
    sqs = boto3.resource('sqs')
    #s3 = boto3.resource('s3')
    print("You are connected to the AWS service ...")
    q = worker()
    while True :
        print("waiting for message ...")
        time.sleep(0.5)
        for keyname in q.inputqueue.receive_messages():
            time.sleep(0.5)
            print(keyname.body)
	    Image=skimage.io.imread('Moon.jpg')
    	    plt.imshow(Image,cmap='gray')
    	    Image.shape
            plt.show();
            #li = q.transIntoList(str(message.body))
            I2 = q.process("Moon.jpg")
            plt.imshow(I2);
            plt.show();
            print("The image is processed !! ")
            q.send("imageProcessed")
            keyname.delete()
