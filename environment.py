class Environnement : 
    composition_gagnant = [
                0b111,          
                0b111000,       
                0b111000000,    
                0b1001001,      
                0b10010010,     
                0b100100100,  
                0b100010001,    
                0b01010100      
            ]

    def __init__(self):
        self.player_x = 0
        self.player_o = 0 

    def mouvement_valide(self):
        occuper = self.player_x |self.player_o
        mouvements = []
        for i in range(9):
            if not (occuper & (1 << i)):
                mouvements.append(i)

        return mouvements

    def verification_victoire(self,tableau_joueur):
        for composition in Environnement.composition_gagnant:
            if (tableau_joueur & composition) == composition:
                return True
        return False

    def match_null(self):
        mouvements = self.mouvement_valide(self.player_x, self.player_o)

        if len(mouvements) == 0 and not self.verification_victoire(self.player_o) and not self.verification_victoire(self.player_x):
            return True
        return False

    def jouer_coup(self, case, joueur):

        if case not in self.mouvement_valide():
            return False

        if joueur == "X":
            self.player_x |= (1 << case)
        
        else:
            self.player_o |= (1 << case)

        return True


    def afficher_plateau(self, tableau_x, tableau_o):
        grille = []

        for i in range(9):
            if tableau_x & (1 << i):
                grille.append("X")
            elif tableau_o & (1 << i):
                grille.append("O")
            else:
                grille.append(str(i))


        print(f"\n {grille[0]} | {grille[1]} | {grille[2]} ")
        print("-----------")
        print(f" {grille[3]} | {grille[4]} | {grille[5]} ")
        print("-----------")
        print(f" {grille[6]} | {grille[7]} | {grille[8]} \n")
                
    




    