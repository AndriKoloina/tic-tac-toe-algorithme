import pickle
from agent import *
from environment import *
import random

class Evaluation:

    def __init__(self):
        self.agent = Agent()
        self.env = Environnement()
        
        with open("q_tables.pkl", "rb") as fichier:
            self.agent.q_table = pickle.load(fichier) 

        self.agent.epsilon = 0.0

    def lancement_evaluation(self, nb_parties):
        nb_victoire_agent = 0
        nb_defaite = 0
        nb_match_null = 0

        for _ in range(nb_parties):
            self.env.reset()
            joueur_actuel = "X"
            match_terminer = False

            for j in range(9):
                
                etat_actuel = self.agent.encodage_etat(self.env)
                action_valide = self.env.mouvement_valide()

                if joueur_actuel == "X":
                   coup = self.agent.choix_action(etat_actuel, action_valide)
                   self.env.jouer_coup(coup, joueur_actuel)

                   if self.env.verification_victoire(self.env.player_x) is True:
                       nb_victoire_agent += 1
                       match_terminer = True
                       break

                else:
                   coup = random.choice(action_valide)
                   self.env.jouer_coup(coup, joueur_actuel)

                   if self.env.verification_victoire(self.env.player_o) is True:
                       nb_defaite += 1
                       match_terminer = True
                       break

                if self.env.match_null() is True:
                    nb_match_null += 1
                    match_terminer = True
                    break

                joueur_actuel = "O" if joueur_actuel == "X" else "X"

    
        print("Résultat de l'évaluation sur {}". format(nb_parties))
        print("Nombre de victoire : {} ({:1f} %)". format(nb_victoire_agent, (nb_victoire_agent) / (nb_parties) * 100))
        print("Nombre de défaite :{} ({:1f} %) ". format(nb_defaite, (nb_defaite) / (nb_parties) * 100))
                

if __name__ == "__main__":
    nombre_de_partie = 1000
    evaluation = Evaluation()
    evaluation.lancement_evaluation(nombre_de_partie)

