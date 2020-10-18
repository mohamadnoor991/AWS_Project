import boto3
from sys import argv


class main():

    sqs = boto3.resource('sqs')

    req_Queue = sqs.create_queue(QueueName='requestQueue', Attributes={'DelaySeconds': '2'})
    res_Queue = sqs.create_queue(QueueName='responseQueue', Attributes={'DelaySeconds': '2'})

    # Get the queue
    requestQueue = sqs.get_queue_by_name(QueueName='requestQueue')
    responseQueue = sqs.get_queue_by_name(QueueName='responseQueue')

    list_of_nb = str(input("""please enter a set of numbers, 'seperated by space! : """))
    # TODO in case of entring string 
    num = list_of_nb.split()
    if len(num) <= 1:
        print('Please, try to insert two number at least!')
    else:
        
        # Create a new message to be sent 
        req_smg = requestQueue.send_message(MessageBody=list_of_nb)
        while not (responseQueue.receive_messages()):
            print("Wait for response . . . .")
            answer_msg = responseQueue.receive_messages().body
            print(answer_msg)
            break



if __name__ == "__main__":
    main = main()
