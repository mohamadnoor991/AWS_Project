import boto3
import time



AWS_SQS_QUEUE_NAME = 'Mohamadsqs'
QueuResultName= "ServerQueue"
queueurlResultUrl= 'https://sqs.us-east-1.amazonaws.com/804385845436/ServerQueue'

clientSQS = boto3.resource('sqs')
queu = clientSQS.get_queue_by_name(QueueName=AWS_SQS_QUEUE_NAME)

msg = input("inter your 20 numbers ")
authorA=input("enter any personal ID ")

response = queu.send_message(MessageBody = msg,MessageAttributes={
 'Author': {
    'StringValue': authorA,
    'DataType': 'String' }

})


#### can canseble
queueResult = clientSQS.get_queue_by_name(QueueName=QueuResultName)

reciveResult = queueResult.receive_messages()
print('you will get the response soon.... ')
time.sleep(30)

for message in queueResult.receive_messages():
 print(message.body)
    
 if message.message_attributes is not None:
            author_name = message.message_attributes.get('Author').get('StringValue')
            if author_name == authorA:

                    print(message.body)
        ##


