# Readme of Part1 : description to launch.

To launch the application you had to launch the 2 programs of the application (client.py and EserverEC2):

1 / Execute the client.py with the command "python3 client.py" or if you have pycharm you can directly execute the code of the program.

Once the client is up and running you can choose to either send your integer list separated by commas by typing '1' on the command line, and the program sends this list to the SQS (InputQueue) of the AWS, and it waits the response which will retrieve it through the SQS (OutputQueue) thanks to the Worker.

2 / Execute serverEC2.py with the command "python3 serverEC2.py" or if you have pycharm you can directly execute the program code.

Once the worker is executed, it waits for the list to process through the SQS (InputQueue) of the AWS, as soon as it receives the message, it converts it into a real list with real integers, and it proceeds to obtain the Min and Max, the median and also the average. Then it sends these results to the client through the SQS (OutputQueue) and it creates a log file concerning this step of the prcess and it sends this file to the S3 of the AWS.

As soon as the client receives the result, it displays it in the command line, and it tells you to send the new list to be processed again or to quit the program by typing '2' on the command line


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Readme of Part2 : description to launch.

To launch the application you had to launch the 2 programs of the application (client.py and serverEC2.py).

1 / Execute the client.py with the command "python3 client.py" or if you have pycharm you can directly execute the code on the terminal or use  the command line.
First of all  the client.py will get connected to your aws account ,then it will ask you if whether you want to process an image by pressing 1 or to exit by pressing 2 ,once you type 1,it will ask you  to provide the image and there you should type the image name in  your desktop folder and here you should write its name with the full extension ,then he will ask about the name you want to give her in S3 bucket ( Keyname) of the image . Then the image will be sent to the (inbox) and to the worker (EC2 server)to be processed.

2 / Execute serverEC2.py with the command "python3 serverEC2.py" or if you have pycharm you can directly execute the program code or also this time use your command line.
Once the worker is executed, it takes the image from the bucket S3 and then processed it, Then it sends these results to the bucket S3 and  to the client through the SQS (Outbox) where you will find the imagename+’processed’ and it then the client will print the message that your processed image is : imagename+’processed’.
Once this message is printed ,the client has then the possibility to download the processed image in the S3 bucket, then the client can display again its command line, to ask whether you want to enter a new  image to be processed again or to quit the program by typing '2' on the command line.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Version francaise.
# Readme de la Parti 1 : description pour lancer l'application.

Pour lancer l'application vous devait lancer les 2 programmes de l'application : 

1/ Executer le client.py  avec la commande "python3 client.py" ou si vous avez pycharm vous pouvez executer direcetment le code du programme.

Une fois le client est lancer vous pouver choisir soit d'envoyer votre list d'entier separer par des virgules en tapant '1' sur la ligne de commande,  et le programme envoi cette liste au SQS (InputQueue) du AWS, et il attend la reponse qui va le recupere à traver le SQS (OutputQueue) grace au Worker.

2/Executer le serverEC2.py avec lacommande "python3  serverEC2.py " ou si vous avez pycharm vous pouvez executer direcetment le code du programme.

Une fois le worker est executer il attend la liste a procedcer à travers le SQS (InputQueue) du AWS, dés qu'il recoit le message, il le converti en list réel avec des vrais entier, et il proces a fin d'avoir le Min et le Max , la median et aussi la moyen. Aprés il envoi ces résulatat au client à travers le SQS (OutputQueue) et il crée un fichier log concernant cette etape du prcess et il envoi ce fichier au S3 du AWS.

Dés que le client recoi le résultat , il l'affiche dans la ligne decommande, et il vous repropose d'enoyer encore la nouvelle list a traiter ou de quitter le programme en tapant '2' sur la ligne de commande.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Version francaise
# Readme de la Parti 2 : description pour lancer l'application.

Readme of Part2: description à lancer.

Pour lancer l'application il fallait lancer les 2 programmes de l'application (client.py et serverEC2.py).
1/ Exécutez le client.py avec la commande "python3 client.py" ou si vous avez pycharm vous pouvez directement exécuter le code sur le terminal ou utiliser la ligne de commande.

Tout d'abord, client.py se connectera à votre compte aws, puis il vous demandera si vous souhaitez traiter une image en appuyant sur 1 ou pour quitter en appuyant sur 2, une fois que vous avez tapé 1, il vous demandera de fournir le image et là, vous devez taper le nom de l'image dans votre dossier de bureau et ici, vous devez écrire son nom avec l'extension complète, puis il vous demandera le nom que vous souhaitez lui donner dans le compartiment S3 (Keyname) de l'image. Ensuite, l'image sera envoyée à la (boîte de réception) et au travailleur (serveur EC2) pour être traitée.

2/ Exécutez serverEC2.py avec la commande "python3 serverEC2.py" ou si vous avez pycharm vous pouvez directement exécuter le code du programme ou aussi cette fois utiliser votre ligne de commande.

Une fois que le worker est exécuté, il prend l'image du bucket S3 puis la traite, puis il envoie ces résultats au bucket S3 et au client via le SQS (Outbox) où vous trouverez le nom de l'image + 'traité' et ensuite le client imprimera le message indiquant que votre image traitée est: nom_image + 'traitée'.
Une fois ce message imprimé, le client a alors la possibilité de télécharger l'image traitée dans le bucket S3, puis le client peut afficher à nouveau sa ligne de commande, pour demander si vous souhaitez saisir une nouvelle image à traiter à nouveau ou quitter le programme en tapant «2» sur la ligne de commande.





