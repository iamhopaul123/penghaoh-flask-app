from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__, static_folder='my-app')

@app.route("/")
def healthcheck():
    ## print the guestbook
    return render_template("admin.html", entries=model.get_entries())

@app.route("/my-app/")
def admin():
    ## print the guestbook
    return render_template("admin.html", entries=model.get_entries())

@app.route("/my-app/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/my-app/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model.add_entry(name, message)
    return redirect("/my-app")

@app.route("/my-app/delete", methods=["POST"])
def deleteentry():
    id_value = request.form["id"]
    model.delete_entry(id_value)
    return redirect("/my-app")

if __name__=="__main__":
    model.init()
    app.run(debug=True, host='0.0.0.0')
