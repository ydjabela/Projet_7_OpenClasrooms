## Projet OpenClassrooms
## Projet 7 Résolvez des problèmes en utilisant des algorithmes en Python

###Description du projet :
Ce projet consiste à optimiser les solutions des clients afin de rendre les programmes d'investissement à court terme plus compétitifs.
AlgoInvest&Trade à besoin d'un algorithme qui maximisera le profit réalisé par les clients après deux ans d'investissement. 
l'algorithme doit suggérer une liste des actions les plus rentables à acheter pour maximiser le profit d'un client au bout de deux ans.

### Récupérer le projet :

```
git clone https://github.com/ydjabela/Projet_7_Openclassrooms
```

### Création de l'environnement virtuel

Assurez-vous d'avoir installé python et de pouvoir y accéder via votre terminal, en ligne de commande.

Si ce n'est pas le cas : https://www.python.org/downloads/

```
python -m venv Projet_7
```

### Activation de l'environnement virtuel du projet

Windows :

```
Projet_7\Scripts\activate.bat
```

MacOS/Linux :
```
source Projet_7/bin/activate
```

### Installation des packages necessaire pour ce projet
```
pip install -r requirements.txt
```

### Exécuter le scripts:

#### pour exécuter le scraper complet

Pour lancer le projet : 
``` python bruteforce.py  ``` et pour lancer le script bruteforce !
``` python optimized.py  ``` et pour lancer le script optimisé !

###Vérifier la qualité du code :

installer flake8-html

``` pip install flake8-html ```

Pour lancer la vérification de la qualité du code : 
```
flake8 --format=html --htmldir=flake-report --exclude=env --max-line-length=119
```
### Contributeurs
- Yacine Djabela 
- Stephane Didier

