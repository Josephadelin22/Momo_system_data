# Momo_system_data

.
├── README.md                d’exécution, aperçu du projet
├── .env.example            # Exemple de variables d’environnement (DB_URL, API_KEY, etc.)
├── requirements.txt        # Dépendances Python (lxml, dateutil, sqlite-utils, FastAPI en option)
├── index.html              # Point d’entrée statique du tableau de bord
│
├── web/                    # Frontend (statique)
│   ├── styles.css          # Styles globaux
│   ├── chart_handler.js    # JS pour graphiques, fetch JSON, rendering DOM
│   └── assets/             # Images/icônes (optionnel)
│
├── data/                   # Données brutes, transformées et base de données
│   ├── raw/                # Entrées XML (à ignorer dans git)
│   │   └── momo.xml
│   ├── processed/          # Données prêtes pour le dashboard
│   │   └── dashboard.json
│   ├── db.sqlite3          # Base SQLite locale
│   └── logs/               # Logs et erreurs
│       ├── etl.log
│       └── dead_letter/    # XML rejetés ou malformés
│
├── etl/                    # Pipeline ETL
│   ├── __init__.py
│   ├── config.py           # Paramètres (seuils, mappings, chemins)
│   ├── parse_xml.py        # Parsing XML avec ElementTree/lxml
│   ├── clean_normalize.py  # Normalisation montants, dates, numéros
│   ├── categorize.py       
│   ├── load_db.py           
│   └── run.py              
│
├── api/                    
│   ├── __init__.py
│   ├── app.py              
│   ├── db.py                
│   └── 
│
├── scripts/                # Scripts shell pratiques
│   ├── run_etl.sh          # Lance ETL complet sur un XML donné
│   ├── export_json.sh      # Regénère dashboard.json
│   └── serve_frontend.sh   # Démarre un petit serveur HTTP (ou Flask statique)
│
└── tests/                 
    ├── test_parse_xml.py
    ├── test_clean_normalize.py
    └── test_categorize.py


Prjoject board: [scrum Board] (https://github.com/Josephadelin22/Momo_system_date/projects/1)
