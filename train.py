from environment import *
from agent import *
import random
import pickle 

class Train:

    env = Environnement()
    agent = Agent()

    def episode(self):
        for i in range(20000):
            self.env.reset()
            joueur_actuel = random.choice(["X", "O"]) 

            for j in range(9):
                
                etat_actuel = self.agent.encodage_etat(self.env)
                action_valide = self.env.mouvement_valide()

                numero_case = self.agent.choix_action(etat_actuel, action_valide)

                verification_nouvelle_position = self.env.jouer_coup(numero_case, joueur_actuel)


                if verification_nouvelle_position is True:
                    recompense = 0
                    partie_finie = False

                    if self.env.match_null() is True:
                        recompense = 0.0
                        partie_finie = True
                        break
                    elif joueur_actuel == "X" and self.env.verification_victoire(self.env.player_x) is True:
                        recompense = 1.0
                        partie_finie = True
                        break
                    elif joueur_actuel == "O" and self.env.verification_victoire(self.env.player_o) is True:
                        recompense = 1.0
                        partie_finie = True
                        break


                etat_suivant = self.agent.encodage_etat(self.env)
                actions_suivantes = self.env.mouvement_valide() if not partie_finie else []

                self.agent.mise_a_jour_par_equation_Bellman(etat_actuel, numero_case, recompense, etat_suivant, actions_suivantes)
                
                joueur_actuel = "O" if joueur_actuel == "X" else "X"


            if self.agent.epsilon > self.agent.epsilon_min:
                self.agent.epsilon *= self.agent.epsilon_decay
                    

import pickle


with open("q_tables.pkl", "rb") as fichier:
    q_table = pickle.load(fichier)

with open("q_table_export.txt", "w", encoding="utf-8") as f_txt:
    for etat, actions in q_table.items():
        f_txt.write(f"État (Bitboards X, O) : {etat}\n")
        f_txt.write(f"Actions & Q-valeurs : {actions}\n")
        f_txt.write("-" * 50 + "\n")

print("Exportation terminée ! Ouvrez le fichier 'q_table_export.txt'.")