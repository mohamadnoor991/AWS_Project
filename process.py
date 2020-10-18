import boto3
from numpy import max, min, mean, median


sqs             = boto3.resource('sqs')

# Get the queue
requestQueue    = sqs.get_queue_by_name(QueueName='requestQueue')
responseQueue    = sqs.get_queue_by_name(QueueName='responseQueue')

numbers         = []
# while True:
#     print("waiting requests.............")
# Process messages by printing out body and optional author name
for message in requestQueue.receive_messages():
    rec_list_of_nb = message.body
    
    for nb in rec_list_of_nb.split():
        numbers.append(float(nb))

    print('Hello, {}!'.format(numbers))
    min     = min(numbers)
    max     = max(numbers)
    mean    = mean(numbers)
    median  = median(numbers)
    
    
    reply_msg   = """
        Min     = {}   
        Max     = {}   
        Mean    = {}   
        Median  = {}   """.format(min,max,mean,median)


    print(reply_msg)
    # Let the queue know that the message is processed
    res     = responseQueue.send_message(MessageBody=reply_msg)
    message.delete()
    