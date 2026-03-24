# Natural Language Database Query System using LLMs

## 🚀 Overview

This project enables users to interact with a database using natural language queries instead of writing SQL manually.
User input in plain English is processed using an LLM (via Ollama) and converted into executable SQL queries, which are then run on a MySQL database.

---

## ✨ Features

* Convert natural language queries into SQL using LLM (Ollama)
* Execute SQL queries dynamically on a MySQL database
* Web interface for entering queries and viewing results
* Flask backend for handling requests and database communication

---

## 🛠 Tech Stack

* **Backend:** Flask (Python)
* **Database:** MySQL
* **LLM Integration:** Ollama
* **Frontend:** HTML, CSS
* **Libraries:** requests, python-dotenv

---

## 📂 Project Structure

```
Project_root/
├── app.py              # Main Flask application
├── llm_query.py        # Handles LLM-based query generation
├── database.sql        # Database schema and sample data
├── templates/          # HTML templates
├── static/             # CSS files
├── requirements.txt    # Dependencies
├── .gitignore
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/anagh-guptaa/nl-db-query-llm.git
cd nl-db-query-llm
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Configure environment variables

Create a `.env` file in the root directory and add:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=yourdbname
```

> ⚠️ Note: `.env` is not included in the repository for security reasons.

---

### 4. Setup the database

* Open MySQL
* Create a database
* Import the `database.sql` file

Example:

```
SOURCE database.sql;
```

---

### 5. Run the application

```
python app.py
```

---

## 🔄 How It Works

1. User enters a natural language query through the UI
2. Query is sent to the LLM (Ollama)
3. LLM converts it into SQL
4. SQL query is executed on the MySQL database
5. Results are fetched and displayed to the user

---

## 📌 Current Improvements

* Improving accuracy of generated SQL queries
* Enhancing error handling for invalid inputs
* Optimizing response time

---

## 🚀 Future Enhancements

* Chat-based interface for better user interaction
* Support for complex multi-step queries
* Role-based authentication and access control
* Integration with multiple database types

---

## 📎 Notes

* Ensure Ollama is running locally before executing queries
* Database must be active and accessible
* This project demonstrates integration of LLMs with real-world backend systems

---

## 👨‍💻 Author

anagh-guptaa
GitHub: https://github.com/anagh-guptaa

