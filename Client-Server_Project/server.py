import boto3
import math
import statistics
AWS_SQS_QUEUE_NAME = "Mohamadsqs"
#queue for the results
QueuResultName= "ServerQueue"
sqs= boto3.resource('sqs')
#queue for the results
sqsResult = boto3.resource('sqs')

sqsurl= 'https://sqs.us-east-1.amazonaws.com/804385845436/Mohamadsqs'
#queue for the results
queueurlResultUrl= 'https://sqs.us-east-1.amazonaws.com/804385845436/ServerQueue'


queue = sqs.get_queue_by_name(QueueName=AWS_SQS_QUEUE_NAME)
queueResult = sqs.get_queue_by_name(QueueName=QueuResultName)

numberslist         = []
for message in queue.receive_messages():
    listnum = message.body

    # Processing the message from the client
    for nb in listnum.split():
        numberslist.append(float(nb))

    print('Sets of numbers received, {}!'.format(numberslist))

    # Clacutation phase
    min     = min(numberslist)
    max     = max(numberslist)
    mean    = statistics.mean(numberslist)
    median  = statistics.median(numberslist)
    print('the max number is: ',max,'the min number is: ',min,'the mean number is: ',mean,'the median number is: ',median ) 
    servermessage= "'the max number is: ',max,'the min number is: ',min,'the mean number is: ',mean,'the median number is: ',median"
    responseResult = queueResult.send_message(MessageBody= servermessage)