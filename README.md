# PROJET 3 - Choix A - DAAR
>  ## Réalisé par :
> * <b>Amine KHEDDAR</b> 
> * <b>Sofiane BELKHIR</b>


🚀 Le code du projet est divisé en 2 répertoires.
* 📁 <b>BACK_END_DAAR</b> 
* 📁 <b>FRONTEND_DAAR</b>
 

# Exécution du code

## Pour le Back End :

Ce placer dans le dossier <b>BACK_END_DAAR</b> sur un terminale puis lancer les commandes suivantes : 

```sh
python3 -m venv myTidyVEnv
source myTidyVEnv/bin/activate
pip3 install django djangorestframework requests
pip3 install django-cors-headers stop-words
cd .\mySearchEngine\
python3 manage.py runserver
```

Le nombre de livre à importer peut etre modifier en changeant le parametre <b>number_of_book</b> dans le fichier <b>.\mygutenberg\config.py</b>

## Pour actualiser la base de données, lancer les commandes suivantes : 

```sh
cd .\mySearchEngine\
python manage.py refreshBooksList
python manage.py RefreshJaccardDistance
```

#### Pour le Front End :

Ce placer dans le dossier <b>FRONTEND_DAAR</b> sur un terminale puis lancer les commandes suivantes : 

```sh
npm install
npm install -g @ionic/cli
ionic serve
```

> Utilisation du Site 

* <b> Recherche Simple : </b>
    entrer un mot puis appuyer sur entrer pour effectuer une recherche 

* <b> Recherche avancée : </b>
    entrer une expression régulière puis appuyer sur entrer pour effectuer une recherche 

On pourra switcher entre une recherche simple et avancée en appuyant sur le bouton en haut de la barre de recherche


