from db import *
from flask import request, jsonify


@app.route("/todos", methods=["GET", "POST"])
def all_todos():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM todos")
        todos = [
            dict(id=row[0], title=row[1], description=row[2], done=row[3])
            for row in cursor.fetchall()
        ]
        if todos is not None:
            return jsonify(todos)

    if request.method == "POST":
        print("get post req")
        title = request.form["title"]
        description = request.form["description"]
        done = request.form["done"]
        sql = "INSERT INTO todos (title, description, done) VALUES (?, ?, ?)"
        cursor = cursor.execute(sql, (title, description, done))
        conn.commit()

        return f"{cursor.lastrowid}"


@app.route("/todo/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_todo(id):
    conn = db_connection()
    cursor = conn.cursor()
    todo = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM todos WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            todo = r
        if todo is not None:
            return jsonify(todo), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = "UPDATE todos SET title=?, description=?, done=? WHERE id=?"
        title = request.form["title"]
        description = request.form["description"]
        done = request.form["done"]
        updated_todo = {
            "id": id,
            "title": title,
            "description": description,
            "done": done
        }
        conn.execute(sql, (title, description, done, id))
        conn.commit()
        return jsonify(updated_todo)

    if request.method == "DELETE":
        sql = "DELETE FROM todos WHERE id=?"
        conn.execute(sql, (id,))
        conn.commit()
        return f"{id}", 200


if __name__ == "__main__":
    app.run(debug=True)