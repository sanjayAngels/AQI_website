from flask import Flask , render_template 






app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Product and Services")
def product():
    return render_template("product.html")

@app.route("/Partner")
def partner():
    return render_template("partner.html")

if __name__ == "__main__":
    
    app.run("0.0.0.0", port=8500, debug=True)
    