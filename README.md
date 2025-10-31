# 🧰 Boîte de Rangement Intelligente
## Smart Storage Assistant

### 🎯 Objectif du projet

Application de bureau interactive permettant de visualiser, gérer et localiser facilement les outils ou composants dans une boîte de rangement physique à **12×12 compartiments (144 cases)**.

### ✨ Fonctionnalités principales

- **Grille virtuelle 12×12** : Visualisation de la boîte réelle avec 144 cases
- **Gestion du contenu** : Association d'éléments (outils/composants) à chaque case
- **Gestion de projets** : Création et sélection de projets (ex. "Circuit Raspberry Pi")
- **Localisation visuelle** : Surbrillance automatique des cases contenant les pièces nécessaires à un projet sélectionné
- **Recherche rapide** : Recherche d'outils/composants dans la boîte

### 💡 Contexte d'utilisation

Ce logiciel est utile pour :
- Les makers, étudiants ou techniciens qui ont des kits électroniques avec plusieurs petits composants
- Gagner du temps lors de la recherche d'outils pour un montage précis
- Visualiser et documenter facilement le contenu de la boîte

### 🏗️ Architecture du projet

Le projet sera développé de manière **modulaire**, chaque fonctionnalité étant autonome avec des commits dédiés et descriptifs.

#### Structure prévue :
```
SmartStorageAssistant/
├── src/
│   ├── models/          # Modèles de données (Case, Projet, Composant)
│   ├── views/           # Interface utilisateur (grille, formulaires)
│   ├── controllers/     # Logique métier
│   └── utils/           # Utilitaires
├── data/                # Données persistantes (JSON/SQLite)
├── tests/               # Tests unitaires
└── requirements.txt     # Dépendances Python
```

### 🛠️ Technologies prévues

- **Langage** : Python
- **Interface graphique** : Tkinter (ou PyQt/PySide pour un rendu plus moderne)
- **Stockage** : JSON ou SQLite pour la persistance des données
- **Architecture** : MVC (Modèle-Vue-Contrôleur)

### 📋 Étapes de développement (modulaires)

1. **Structure de base** : Architecture MVC et configuration
2. **Modèle de données** : Classes Case, Composant, Projet
3. **Grille 12×12** : Affichage de la grille de base
4. **Gestion du contenu** : Ajout/modification/suppression d'éléments par case
5. **Gestion de projets** : Création et sélection de projets
6. **Système de surbrillance** : Mise en évidence des cases selon le projet
7. **Persistance des données** : Sauvegarde/chargement
8. **Recherche et filtres** : Recherche de composants dans la boîte

### 🚀 Installation

À venir...

### 📝 Licence

À définir

