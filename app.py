from flask import Flask, render_template, request

from workouts import WorkoutFactory

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    plan, error = None, None
    if request.method == "POST":
        try:
            workout = WorkoutFactory.create(
                request.form["kind"], request.form["level"]
            )
            plan = workout.plan()
        except ValueError as e:
            error = str(e)
    return render_template("index.html", plan=plan, error=error)


if __name__ == "__main__":
    app.run(debug=True)