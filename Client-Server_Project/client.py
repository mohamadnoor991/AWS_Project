import boto3


AWS_SQS_QUEUE_NAME = 'Mohamadsqs'
clientSQS = boto3.resource('sqs')
queu = clientSQS.get_queue_by_name(QueueName=AWS_SQS_QUEUE_NAME)

msg = input("inter your 20 numbers ")

response = queu.send_message(MessageBody = msg)
print("your message id is "+ response['MessageId'])


