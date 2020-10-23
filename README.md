# Readme of Part1 : description to launch.

To launch the application you had to launch the 2 programs of the application (client.py and EserverEC2):

1 / Execute the client.py with the command "python3 client.py" or if you have pycharm you can directly execute the code of the program.

Once the client is up and running you can choose to either send your integer list separated by commas by typing '1' on the command line, and the program sends this list to the SQS (InputQueue) of the AWS, and it waits the response which will retrieve it through the SQS (OutputQueue) thanks to the Worker.

2 / Execute serverEC2.py with the command "python3 serverEC2.py" or if you have pycharm you can directly execute the program code.

Once the worker is executed, it waits for the list to process through the SQS (InputQueue) of the AWS, as soon as it receives the message, it converts it into a real list with real integers, and it proceeds to obtain the Min and Max, the median and also the average. Then it sends these results to the client through the SQS (OutputQueue) and it creates a log file concerning this step of the prcess and it sends this file to the S3 of the AWS.

As soon as the client receives the result, it displays it in the command line, and it tells you to send the new list to be processed again or to quit the program by typing '2' on the command line


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Version francaise.

Pour lancer l'application vous devait lancer les 2 programmes de l'application : 

1/ Executer le client.py  avec la commande "python3 client.py" ou si vous avez pycharm vous pouvez executer direcetment le code du programme.

Une fois le client est lancer vous pouver choisir soit d'envoyer votre list d'entier separer par des virgules en tapant '1' sur la ligne de commande,  et le programme envoi cette liste au SQS (InputQueue) du AWS, et il attend la reponse qui va le recupere à traver le SQS (OutputQueue) grace au Worker.

2/Executer le serverEC2.py avec lacommande "python3  serverEC2.py " ou si vous avez pycharm vous pouvez executer direcetment le code du programme.

Une fois le worker est executer il attend la liste a procedcer à travers le SQS (InputQueue) du AWS, dés qu'il recoit le message, il le converti en list réel avec des vrais entier, et il proces a fin d'avoir le Min et le Max , la median et aussi la moyen. Aprés il envoi ces résulatat au client à travers le SQS (OutputQueue) et il crée un fichier log concernant cette etape du prcess et il envoi ce fichier au S3 du AWS.

Dés que le client recoi le résultat , il l'affiche dans la ligne decommande, et il vous repropose d'enoyer encore la nouvelle list a traiter ou de quitter le programme en tapant '2' sur la ligne de commande.
