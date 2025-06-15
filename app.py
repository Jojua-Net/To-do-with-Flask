from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_all_tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, is_done FROM todos")
    tasks = c.fetchall()
    conn.close()
    return tasks

@app.route("/")
def home():
    tasks = get_all_tasks()

    return render_template("home.html", tasks=tasks)



def add_task(task_text):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos (task) VALUES (?)", (task_text,))
    conn.commit()
    conn.close()

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        task_text = request.form["task"]
        if task_text.strip():
            add_task(task_text)
        return redirect("/")
    
    return render_template("add.html")



def delete_task(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM todos WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()


@app.route("/delete/<int:task_id>")
def delete(task_id):
    delete_task(task_id)
    return redirect("/")




def mark_done(task_id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE todos SET is_done = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

@app.route("/done/<int:task_id>")
def done(task_id):
    mark_done(task_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)