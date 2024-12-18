class conpteBancaire:

    # Constructeur pour initialiser les attributs a l'objet
    def __init__(self, titulaire, solde_initial=0):
        self.__titulaire = titulaire
        self.__solde_initial = solde_initial

    # methode pour afficher les infos du compte
    def afficher_infos(self):
        print(f"\nTitulaire: {self.__titulaire}")
        print(f"Solde initial: {self.__solde_initial} Dh\n")

    # methode pour deposer de l'argent dans le compte
    def deposer(self, montant):

        # l'utilisateur doit entrer un montant positif
        if montant > 0:
            self.__solde_initial += montant # self.__solde_initial = self.__solde_initial + montant
            print(f"Montant deposé: {montant} Dh")
        else:
            print("Montant invalide.")

    # methode pour retirer de l'argent du compte
    def retirer(self, montant):
        # l'utilisateur doit entrer un montant positif
        if montant > 0:
            if montant <= self.__solde_initial:
                self.__solde_initial -= montant # self.__solde_initial = self.__solde_initial - montant
                print(f"Montant retiré: {montant} Dh")
            else:
                print("Solde insuffisant.")
        else:
            print("Montant invalide.")

    # Méthode pour retourner le solde (si nécessaire ailleurs)
    def get_solde(self):
        return self.__solde
    
#methode pour intéragir avec l'utilisateur
def gestion_compte():
    # Demander à l'utilisateur de saisir le nom du titulaire et le solde initial
    titulaire = input("Entrez le nom du titulaire: ")
    solde_initial = float(input("Entrez le solde initial: "))
    # Créer un objet compte bancaire avec les informations saisies
    compte = conpteBancaire(titulaire, solde_initial)

    # Boucle tanque pour permettre à l'utilisateur de réaliser des opérations sur le compte
    while True:
        print("\nQue souhaitez-vous faire ?")
        print("1. Afficher les informations du compte")
        print("2. Déposer de l'argent")
        print("3. Retirer de l'argent")
        print("4. Quitter")

        choix = input("Entrez votre choix: ")

        # Traiter le choix de l'utilisateur
        if choix == "1":
            compte.afficher_infos()

        elif choix == "2":
                try:
                    montant = float(input("Entrez le montant à déposer: "))
                    compte.deposer(montant)
                except ValueError:
                    print("Montant invalide. veuillez entrer un montant valide.")

        elif choix == "3":
                try:
                    montant = float(input("Entrez le montant à retirer: "))
                    compte.retirer(montant)
                except ValueError:
                    print("Montant invalide. veuillez entrer un montant valide.")
        
        elif choix == "4":
            print("Au revoir! merci d'avoir utilisé notre service.")
            break

        else:
            print("Choix invalide. Veuillez entrer un choix valide.")

# Afficher le solde actuel du compte
def programme_principal():
    while True:
        print("\nVoulez-vous commencer à utiliser le système bancaire ?")
        print("1. Commencer")
        print("2. Quitter complètement")
        choix = input("Entrez votre choix (1 ou 2) : ")

        if choix == "1":
            comptes = gestion_compte()
        elif choix == "2":
            print("Merci d'avoir utilisé notre système bancaire. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")

programme_principal()