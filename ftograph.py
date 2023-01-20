# Function to Graph By E.H.A.
import matplotlib.pyplot as plt
import numpy as np

# couleurs
class bcolors:
    RED ='\033[91m' # couleur rouge 
    RESET = '\033[0m' # reset la couleur


# contenant(variables)
msg_start = """Bievenue sur\n
███████╗████████╗ ██████╗  ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗
██╔════╝╚══██╔══╝██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║  ██║
█████╗     ██║   ██║   ██║██║  ███╗██████╔╝███████║██████╔╝███████║
██╔══╝     ██║   ██║   ██║██║   ██║██╔══██╗██╔══██║██╔═══╝ ██╔══██║
██║        ██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██║     ██║  ██║
╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝
                                                                   \nUn outil d'E.H.A. permettant de transformer une fonction en graphique."""
msg_f = "Entrez votre fonction sous la forme y = mx + p\ny= "
msg_min = "Entrez le x minimale de votre fonction(ou cliquez sur Q pour quitter): "
msg_max = "Entrez le x maximal de votre fonction: "
msg_f_title = "Entrez votre fonction complète (ex:y=mx+p): "
msg_bye = "Merci d'avoir utilisé FtoGRAPH. A bientôt."
# acceuil
while True:
    print(bcolors.RED + msg_start + bcolors.RESET)

    # contenants input()
    xmin = int(input(msg_min))
    if xmin == "Q" : # quitter
        print(bcolors.RED + msg_bye + bcolors.RESET)
        break
    xmax = int(input(msg_max))
    f_title = input(msg_f_title)

    # 100 nombres espacés linéairement
    x = np.linspace(xmin,xmax,100)

    # la fonction,valeur de y
    f = eval(input(msg_f))
    y = f
    # parametrer les axes au centre
    ax = plt.gca()

    ax.plot(x,y)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    # plot the functions
    plt.xlim(-np.pi,np.pi)
    plt.plot(x,y, 'b', label= f_title)
    plt.legend(loc='upper left')
    plt.title('Function to Graph By E.H.A.')
    plt.grid()

    # afficher le plot
    plt.show()



