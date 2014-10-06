import mailchimp
from flask import Flask
from flask import render_template
from chimp_action import *
import datetime
app = Flask(__name__)




@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/fp")
def fp():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/fp_ok")
def fp_ok():
    result = "Error"
    test()
    return render_template('fp.html',result=result)


@app.route("/rf")
def rf():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/rf_ok")
def rf_ok():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/eff")
def eff():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/eff_ok")
def eff_ok():
    result = "Error"
    return render_template('fp.html',result=result)


@app.route("/pbk")
def pbk():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/pbk_ok")
def pbk_ok():
    result = "Error"
    return render_template('fp.html',result=result)


@app.route("/webres")
def webres():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/webres_ok")
def webres_ok():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/static")
def static_e():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/static_ok")
def static_ok():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/all")
def all():
    result = "Error"
    return render_template('fp.html',result=result)

@app.route("/all_ok")
def all_ok():
    result = "Error"
    return render_template('fp.html',result=result)


@app.route("/panic")
def panic():
    result = "Error"
    return render_template('fp.html',result=result)



if __name__ == "__main__":
    app.run()

#Enable to test send function
#send_campain()