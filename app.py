from flask import Flask, request, render_template_string
import yaml

app = Flask(__name__)

HTML = """
<h2>Vulnerable Flask Demo</h2>
<form method="POST">
    <textarea name="data" rows="10" cols="40"></textarea><br><br>
    <button type="submit">Parse YAML</button>
</form>

{% if result %}
<h3>Parsed Output:</h3>
<pre>{{ result }}</pre>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        user_input = request.form.get("data")

        # Intentionally vulnerable usage
        result = yaml.load(user_input)

    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(debug=True)
