from flask import Flask, render_template, request, abort, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    """Check if the user indicated it's their birthday."""
    name = request.form.get("name", "").strip().lower()  # Normalize input

    if not name:
        abort(400, description="Please enter 'yes' or 'no'")

    if name == "yes":
        return render_template("hello.html")
    else:
        return render_template("test.html")  # Using test.html as wait.html

@app.route("/birthday", methods=["POST"])
def birthday():
    """Render birthday greeting with the user's name."""
    name = request.form.get("name", "").strip()

    if not name:
        abort(400, description="Name is required")
    return render_template("birthday.html", name=name)

@app.route("/test", methods=["POST"])
def test():
    """Test route to display the submitted name."""
    name = request.form.get("name", "").strip()
    if not name:
        abort(400, description="Name is required")
    return render_template("test.html", name=name)

@app.route("/favicon.ico")
def favicon():
    """Serve the favicon."""
    return send_from_directory(app.static_folder, "favicon.ico", mimetype="image/vnd.microsoft.icon")

@app.errorhandler(400)
def bad_request(e):
    """Handle bad request errors."""
    return render_template("error.html", message=e.description), 400

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)