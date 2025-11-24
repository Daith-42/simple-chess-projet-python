##########################################################

NOM : simple_chess_david_ameline
PAR : David AMELINE
POUR : SUPINFO
DATE : 26/10/2025

##########################################################

Simple Chess est un jeu dans lequel 2 joueur s'affronte dans un carré de n cases sur n cases initialement vide.

Le premier joueur possède des pions blancs et le second des pions noirs.

À tour de rôle, chaque joueur déplace l'un de ses pions

##########################################################

Il contient 9 fonctions (6 sous-fonctions, 2 procédures, et une fonction principale.

Sous-fonctions :
    - newBoard(n)
        crée la table de jeu
    - possiblePawn(board, n, player, i, j
        vérifie si le joueur peut jouer ce pion
    - selectPawn(board, n, player)
        fait saisir au joueur les coordonnées du pion qu'il veut jouer
    - possibleDestination(board, n, player, i, j, l)
        vérifie si le joueur peut déplacer son pion à l'endroit désirer
    - selectDestination(board, n, directions, player, i, j)
        fait saisir au joueur les coordonnées du pion qu'il veut jouer
    - lose(board, n, player)
        verifie si il y a un perdant

Procédures :
    - displayBoard(board, n)
        affiche la table de jeu
    - move(board, n, player, i, j, l)
        réalise les changements dans board

Fonction principale :
    - simpleChess(n)
        fait tourné tous les sous programmes ensemble

##########################################################
