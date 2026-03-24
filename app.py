from flask import Flask,render_template,request
import MySQLdb
from llm_query import generate_sql
import os
from dotenv import load_dotenv
load_dotenv()

app=Flask(__name__)

def get_db():
    return MySQLdb.connect(host="localhost",user="root",passwd=os.getenv("SQL_PASSWORD"),db="nl_database")

@app.route("/", methods=["GET","POST"])
def home():
    result=None
    query=None
    if request.method=="POST":
        question=request.form["question"]
        query=generate_sql(question)
        db=get_db()
        cur=db.cursor()
        cur.execute(query)
        result=cur.fetchall()
        cur.close()
        db.close()
    return render_template("index.html",query=query,result=result)

if __name__=="__main__":
    app.run(debug=True)

