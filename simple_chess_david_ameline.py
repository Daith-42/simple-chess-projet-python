""" Simple Chess - par David Ameline PGE1 pour SUPINFO """

def newBoard(n):
    """fonction qui retourne une liste à deux dimensions représentant l’état initial d’un plateau de jeu de n cases sur n cases."""

    # création de la table vide
    a = [[0 for x in tuple(range(n))] for x in tuple(range(n))]

    # ajout des pions
    a[1] = [1 for x in tuple(range(n))]
    a[n - 2] = [2 for x in tuple(range(n))]

    return a



def displayBoard(board, n):
    """procédure qui réalise l’affichage du plateau sur la console"""

    # affichage du tableau
    for i in range(n):
        print(i + 1, end=('|'))

        # affichage des bons pions
        for j in range(n):

            # si la case est vide
            if board[i][j] == 0:
                print('.', end=(' '))

            # si la case appartient au joueur 1
            if board[i][j] == 1:
                print('x', end=(' '))

            # si la case appartient au joueur 2
            if board[i][j] == 2:
                print('o', end=(' '))

            # si la case est neutre
            if board[i][j] == 3:
                print('N', end=(' '))

        print(" ")

    # affichage de la ligne du bas
    print(' ', end=(''))
    print('--' * n)

    # affichage des chiffres du bas
    print('  ', end=(''))
    for k in range(n):
        print(k + 1, end=(' '))

    print("")
    print("")



def possiblePawn(board, n, player, i, j):
    """fonction qui retourne True si i et j sont les coordonnées d’un pion que le joueur player peut déplacer, et False sinon"""

    # vérification de la direction en fonction du joueur
    if player == 1:
        direction = 1
    else:
        direction = -1

    # vérifie si les coordonnées sont dans le tableau
    if 0 <= i < n and 0 <= j < n:
        # vérifie si le pion appartient au joueur
        if board[i][j] == player:
            # vérifie si au moins 1 déplacement est faisable

            # Déplacement vertical
            if 0 <= i + direction < n and board[i + direction][j] == 0:
                return True

            # Déplacement diagonale gauche
            if 0 <= i + direction < n and 0 <= j - 1 < n and board[i + direction][j - 1] == (3 - player):
                return True

            # Déplacement diagonale droite
            if 0 <= i + direction < n and 0 <= j + 1 < n and board[i + direction][j + 1] == (3 - player):
                return True

    return False



def selectPawn(board, n, player):
    """fonction qui fait saisir au joueur player les coordonnées d’un pion pouvant se déplacer"""

    valide = False

    while valide == False:

        i = int(input("Choisir la ligne d'un pion : ")) - 1

        j = int(input("Choisir la colonne correspondante : ")) - 1


        if possiblePawn(board, n, player, i, j) == True:
            valide = True


        if valide == False:
            print("incorect, entrez de nouveau les coordonées du pion")

    return i, j



def possibleDestination(board, n, player, i, j, l):
    """fonction dans laquelle on vérifie si le déplacement est faisable"""

    # vérification de la direction en fonction du joueur
    if player == 1:
        i = i + 1
        adversaire = 2
    else:
        i = i - 1
        adversaire = 1

    # vérifie si la coordonnée est dans le tableau et si le déplacement est faisable
    if 0 <= l < n and (j == l or j == l - 1 or j == l + 1):

        # vérifie si le déplacement est faisable
        if (l == j and board[i][l] == 0):
            return True

        if (l == j - 1 or l == j + 1) and board[i][l] == adversaire:
            return True
    return False



def selectDestination(board, n, directions, player, i, j):
    """fonction dans laquelle le joueur entre son déplacement"""

    valide = False

    while valide == False:

        l = int(input("Choisir la colonne de destination : ")) - 1

        if possibleDestination(board, n, player, i, j, l) == True:
            valide = True

        if valide == False:
            print("incorect, entrez de nouveau des coordonnés")

    return l



def move(board, n, player, i, j, l):
    """procédure qui réalise le déplacement du joueur"""

    board[i][j] = 0

    if player == 1:
        board[i + 1][l] = 1

    else:
        board[i - 1][l] = 2



def lose(board, n, player):
    """fonction qui retourne True si le joueur player a perdu"""

    # vérification pour le player 1
    if player == 1:
        # vérification de si un pion adverse a atteint le coter adverse
        if 2 in board[0]:

            return True

    # vérification pour le player 2
    else:
        # vérification de si un pion adverse a atteint le coter adverse
        if 1 in board[n-1]:

            return True

    verification_pion = False
    verification_deplacement = False

    # vérification de si il reste des pions au player
    for idex in range(n):
        for jdex in range(n):
            if jdex == 2:
                verification_pion = True

            # vérification si au moins un pion peut bouger
            if possiblePawn(board, n, player, idex, jdex):
                verification_deplacement = True

    if verification_pion == False or verification_deplacement == False:
        return True

    return False



def simpleChess(n):
    """fonction qui fait fonctinner l'ensemble du jeu"""

    # ajout d'une taille minimal pour la table de jeu
    if n < 4:
        n = 4

    # création de la table de jeu
    board = newBoard(n)

    # c'est le joueur 1 qui commence
    player = 1
    directions = 1

    while lose(board, n, player) == False:

        # affichage de la table de jeu
        displayBoard(board, n)

        # affichage de à qui le tour
        print("C'est au Joueur", player, "de jouez")

        # selection des coordonées
        i, j = selectPawn(board, n, player)
        l= selectDestination(board, n, directions, player, i, j)

        # update de la table de jeu
        move(board, n, player, i, j, l)

        # changement de joueur
        if player == 1:
            player = 2

        else:
            player = 1

    displayBoard(board, n)
    # affichage du gagnant
    if player == 1:
        print("le joueur 2 a gagner")

    else:
        print("le joueur 1 a gagner")

n=5
simpleChess(n)














