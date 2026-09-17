from flask import Flask, render_template, request, jsonify

@app.route('/todo')
def todo_page():
    return render_template('todo.html')