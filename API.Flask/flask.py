from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []


def find_task(id):
    for i in range(len(tasks)):
        if tasks[i]["task-id"] == id:
            return tasks[i]
        else:
            return None


@app.route("/tasks", methods=["GET"])
def all_tasks():
    return jsonify({"all_tasks": tasks}), 200


@app.route("/tasks/<int:id>", methods=["GET"])
def show_task(id):
    task = find_task(id)
    if task is None:
        return jsonify({"error": "there are no tasks with this ID"}), 404
    return jsonify({f"task {id}": task}), 200


@app.route("/tasks", methods=["POST"])
def create_new_task():
    task_title, task_description = request.json.get("title"), request.json.get(
        "description"
    )
    if task_title is None or task_description is None:
        return jsonify({"error": "not enough data"}), 400
    new_task = {
        "descpition": task_description,
        "task-id": (len(tasks) + 1),
        "title": task_title,
    }

    tasks.append(new_task)

    return jsonify(new_task), 200


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = find_task(id)
    if task is None:
        return jsonify({"error": "there are no tasks with this ID"}), 404

    tasks.remove(task)
    return jsonify({"success": "task deleted successfully"}), 200


if __name__ == "__main__":
    app.run()
