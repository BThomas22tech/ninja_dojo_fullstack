from dojo_ninjas import app
from flask import render_template,redirect,request
from dojo_ninjas.models.dojo_model import Dojo
from dojo_ninjas.models.ninjas_model import Ninja


@app.route("/dojo")
def index():
    dojo = Dojo.get_all()
    
    return render_template("index.html", dojo = dojo)


@app.route("/dojo/new_dojo", methods = ['POST'])
def new_dojo():
    data ={
        "name": request.form['name']
    }
    Dojo.save_dojo(data)
    return redirect('/dojo')

@app.route("/dojo/<int:id>")
def show_ninja(id):
    data = {'id':id}
    ninja = Ninja.show_ninjas(data)
    
    
    return render_template("ninjas_in_dojo.html", ninja = ninja, dojo = Dojo.get_dojo_with_ninjas(data))
