from environment import *
import random

class Agent:

    env = Environnement()
    def __init__(self):
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.01
        self.q_table = {}


    def encodage_etat(self, env):
        encodage = (env.player_x, env.player_o)

        return encodage


    def get_gestion_Q_valeurs(self, etat, liste_actions_valides):
        
        if etat not in (self.q_table):
            self.q_table[etat] = {action: 0.0 for action in liste_actions_valides}
        else:
            for action in liste_actions_valides:
                if action not in self.q_table[etat]:
                    self.q_table[etat][action] = 0.0

        return self.q_table[etat]
            


    def choix_action(self, etat, liste_actions_valides):
        q_values = self.get_gestion_Q_valeurs(etat, liste_actions_valides)

        choix_mode= random.random()

        if choix_mode < self.epsilon:
            pioche_coup = random.choice(liste_actions_valides)

            return pioche_coup
        else:
            max_q = max(q_values.values())

            meilleurs_coups = [action for action, q in q_values.items() if q == max_q]

            return random.choice(meilleurs_coups)


    def mise_a_jour_par_equation_Bellman(self, etat_s, action, recompense_r, etat_suivant, liste_actions_suivantes):
        q_ancienne = self.q_table[etat_s][action]

        q_valeur_suivante = self.get_gestion_Q_valeurs(etat_suivant, liste_actions_suivantes)

        if liste_actions_suivantes:
            max_q_futur = max(q_valeur_suivante.values())
        else:
            max_q_futur = 0.0

        q_nouvelle = q_ancienne + self.alpha *  (recompense_r + self.gamma  * max_q_futur - q_ancienne)

        self.q_table[etat_s][action] = q_nouvelle 

        return self.q_table[etat_s][action]




