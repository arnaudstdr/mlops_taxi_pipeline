# MLOps Taxi Pipeline

[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-%2019.03%2B-blue?logo=docker)](https://www.docker.com/)
[![MLflow](https://img.shields.io/badge/MLflow-2.0+-orange?logo=apache)](https://mlflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.0-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Grafana](https://img.shields.io/badge/grafana-%209.0%2B-F46800?logo=grafana)](https://grafana.com/)
[![Last Commit](https://img.shields.io/github/last-commit/arnaudstdr/mlops_taxi_pipeline)](https://github.com/arnaudstdr/mlops_taxi_pipeline/commits)
[![GitHub Stars](https://img.shields.io/github/stars/arnaudstdr/mlops_taxi_pipeline?style=social)](https://github.com/arnaudstdr/mlops_taxi_pipeline/stargazers)


**Un pipeline MLOps end-to-end pour la prédiction de courses de taxi, avec monitoring avancé et détection de dérive.**

---

## 📌 Description

Ce projet implémente un **pipeline MLOps complet** pour entraîner, déployer et monitorer un modèle de prédiction de prix ou de demande de course de taxi. Le pipeline est conçu pour être **reproductible, scalable et maintenable**, en intégrant : 
- Prétraitement des données
- Entraînement et fine-tuning d'un modèle (LLM ou classique)
- Déploiement en production avec une API FastAPI
- Monitoring en temps réel (métriques, dérive des données/modèle)
- Infrastructure as Code (Docker, Kubernets, Terraform)

**objectif** : Montrer aux recruteurs la maîtrise des enjeux d'industrialisation des modèles de machine learning.

---

## 🔧 Stack Technique

| Composant | Technologie
| --------- | -----------
| Orchestration | MLflow + Kubeflow (ou Airflow)
| Infrastructure | Docker + Kubernetes (ou Terraform)
| Monitoring | Prometheus + Grafana (métriques), Evidently/Arize (dérive)
| Déploiement | FastAPI, GCP/AWS
| Modèle | Fine-tuning d’un petit LLM (Hugging Face) ou modèle classique
| Données | Dataset public (NYC Taxi Dataset)

---

## 📁 Structure du Projet

```mlops_taxi_pipeline/
├── data/                  # Données brutes et prétraitées
├── notebooks/             # Explorations et prototypage
├── src/
│   ├── preprocessing/     # Scripts de prétraitement
│   ├── training/          # Scripts d'entraînement
│   ├── deployment/        # API FastAPI et Dockerfiles
│   ├── monitoring/        # Dashboards Grafana/Evidently
│   └── tests/             # Tests unitaires et d'intégration
├── .github/               # Workflows CI/CD
├── docker-compose.yml     # Configuration Docker
├── requirements.txt       # Dépendances Python
├── README.md              # Ce fichier
└── LICENSE                # Licence du projet
```

--- 

## ⚙️ Prérequis
- Python 3.10+
- Docker & Docker Compose
- Compte GCP ou AWS (pour le déploiement cloud)
- Outils : `mlflow`, `kubectl`, `terraform` (optionnel)

### Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/arnaudstdr/mlops_taxi_pipeline.git
cd mlops_taxi_pipeline
   ```

2. Installer les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

3. Configurer les variables d'environnement (ex : .env) pour accès cloud et API. 

---

## 🚀 Utilisation

### 1. Prétraitement des Données
```bash
python src/preprocessing/preprocess.py --input data/raw/taxi_data.csv --output data/processed/
```

### 2. Entraînement du Modèle
```bash
mlflow run src/training -P data_path=data/processed/
```

### 3. Déploiement
- **Localement** avec Docker :
```bash
docker-compose up --build
```
L'API sera disponible sur `http://localhost:8000`.

- **Sur le cloud** (GCP/AWS) :
```bash
# Exemple avec Terraform
cd infrastructure/
terraform init && terraform apply
```

### 4. Monitoring
- Accéder à Grafana : 
```bash
kubectl port-forward svc/grafana 3000:3000
```
Ou via l'URL du service cloud. 

---

## 📊 Monitoring et Dérive
- **Métriques** : Latence, précision, taux d'erreur (Prometheus + Grafana). 
- **Dérives** : Détection automatique des dérives de données/modèle avec Evidently. 
- **Alerts** : Configurées pour notifier en cas de dérive ou de dégradation des performances. 

---

## 🎯 Livrables
- [ ] Dépôt GitHub structuré et documenté
- [ ] Pipeline reproductible et scalable
- [ ] Dashboard de monitoring (Grafana, Evidently)
- [ ] Article technique (Medium/Dev.to)

---

## 🤝 Contribution
Les contributions sont les bienvenues ! Ouvrez une **issue** ou soumettez une **pull request**.

--- 
## 📜 Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---
## 📬 Contact
Arnaud Stadler - [Portfolio](https://arnaud-stadler.com) - [LinkedIn](https://www.linkedin.com/in/arnaud-stadler-89a2322ba/) - [GitHub](https://github.com/arnaudstdr) - [mail](mailto:arnaud.stadler@ikmail.com)
