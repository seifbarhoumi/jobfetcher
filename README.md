# 🚀 France Travail Job Scraper (Flexible & Automatisé)

![Repo Size](https://img.shields.io/badge/Repo%20Size-506.9kB-blue)
![Last Commit](https://img.shields.io/badge/Last%20Commit-March%2025,%202025-orange)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Docker](https://img.shields.io/badge/Docker-Supported-blue)

# 📌 Description
Ce projet est un extracteur avancé d'offres d'emploi utilisant l'API France Travail.

## 🏗 Fonctionnalités principales :
* **✔ Scraping sur mesure :** choisissez le département, le type de contrat et le nombre d'offres
* **✔ Export CSV automatique :** extraction des offres, entreprises et compétences
* **✔ Interface CLI :** utilisation intuitive via Typer
* **✔ Exécution planifiée :** automatisation avec Cron (tâches récurrentes)
* **✔ Conteneurisation Docker :** exécution reproductible et portable
* **✔ Authentification OAuth2 :** sécurité renforcée

## 🔍 Exemple d'utilisation

Ce projet est un **extracteur de données** qui récupère les offres d'emploi en **CDI** du département **07** via l'API de **France Travail**. Il génère automatiquement **trois fichiers CSV** :

✅ `offres_d_emploi.csv` → Liste des offres disponibles  
✅ `entreprises.csv` → Informations sur les entreprises  
✅ `competences.csv` → Compétences requises  

_💡 Exemple de commande CLI :_

`python -m job_cli fetch job --type-contrat CDI --departement 07 
`
---

## 🛠️ Tech Stack
- 🐍 **Python 3.10** → Langage principal du projet
- 🔗 **Requests** → interaction avec l’API France Travail
- 🔒 **OAuth 2.0** → authentification sécurisée
- 🐳 **Docker** → exécution reproductible  
- 🏗 **Docker Compose** → Orchestration des services

## 📦 Gestion des Données & Configuration
- 🛠 **Pydantic** → gestion des paramètres et validation des données 
- 🏗 **Pydantic Settings** → gestion de la configuration avec validation

## 🖥️ Interface & Automatisation
- 🔄 **Tenacity** → gestion des tentatives et des erreurs 
- 💻 **Typer** → création d’une interface CLI intuitive
- 🕒 Schedule (Cron via Python) → Planification automatique des tâches

## 📝 Logs & Erreurs
- 🔍 Logging (logging) → Suivi des événements et erreurs

## 🧪 Tests & Débogage
- ✅ **Pytest** → tests unitaires et d’intégration  
- 🧩 pytest-mock → Simulation des appels API et dépendances 
- 🌍 pytest-dotenv → Chargement des variables d’environnement dans les tests

## 🚀 Déploiement & CI/CD
- 📜 Makefile → Simplification des commandes courantes (make build, make test, etc.)
- 🖥️ Shell scripting (bash) → Automatisation des tâches de build et maintenance
- 🔄 Docker & Docker Compose → Conteneurisation et orchestration


---


## 📂 **Structure du projet**

```
📁 jobfetcher
│── 📁 job_cli/          # CLI Package
│ │── 📁 commands/       # Typer commands
│ │ │── 📁 fetch/        # fetch job commands
│ │ │ │── 📄 __init__.py # Init file
│ │ │ │── 📄 fetch.py    # fetch command avec le script pincipal
│ │ │── 📄 __init__.py   # Init file
│ │── 📄 __init__.py     # Init file
│ │── 📄 main.py         # Contains the Typer app management
│── 📁 DEPLOY/           # Repertoire de deploiement 
│ │── 📄 Dockerfile      # Conteneurisation avec Docker
│ │── 📄 docker-compose.yml # Exécution avec Docker-compose
│── 📁 services/         # Gestion des appels API
│ │── 📄 auth.py         # Gère l'authentification OAuth2
│ │── 📄 offres.py       # Récupère les offres d'emploi
│ │── 📄 data_handler.py # transforme les sorties d'API en fichiers CSVs
│── 📁 utils/            # Outils et helpers
│ │── 📄 csv_writer.py   # Gère l'export en CSV
│ │── 📄 logger.py       # Gère les logs
│ │── 📄 config.py       # Configuration (lecture des variables d'env)
│── 📁 tests/            # Tests unitaires
│ │── 📄 test_config.py  # Assertion de la bonne config
│ │── 📄 test_auth.py    # Assertion de l'authentification
│ │── 📄 test_offres.py  # Assertion de la récupération des offres d'emploi
│── 📁 outputs/          # Outputs fichiers CSVs   & entreprises competences.csv
│ │── 📁 DEPARTEMENT_ZIPCODE/  # 01..101
│ │ │── 📁 TYPE_CONTRAT/       # CDI|CDD|MIS
│ │ │ │── 📄 offres_d_emploi.csv  
│ │ │ │── 📄 entreprises.csv   
│ │ │ │── 📄 competences.csv   
│── 📄 job_fetcher.log   # Logs les appels d'API
│── 📄 requirements.txt  # Dépendances Python
│── 📄 .env              # Variables d'environnement (API keys, secrets)
│── 📄 .env_template     # Template des Variables d'environnement 
│── 📄 .gitignore        # Fichiers à ignorer dans Git
│── 📄 Makefile          # simplifier les commandes courantes (Docker, Typer[Fetch], etc)
│── 📄 cron_fetch        # the Cron Job Script pour programmer la récupération des infos
│── 📄 README.md         # Documentation

```

---

## 📂 Installation & Utilisation

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/seifbarhoumi/jobfetcher.git
cd jobfetcher
```

### 2️⃣ Configurer les dépendances
```bash
make install
```

### 3️⃣ Utilisation du Scraper
```bash
make run
```
ou
```bash
python -m job_cli fetch job --type-contrat [CDI|CDD|MIS] --departement x 
```

---

## 🕒 Automatisation avec Cron


### 📌 Ajouter une tâche planifiée (tous les jours à 6h du matin)

```bash
make setup-cron
```

### 📌 Lister les tâches cron actives

```bash
make list-cron
```
### 📌 Arrêter le cron job
```bash
make stop-cron
```

### 📌 Lister les tâches cron actives

```bash
make list-cron
```

---

## 🐳 Exécution avec Docker

### 1️⃣ Construire l’image

```bash
make docker-build
```
### 2️⃣ Lancer le scraping dans un container

```bash
make docker-run
```
ou
```bash
docker run --rm jobfetcher fetch job --type-contrat CDI --departement 07 
```


--- 

## ✅ Tests

Exécuter les tests unitaires :

```bash
make test
```
OU
```bash
pytest tests/
```

---

## 🔥 Résumé des Commandes Utiles


| Commande	          | Description  | 
|--------------------|---|
| `make install`	    | Installer les dépendances
  |
| `make run`	        | Exécuter un fetch manuel
  |
| `make setup-cron`	 | Planifier le cron job
  |
| `make list-cron`	  | Voir les tâches cron actives
  |
|  `stop-cron`	        |  Supprimer le cron job
 |
| `make docker-build	 `| Construire l’image Docker
  |
| `make docker-run`	   | Lancer le container Docker
  |
| `make test`	         | Exécuter les tests
  |


---
