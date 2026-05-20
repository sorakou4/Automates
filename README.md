# Manipulation d’automates finis en Python

Ce projet implémente un ensemble complet d’outils pour manipuler des automates finis :  
lecture de mots, déterminisation, complétion, complémentation, automate produit, minimisation,  
ainsi que la génération de graphes avec Graphviz.

Il s’agit d’un projet réalisé dans le cadre du BUT Informatique (Théorie des langages et automates).

---

## Fonctionnalités

### Manipulation de mots
- Préfixes
- Suffixes
- Facteurs
- Miroir
- Concaténation de langages
- Puissance d’un langage
- Génération de tous les mots d’un alphabet

### Automates finis
- Lecture d’une lettre
- Lecture d’un mot
- Acceptation d’un mot
- Langage accepté (mots de longueur ≤ n)

### Déterminisation
- Vérification si un automate est déterministe
- Déterminisation (construction par sous-ensembles)
- Renommage des états

### Complétion & Complémentation
- Vérification si un automate est complet
- Ajout d’un état puits
- Complémentation d’un automate déterministe complet

### Automate produit
- Intersection de deux automates
- Différence de langages

### Propriétés de fermeture
- Automate des préfixes
- Automate des suffixes
- Automate des facteurs
- Automate miroir

### Minimisation
- Algorithme de Moore
- Séparation des classes
- Découpe des classes
- Construction de l’automate minimal

---

## Visualisation avec Graphviz

Le projet permet de **dessiner automatiquement un automate** au format `.png` grâce à Graphviz.

Exemple :

```python
dessine(auto, "nom_du_fichier")
