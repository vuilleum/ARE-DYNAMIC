#Visualiser avec Python

_Ce document est librement inspiré [tutoriel NumPy de Nicolas Rougier](http://www.labri.fr/perso/nrougier/teaching/matplotlib/matplotlib.html) et est disponible avec son autorisation sous licence Creative Commons Attribution 3.0 United States License (CC-by) http://creativecommons.org/licenses/by/3.0/us_

Lorsque l'on fait une simulation d'un phénomène physique, il est nécessaire de pouvoir visualiser graphiquement ce qui se passe.

[Matplotlib](http://matplotlib.org) est une bibliothèque du langage de programmation Python qui, combinée avec les bibliothèques de calcul scientifique ```NumPy``` et ```scipy```, constitue un puissant outil pour tracer et visualiser des données.

## Utiliser Matplotlib pour tracer une fonction

```python
from pylab import *
x = np.linspace(-np.pi, np.pi, 256)
cosx = np.cos(x)
sinx = np.sin(x)
plot(x, cosx)
plot(x, sinx)
show()
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_1.png)

La fonction ``linspace`` de la librairie ``NumPy`` (np) permet de générer un tableau de 256 valeurs réélles variant de -π à π (inclus).
`cosx` est un tableau de 256 valeurs contenant le résultat de l'application de la fonction ``cos(x)`` sur chacune des valeurs du tableau `x`.

## Valeurs d'affichage par défaut
Matplotlib est fournie avec un jeu de paramètres par défaut qui permet de personnaliser toute sorte de propriétés. Vous pouvez contrôler les réglages par défaut de (presque) toutes les propriétés : taille du graphique, résolution en points par pouce (dpi), épaisseur du trait, couleurs, styles, vues, repères, grilles, textes, polices de caractères, etc. Bien que les réglages par défaut répondent à la plupart des cas courants, vous pourriez être amené à en modifier quelques-uns pour des cas plus spécifiques.

In the script below, we've instantiated (and commented) all the figure settings that influence the appearance of the plot. The settings have been explicitly set to their default values, but now you can interactively play with the values to explore their affect (see Line properties and Line styles below).

```python
# Import everything from matplotlib (numpy is accessible via 'np' alias)
from pylab import *

# Create a new figure of size 8x6 points, using 80 dots per inch
figure(figsize=(8,6), dpi=80)

# Create a new subplot from a grid of 1x1
subplot(1, 1, 1)

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
cosx,sinx = np.cos(x), np.sin(x)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
plot(x, cosx, color="blue", linewidth=1.0, linestyle="-")

# Plot sine using green color with a continuous line of width 1 (pixels)
plot(x, sinx, color="green", linewidth=1.0, linestyle="-")

# Set x limits
xlim(-4.0, 4.0)

# Set x ticks
xticks(np.linspace(-4, 4, 9, endpoint = True))

# Set y limits
ylim(-1.0, 1.0)

# Set y ticks
yticks(np.linspace(-1, 1, 5 , endpoint = True))

# Save figure using 72 dots per inch
# savefig("exercice_2.png", dpi = 72)

# Montrer le résultat à l'écran
show()
```

##Changer les caractéristiques du trait

Nous voulons changer la courbe du coisinus en bleu et le sin en rouge avec une ligne plus épaisse. Nous allons également modifier la taille de la figure pour la rendre un peu plus horizontale.

```python
...
figure(figsize=(10,6), dpi=80)
plot(x, cosx, color="blue", linewidth=2.5, linestyle="-")
plot(x, sinx, color="red",  linewidth=2.5, linestyle="-")
...
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_3.png)

La fonction ``plot()`` dispose d'un argument color qui permet de changer la couleur de la courbe. Changer par exemple la ligne ``plot(x,cosx)`` par ``plot(x, cosx, color="red")``.

L'argument ``linewidth`` permet de changer l'épaisseur du trait exprimé en pixels.

L'argument ``linestyle`` permet de changer le style d'affichage de la ligne de courbe.
Vous pouvez essayer les différents paramètres: '-', '--', '-.', ':' ou 'steps'.

##Fixer les limites de la figure

Les axes du repère sont les droites qui portent les marques de graduation et qui délimitent la zone de représentation du graphique. Ces axes peuvent être placés arbitrairement.

Il est possible de changer les axes du repères en utilisant les fonctions ``xlim()``, ``ylim()``.


```python
xmin ,xmax = x.min(), x.max()
ymin, ymax = y.min(), y.max()

dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2

xlim(xmin - dx, xmax + dx)
ylim(ymin - dy, ymax + dy)
```

Voir documentation sur les fonctions ``xlim()`` : http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.xlim et ``ylim()`` :
http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.ylim

## Définir des graduations

Current ticks are not ideal because they do not show the interesting values (+/-π,+/-π/2) for sine and cosine. We'll change them such that they show only these values.

```python
...
xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
yticks([-1, 0, +1])
...
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_5.png)


## Définir le texte des graduations

Les graduations actuelles ne sont pas idéales : elles n'affichent pas sur l'axe des abscisses les valeurs (+/-π, +/-π/2) et sur l'axe des ordonnées les valeurs (-1, 0, +1) qui nous intéressent pour cosinus. Modifions-les pour qu'elles correspondent à ces valeurs :

```python
xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
yticks([-1, 0, +1])
```

Les graduations sont bien placées, mais le contenu de leur texte n'est pas très explicite. Nous pourrions deviner que 3.142 correspond à π, mais ce serait beaucoup mieux de l'indiquer clairement. Lorsqu'on définit des valeurs pour les graduations, il est aussi possible de définir des étiquettes de texte correspondant à ces valeurs dans une liste fournie en second argument d'appel de fonction. Nous utiliserons une notation LaTeX pour obtenir un meilleur rendu final.

```python
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_6.png)

## Ajouter une légende

### Sauvegarder une figure Matplotlib

On peut générer un fichier image (que l'on pourra réutiliser ensuite sur le web ou dans un rapport) à partir d'une figure Matplotlib (par exemple ici en résolution de 72 points par pouce[^1].)

[^1]: 1 pouce = 2.54 cm

```python
savefig("nom_image.png", dpi=72)
```

## Utiliser Matplotlib pour afficher des mesures

## Utiliser Matplotlib pour dessiner une grille 2D

## Faire des animations avec Matplotlib
Il est possible d'utiliser Matplotlib pour animer des images en utilisant le module animation.

```
from matplotlib import animation
````

Il faut dans un premier temps créer la figure à animée. Pour cela deux fonctions peuvent être utilisées :

1. init() qui définit l'image de base, qui restera présente par défaut en arrière-plan,
2. animate() qui définit l'évolution de l'image et qui sera appellé périodiquement.
