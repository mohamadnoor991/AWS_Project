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
x=0
while x<=20:
 for message in queue.receive_messages(MessageAttributeNames=['Author']):
        
            author_name1 = message.message_attributes.get('Author').get('StringValue') 
    
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
            servermessage=  'the max number is: '+str(max)+'the min number is: '+str(min)+'the mean number is: '+str(mean)+'the median number is: '+str(median)
            responseResult = queueResult.send_message(MessageBody= servermessage,MessageAttributes={
            'Author': {
                'StringValue': author_name1,
                'DataType': 'String'
            }})
 x+=1   


