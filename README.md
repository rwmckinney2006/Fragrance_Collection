# Fragrance Collection Database
A  Streamlit app for storing and visualizing fragrance collection in Python and MySQL.

**[Live Demo](https://fragrancecollection.streamlit.app/)**

---

## Features
- Store fragrance collection in MySQL database.
- Attributes including name, brand, notes, size, concentration, retail price, season and image path.
- Secure .env file for database information.
- Python scripts to connect MySQL database to convert to .csv file.
- Streamlit app connection in .py file.
- Streamlit UI to display fragrance details, images and links.

---

## Tech Stack
**Languages & Environments**
- Python 3.13.5
- Jupyter Kernel: Python 3.12.12 (Anaconda)
- MySql 8.4.0

**Libraries**
- mysql-connector-python
- python-dotenv
- Streamlit 
- Pandas

**Tools**
- VS Code
- Git + Github

---

## How It Works
1. Build fragrance database in MySQL.
2. Jupyter Notebook to connect database to python using mysql-connector-python and convert database to .csv file using pandas.
3. Jupyter Notebook to add optional link column to .csv file and Streamlit to display database details, images and links.

---

## How to Run It

### Prerequisites
- Python 3.12 or higher
- MySQL 8.4.0 or higher 

### Installation Steps

1. **Clone The Repository**
```bash
    git clone https://github.com/rwmckinney2006/Fragrance_Collection.git
    cd Fragrance_Collection
```
2. **Install Required Dependencies**
```bash
    pip install mysql-connector-python python-dotenv streamlit pandas
```

3. **Set Up MySQL Database**
- Create a new database in MySQL:
```sql
    CREATE DATABASE fragrance_database;
```
- Import the database schema:
```bash
    mysql -u your_username -p fragrance_schema.sql
```

4. **Configure Environment Variables**
- Create a `.env` file in the project root directory
- Add your database credentials:
```
    DB_HOST=localhost
    DB_USER=your_mysql_username
    DB_PASSWORD=your_mysql_password
    DB_NAME=fragrance_database
```

5. **Run The Application**
```bash
    streamlit run fragrance_app.py
```

---

## Troubleshooting
- if you encounter MySQL connection erros, verify your credentials in the `.env` file.
- Ensure MySQL service is running on your machine.
- Check that all dependencies are installed with `pip list`.