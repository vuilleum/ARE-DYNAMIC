#Visualiser avec Python

_Ce document est librement inspiré [tutoriel NumPy de Nicolas Rougier](http://www.labri.fr/perso/nrougier/teaching/matplotlib/matplotlib.html) et est disponible avec son autorisation sous licence Creative Commons Attribution 3.0 United States License (CC-by) http://creativecommons.org/licenses/by/3.0/us_

Lorsque l'on fait une simulation d'un phénomène physique, il est nécessaire de pouvoir visualiser graphiquement ce qui se passe. Une visualisation permet de comprendre et d'analyser plus facilement un phénomène.

[Matplotlib](http://matplotlib.org) est une bibliothèque du langage de programmation Python qui, combinée avec les bibliothèques de calcul scientifique ```NumPy``` et ```SciPy```, constitue un puissant outil pour tracer et visualiser des données issues de mesures ou bien de simulation.

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

Dans le programme ci-dessous, nous avons mis l'ensemble des paramètres qui peuvent influencer l'apparence de la figure. Les paramètres ont été mis explicitement à leurs valeurs par défaut, mais vous pouvez jouer interactivement avec eux pour modifier la visualisation.

```python
# Importer tout de matplotlib (NumPy est accessible via l'alias 'np' alias)
from pylab import *

# Créer une nouvelle figure de taille 8x6 points, en utilisant une résolution de 80 DPI
figure(figsize = (8, 6), dpi=80)

# Créer une sous-figure à partir d'une grille 1x1
subplot(1, 1, 1)

x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
cosx, sinx = np.cos(x), np.sin(x)

# Dessiner la courbe cosinus avec la couleur bleu et une ligne continue de 1 pixel
plot(x, cosx, color = "blue", linewidth = 1.0, linestyle = "-")

# Dessiner la courbe sinus avec une couleur verte et une ligne continue de 1 pixel
plot(x, sinx, color = "green", linewidth = 1.0, linestyle = "-")

# Fixer les limites sur l'axe des x
xlim(-4.0, 4.0)

# Fixer la graduations sur l'axe des x
xticks(np.linspace(-4, 4, 9, endpoint = True))

# Fixer les limites sur l'axe des y
ylim(-1.0, 1.0)

# Fixer la graduations sur l'axe des y
yticks(np.linspace(-1, 1, 5 , endpoint = True))

# Sauvegarder la figure en 72 DPI
# savefig("exercice_2.png", dpi = 72)

# Montrer le résultat à l'écran
show()
```

**Question: Que signifie DPI ?**

##Changer les caractéristiques du trait

Nous voulons changer la courbe du cosinus en bleu et le sin en rouge avec une ligne plus épaisse. Nous allons également modifier la taille de la figure pour la rendre un peu plus horizontale.

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

Les graduations de notre figure ne sont pas idéales car elles ne montre pas des valeurs intéressantes comme (+/-π,+/-π/2) pour sinus et cosinus. Nous les changeons pour montrer ces valeurs.

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

Les graduations sont bien placées, mais le contenu de leur texte n'est pas très explicite. Nous pourrions deviner que 3.142 correspond à π, mais ce serait beaucoup mieux de l'indiquer clairement. Lorsqu'on définit des valeurs pour les graduations, il est aussi possible de définir des étiquettes de texte correspondant à ces valeurs dans une liste fournie en second argument d'appel de fonction. Nous utiliserons une notation [LaTeX](https://fr.wikipedia.org/wiki/LaTeX) pour obtenir un meilleur rendu final.

```python
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_6.png)

## Modifier la position des bords

Les bords peuvent être placés arbitrairement et jusqu'à présent il se trouve en bas et en haut, à droite et à gauche de la figure. Nous allons changer leurs positions pour les placer au milieu. Il y en 4 (top/bottom/left/right). Nous allons effacer celui du haut (top) et de droite (right) en leur donnant une couleur vide (none). On déplace ensuite celui du bas et de gauche au coordonnées 0 en x et en y.

```python
...
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
...
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_7.png)

## Ajouter une légende

Ajoutons une légende dans le coin haut gauche. Il faut ajouter un paramètre nommé ``label`` qui sera utilisé dans la boîte de légende.

```python
...
plot(c, cosx, color="blue", linewidth=2.5, linestyle="-", label="cosinus")
plot(x, sinx, color="red",  linewidth=2.5, linestyle="-", label="sinus")

legend(loc='upper left')
...
```

![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_8.png)

** Question: Que fait la fonction ``legend()``?**

## Ajouter des points particuliers

Ajoutons quelques points intéressants en utilisant la fonction ``annotate()``.
Nous choisissons la valeur 2π/3 et nous voulons annoter à la fois la courbe sinus et cosinus. Nous dessinons un marqueur sur la courbe ainsi qu'une ligne en trait pointillé. Puis nous utilisons la fonction ``annotate()``pour afficher du texte avec une flêche.

```python
...

t = 2*np.pi/3
plot([t,t],[0,np.cos(t)], color ='blue', linewidth=2.5, linestyle="--")
scatter([t,],[np.cos(t),], 50, color ='blue')

annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
xy=(t, np.sin(t)), xycoords='data',
xytext=(+10, +30), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plot([t,t],[0,np.sin(t)], color ='red', linewidth=2.5, linestyle="--")
scatter([t,],[np.sin(t),], 50, color ='red')

annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
xy=(t, np.cos(t)), xycoords='data',
xytext=(-90, -50), textcoords='offset points', fontsize=16,
arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
...
```
![image](http://www.labri.fr/perso/nrougier/teaching/matplotlib/figures/exercice_9.png)

## Sauvegarder une figure Matplotlib

On peut générer un fichier image (que l'on pourra réutiliser ensuite sur le web ou dans un rapport) à partir d'une figure Matplotlib (par exemple ici en résolution de 72 points par pouce (1 pouce : 2.54 cm).)

```python
savefig("nom_image.png", dpi=72)
```

## Utiliser Matplotlib pour afficher des mesures

## Utiliser Matplotlib pour afficher le contenu d'une grille à deux dimensions
Matplotlib peut afficher des images. Pour cela, il faut utiliser la commande:

```python
plt.imshow(m, cmap= ... , interpolation= ... )
```

 * Le premier paramètre est une matrice (array de numpy). Chaque élément de cette matrice est l’information sur un pixel, par exemple il peut s’agir d’une liste de triplets encodant les composantes R (rouge), G (verte), B (bleue) de chaque pixel.
 * Le deuxième paramètre est la “carte de couleur” de l’image, elle associe couleurs aux valeurs.
 * Le troisième paramètre est la manière dont les valeurs sont interpolées.

Pour les détails, voir: http://matplotlib.org/users/image_tutorial.html

## Faire des animations avec Matplotlib
Il est possible d'utiliser Matplotlib pour animer des images en utilisant le module animation.

```
from matplotlib import animation
````

Il faut dans un premier temps créer la figure à animée. Pour cela deux fonctions peuvent être utilisées :

1. init() qui définit l'image de base, qui restera présente par défaut en arrière-plan,
2. animate() qui définit l'évolution de l'image et qui sera appellé périodiquement.
