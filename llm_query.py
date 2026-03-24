import ollama

def generate_sql(question):
    prompt=f"""
Convert the following natural language question into SQL.
Database table:
students(id,name,subject,marks)
Question: {question}
Return only SQL query.
"""
    response=ollama.chat(
        model="phi3:mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response["message"]["content"].strip()
