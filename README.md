# MoMo SMS Data Processing  

##  Team Information  
**Team Name:** Team 8  
**Members:**  
- Adeleye Ayomide  (Adeleye11)  
- Joseph BOUSSAMBA (Josephadelin22)  
- Denyse Ishimirwe (denyseishimirwe)
- Yves Niyenga  

---

##  Project Description  
This project is about building an **enterprise-level fullstack application** to process MoMo SMS transaction data.  

- **Extract**: Get SMS transaction data in XML format  
- **Transform**: Clean, normalize, and categorize transactions  
- **Load**: Store processed data into a relational database (SQLite)  
- **Visualize**: Build a frontend dashboard for analysis  

The backend ETL pipeline is powered by **Python**, while the frontend uses **HTML, CSS, and JavaScript**. An optional **FastAPI API** may provide analytics endpoints.  

---

##  High-Level System Architecture  
The system works as follows:  

**MoMo SMS (XML Data)** → **Python ETL Pipeline** → **SQLite Database** → **Processed JSON** → **Frontend Dashboard**  
*(Optional: SQLite Database → FastAPI API → Frontend Dashboard)*  

 View the full diagram here: https://drive.google.com/file/d/1xx-heJHO9eU-H6tWehh43LTSADeKwxJS/view?usp=drive_link  



---

##  Scrum Board  
We are following **Agile practices** using a Scrum board with three columns:  

- **To Do**  
- **In Progress**  
- **Done**  

 View our Scrum board here: https://trello.com/invite/b/68c0647b4b690ae71b0f7762/ATTIa64c805b0b4ae3e26abb6731bbe71930189BB9AC/group-8-scrum-board  
 

---

##  Project Organization  
Our repo follows this structure:  

```
├── README.md # Setup, run, overview
├── .env.example # DATABASE_URL or path to SQLite
├── requirements.txt # Dependencies
├── index.html # Dashboard entry (static)
├── web/
│ ├── styles.css # Dashboard styling
│ ├── chart_handler.js # Fetch + render charts/tables
│ └── assets/ # Images/icons (optional)
├── data/
│ ├── raw/ # Provided XML input (git-ignored)
│ ├── processed/ # Cleaned/derived outputs for frontend
│ ├── logs/
│ │ └── dead_letter/ # Unparsed/ignored XML snippets
├── etl/ # Python ETL pipeline
├── api/ # Optional FastAPI service
├── scripts/ # Automation scripts
└── tests/ # Unit tests
```


---

##  Deliverables (Week 1)  
-  GitHub repository created with teammates added  
-  Project structure organized  
-  High-level system architecture diagram added  
-  Scrum board link shared in README  

---

# MoMo SMS Data Processing – Week 2  

## Project Description  
This project is about building an **enterprise-level fullstack application** to process MoMo SMS transaction data.  

In Week 2, our focus was on **Database Design and Implementation**, ensuring the system can efficiently store, query, and analyze mobile money transactions. The core work included:  

- Designing a complete **Entity Relationship Diagram (ERD)**.  
- Implementing the **MySQL database schema** with proper constraints and indexes.  
- Creating **JSON schemas** to represent entities and simulate API responses.  
- Producing full **database design documentation**, including rationale, data dictionary, sample queries, and constraints.  
- Updating our **Scrum board** to reflect completed tasks and new sprints.  

---

## Database Design (ERD)  
We created an ERD with the following entities and relationships:  

- **Users** → stores customer information.  
- **Transactions** → stores transaction records linked to users and categories.  
- **Categories** → holds transaction types (Debit, Credit, Airtime, etc.).  
- **System Logs** → records transaction log events for traceability.  

[ERD Diagram](docs/ERD_Diagram.jpg)  

---

## Database Implementation (MySQL)  
We implemented the database schema in MySQL with:  
- **Primary Keys and Foreign Keys** for referential integrity.  
- **CHECK constraints** to prevent invalid data.  
- **Indexes** for faster queries.  
- **Sample test data** (5 records per main table).  

[SQL Script](database/database_setup.sql)  

---

## JSON Data Modeling  
We built JSON schemas for each entity:  
- **User**  
- **Category**  
- **Transaction**  
- **System Log**  
- **Transaction Full** (nested object with user, category, and logs)  

[JSON Schemas](examples/json_schemas.json)   

---

## Documentation  
All detailed documentation is compiled in a single PDF file containing:  
- ERD with rationale and design decisions  
- Data dictionary (tables, attributes, and descriptions)  
- SQL ↔ JSON mapping  
- Sample queries with results  
- Security & accuracy rules (constraints)  

📄 Documentation: `docs/database_design_documentation.pdf`  

---

## Scrum Board  
We continued using Agile practices and updated our Scrum board for Week 2.  

📌 View our Scrum board: [Team 8 Scrum Board](https://trello.com/invite/b/68c0647b4b690ae71b0f7762/ATTIa64c805b0b4ae3e26abb6731bbe71930189BB9AC/group-8-scrum-board)  

---  


