from flask import Flask, render_template_string
import random

app = Flask(__name__)

# Dane: przedrostki, rdzenie i końcówki
przedrostki = ["Tralalero", "Bombardiro", "Brr Brr", "Tung Tung", "Lirili", "Chippini", "Biscottino"]
rdzen = ["Tralala", "Crocodilo", "Patapim", "Cappuccina", "Gusini", "Larilà"]
koncowki = ["ini", "ello", "ino", "ona", "oni", "one", "etto", "ina", "ara", "ara"]

# Funkcja generująca nazwę brainrot
def generuj_brainrot():
    p = random.choice(przedrostki)
    r = random.choice(rdzen)
    if random.random() < 0.6:
        return f"{p} {r}"
    else:
        return r + random.choice(koncowki)

# Strona główna z przyciskiem "Generate!"
HTML = """
<!doctype html>
<title>Italian Brainrot Generator</title>
<h1>🇮🇹 Italian Brainrot Name Generator</h1>
<p><strong>{{ name }}</strong></p>
<form method="post">
    <button type="submit">Generuj nową nazwę</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    name = generuj_brainrot()
    return render_template_string(HTML, name=name)

if __name__ == "__main__":
    app.run(debug=True)
