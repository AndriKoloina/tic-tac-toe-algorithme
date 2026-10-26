from environment import *
import random

class Train:

    env = Environnement()

    def episode(self):
        for i in range(20000):
            self.env.reset()
            joueur_actuel = random.choice(["X", "O"]) 

            for j in range(9):
                numero_case = random.choice(self.env.mouvement_valide())

                verification_nouvelle_position = self.env.jouer_coup(numero_case, joueur_actuel)

                occuper = self.env.player_o | self.env.player_x

                if verification_nouvelle_position is True:
                    if self.env.match_null() is True:
                        break
                    elif joueur_actuel == "X" and self.env.verification_victoire(self.env.player_x) is True:
                           break
                    elif joueur_actuel == "O" and self.env.verification_victoire(self.env.player_o) is True:
                            break

                joueur_actuel = "O" if joueur_actuel == "X" else "X"
                    

                








        