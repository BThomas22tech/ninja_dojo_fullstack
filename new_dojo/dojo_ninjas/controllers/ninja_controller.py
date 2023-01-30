from dojo_ninjas import app
from flask import render_template,redirect,request
from dojo_ninjas.models import ninjas_model, dojo_model
from dojo_ninjas.models.dojo_model import Dojo
from dojo_ninjas.models.ninjas_model import Ninja



@app.route("/dojo/new_ninja")
def new_ninja():
    dojo = Dojo.get_all()
    return render_template("new_ninjas.html", dojo = dojo)



@app.route("/dojo/new_ninja_created", methods = ["POST"])
def created_ninja():
    Ninja.save(request.form)
    return redirect("/dojo")

@app.route("/dojo/ninja_edit/<int:id>")
def edit_ninja(id):
    
    dojo = Dojo.get_all()
    ninja = Ninja.get_one_ninja(id)
    return render_template("update_ninja.html",  dojo = dojo, ninja = ninja)

@app.route("/dojo/ninja_edited/<int:id>", methods = ['POST'])
def edited_ninja(id):
    data ={
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age" : request.form["age"]
        }
    Ninja.edit_ninja(data)
    ninja_data = Ninja.get_one_ninja(id)
    # Ninja.dojo.id
    return redirect(f'/dojo/{ninja_data.dojo}')

@app.route("/dojo/delete_ninja/<int:id>")
def delete_ninja(id):
    data ={
        "id":id
    }
    Ninja.delete_ninja(data)
    return redirect("/dojo/")