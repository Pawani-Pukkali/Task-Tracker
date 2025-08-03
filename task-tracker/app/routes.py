# this file is flask application routes
from flask import Blueprint, render_template, request, redirect

main = Blueprint('main', __name__)

tasks = []

@main.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect('/')
    return render_template('index.html', tasks=tasks)
