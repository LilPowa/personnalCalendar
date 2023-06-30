class MeetingObject:
    def __init__(self, name, dayMeeting, hourMeeting, minuteMeeting, timeMeeting, placeMeeting):
        self.name = name
        self.dayMeeting = dayMeeting
        self.hourMeeting = hourMeeting
        self.minuteMeeting = minuteMeeting
        self.timeMeeting = timeMeeting
        self.placeMeeting = placeMeeting

    def create(self):
        print("Vous avez choisi de créer un évènement, veuillez suivre les consignes afin de le créer\n")
        self.name = input("Choisissez un nom pour votre evenement : ")
        if (self.name != None): 
            self.dayMeeting = input("Choisissez un jour entre le 1 et le 31 : ")    
            if (self.dayMeeting != None & self.dayMeeting <= 31 & self.dayMeeting >= 1):
                self.hourMeeting = input("Choisissez une heure de début entre 0 et 24 : ")
                if (self.hourMeeting != None & self.hourMeeting <= 24 & self.hourMeeting >= 0):
                    self.minuteMeeting = input("Choisissez un nombre de minutes de pour votre rendez-vous, entre 0 et 59 : ")
                    if (self.minuteMeeting != None & self.minuteMeeting <= 59 & self.minuteMeeting >= 0):
                        self.timeMeeting = input("Indiquer une durée pour votre rendez-vous (en minutes, 2h = 120): ")
                        if (self.timeMeeting != None): 
                            self.placeMeeting = input("Indiquer le lieu du rendez-vous : ")
                            if(self.placeMeeting != None):
                                print("Votre rendez vous " + self.name + " est enregistré\n")
                                print("Vous avez donc rendez-vous le " + self.dayMeeting + " à " + self.hourMeeting + ":" + self.minuteMeeting+"\n")
                                print("Votre rendez-vous a une durée de " + self.timeMeeting+"\n")
                                print("Enfin, votre rendz-vous se trouve à l'adresse suivante : " + self.placeMeeting+"\n")
                            else:
                                exit
                        else:
                            exit
                    else:
                        exit
                else:
                    exit
            else:
                exit
        else:
            exit



    