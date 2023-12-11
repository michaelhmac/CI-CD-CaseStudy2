from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store (replace with a database in a real application)
tasks = [
    {"id": 1, "title": "Task 1", "description": "Description for Task 1"},
    {"id": 2, "title": "Task 2", "description": "Description for Task 2"}
]

# Display all tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# Display a form to create a new task
@app.route('/create')
def create():
    return render_template('create.html')

# Add a new task
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    description = request.form['description']
    new_task = {"id": len(tasks) + 1, "title": title, "description": description}
    tasks.append(new_task)
    return redirect(url_for('index'))

# Display details of a task
@app.route('/<int:task_id>')
def detail(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return render_template('detail.html', task=task)
    else:
        return 'Task not found', 404

# Display a form to edit a task
@app.route('/<int:task_id>/edit')
def edit(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return render_template('edit.html', task=task)
    else:
        return 'Task not found', 404

# Update a task
@app.route('/<int:task_id>/update', methods=['POST'])
def update(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        return redirect(url_for('index'))
    else:
        return 'Task not found', 404

# Delete a task
@app.route('/<int:task_id>/delete')
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

