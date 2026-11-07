===========================================================
      SYSTÈME DE GESTION DES EMPLOYÉS (Python & CSV)
===========================================================

1. DESCRIPTION
--------------
Ce logiciel est une solution légère permettant de gérer une base de 
données d'employés stockée au format CSV. Il permet d'effectuer des 
opérations de gestion (CRUD), des analyses statistiques et des 
exports sécurisés.

2. LISTE DES FONCTIONNALITÉS
----------------------------
Le système propose les fonctionnalités suivantes :

*   Authentification : Accès sécurisé par identifiant/mot de passe 
    avec journalisation (audit.log) des tentatives d'accès.

*   Gestion CRUD : Ajouter, Rechercher, Modifier et Supprimer 
    un employé.

*   Statistiques : Calcul de nombre d'employés et calcul automatique des
    salaires (Min, Max, Moyenne) globalement et par département.

*   Génération de Rapport : Création d'un fichier 'report.txt' contenant 
    un histogramme textuel de la répartition par département.

*   Exportation : Extraction automatique des hauts salaires (> 4000) 
    vers un fichier 'high_salary.csv'.

*   Tri et Filtrage : Organisation des données par salaire ou 
    département et filtrage multicritères.

*   Nettoyage : Suppression automatique des doublons sur l'ID lors 
    du lancement du programme.
  
3. GUIDE D'UTILISATION
----------------------
- Assurez-vous d'avoir Python 3.x installé.
- Les fichiers 'employes.csv' et 'users.csv' doivent se trouver 
dans le même dossier que le script.
- Exécutez le script : python projet_csv.py 
- Connectez-vous avec vos identifiants (3 tentatives autorisées).
- Utilisez les chiffres de 1 à 10 pour choisir une action dans 
le menu principal.
- Répondez par 'O' (Oui) ou 'N' (Non) pour quitter ou continuer.

NB: Pour cette version, les entrées utilisateur doivent respecter le type
attendu (chiffres pour le menu, texte pour les noms). Une saisie de type
incorrect (ex: une lettre au lieu d'un chiffre) peut provoquer un arrêt 
du programme.

4. STRUCTURE DU FICHIER CSV
---------------------------
Le fichier 'employes.csv' doit utiliser le point-virgule (;) comme 
séparateur et comporter les colonnes suivantes :
id ; nom ; prenom ; poste ; salaire ; departement

5. SÉCURITÉ ET AUDIT
--------------------
Toutes les tentatives de connexion sont enregistrées dans 'audit.log'. 
En cas de 3 échecs consécutifs, le système se verrouille 
automatiquement pour protéger les données.

===========================================================

