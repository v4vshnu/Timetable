from flask import Flask, jsonify, redirect, render_template, request

app=Flask(__name__)


@app.route("/")
def hello():
    return redirect("/table")

@app.route("/table", methods=["GET"])
def gen():
    return render_template("index.html")

@app.route("/table", methods=["POST"])
def generate():
    cell=[]
    cell.append(request.form.get("A"))
    cell.append(request.form.get("B"))
    cell.append(request.form.get("C"))
    cell.append(request.form.get("D"))
    cell.append(request.form.get("E"))
    cell.append(request.form.get("F"))
    cell.append(request.form.get("G"))
    cell.append(request.form.get("H"))
    return render_template("table.html",data=cell)

if __name__=='__main__':
    app.run(port=5001)