def backtrack(T, i=0, j=0):
    if i == len(T):
        return True
        
    if T[i][j] != 0:
        suivant_i, suivant_j = (i, j + 1) if j < 3 else (i + 1, 0)
        return backtrack(T, suivant_i, suivant_j)
    
    for num in range(1, 5):
        if is_valid(T, i, j, num):
            T[i][j] = num
            
            suivant_i, suivant_j = (i, j + 1) if j < 3 else (i + 1, 0)
            if backtrack(T, suivant_i, suivant_j):
                return True
                
            T[i][j] = 0
    
    return False
    
def is_valid(T, ligne, colonne, num):
    if num in T[ligne]:
        return False
    
    for i in range(4):
        if T[i][colonne] == num:
            return False
    
    start_ligne, start_colonne = 2 * (ligne // 2), 2 * (colonne // 2)
    for i in range(2):
        for j in range(2):
            if T[start_ligne + i][start_colonne + j] == num:
                return False
    return True

def afficher_grille(grille):
    print()
    for i in range(4):
        if i == 2:
            print("---------")
        for j in range(4):
            if j == 2:
                print("|", end=" ")
            print(grille[i][j] if grille[i][j] != 0 else ".", end=" ")
        print()

if __name__ == "__main__":
    grille = [
        [0, 0, 1, 0],
        [0, 0, 0, 3],
        [0, 0, 0, 2],
        [2, 0, 0, 0]
    ]

    print("Grille de départ")
    afficher_grille(grille)
    
    if backtrack(grille):
        print("Solution :")
        afficher_grille(grille)
    else:
        print("IMPOSSIBLE")