import MeetingObject

while(input != "exit"):
    print(" -= Voici la v1 de votre agenda prsonnel =- \n")
    print("1- Créer un évènement")
    print("2- Afficher un évènement")
    print("3- Modifier un évènement")
    print("4- Supprimer un évènement")
    task = input("Quelle action souhaitez-vous faire? En entrant 'exit' vous sortirez de votre agenda !")
    if (task == "exit"):
        exit
    elif(task == ""):
        MeetingObject.create
    else:
        print("Prout")