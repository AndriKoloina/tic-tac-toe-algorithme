import pickle
from agent import *
from environment import *

class Jeu_Humain:

    def __init__(self):
        self.agent = Agent()
        self.env = Environnement()

        with open("q_tables.pkl", "rb") as fichier:
            self.agent.q_table = pickle.load(fichier) 

        self.agent.epsilon = 0.0

    def lancer_partie(self):
        self.env.reset()

        joueur_actuel = "X"

        for _ in range(9):
            action_valide = self.env.mouvement_valide()

            if joueur_actuel == "X":
                coup = int(input("Entrer votre choix de case"))
                while coup not in action_valide:
                    coup = int(input("Rechoisissez votre coup parmis {}".format(action_valide)))

                self.env.jouer_coup(coup, joueur_actuel)
                self.env.afficher_plateau(self.env.player_x, self.env.player_o)
                if self.env.verification_victoire(self.env.player_x) is True:
                    print("Vous avez gagner")
                    break

            else:
                etat_actuel = self.agent.encodage_etat(self.env)
                coup = self.agent.choix_action(etat_actuel, action_valide)
                self.env.jouer_coup(coup, joueur_actuel)
                self.env.afficher_plateau(self.env.player_x, self.env.player_o)

                if self.env.verification_victoire(self.env.player_o) is True:
                    print("Vous avez perdu")
                    break

            if self.env.match_null is True:
                break

            joueur_actuel = "O" if joueur_actuel == "X" else "X"

if __name__ == "__main__":
    jeu = Jeu_Humain()
    jeu.lancer_partie()
            

                