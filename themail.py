
from flask import Flask
from flask import render_template
from chimp_action import *

app = Flask(__name__)




@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/fp")
def fp():
    result = send_campain('69b7c86869',"Farepayment")
    return render_template('fp.html',result=result)

@app.route("/fp_ok")
def fp_ok():
    result = send_campain_resolved('69b7c86869',"Farepayment")
    return render_template('fp.html',result=result)


@app.route("/rf")
def rf():
    result = send_campain('e5ff54afa7','Rentalfront')
    return render_template('fp.html',result=result)

@app.route("/rf_ok")
def rf_ok():
    result = send_campain_resolved('e5ff54afa7',"Rentalfront")
    return render_template('fp.html',result=result)

@app.route("/eff")
def eff():
    result = send_campain('2e7142ac33','EFF')
    return render_template('fp.html',result=result)

@app.route("/eff_ok")
def eff_ok():
    result = send_campain_resolved('2e7142ac33',"EFF")
    return render_template('fp.html',result=result)


@app.route("/pbk")
def pbk():
    result = send_campain('4a3fe182e4','PBK')
    return render_template('fp.html',result=result)

@app.route("/pbk_ok")
def pbk_ok():
    result = send_campain_resolved('4a3fe182e4',"PBK")
    return render_template('fp.html',result=result)


@app.route("/webres")
def webres():
    result = send_campain('2e7142ac33','Webres')
    return render_template('fp.html',result=result)

@app.route("/webres_ok")
def webres_ok():
    result = send_campain_resolved('2e7142ac33',"Webres")
    return render_template('fp.html',result=result)

@app.route("/static")
def static_e():
    result = send_campain('2e7142ac33','Static')
    return render_template('fp.html',result=result)

@app.route("/static_ok")
def static_ok():
    result = send_campain_resolved('2e7142ac33',"Static")
    return render_template('fp.html',result=result)

@app.route("/all")
def all():
    result = send_campain('2e7142ac33','All System')
    return render_template('fp.html',result=result)

@app.route("/all_ok")
def all_ok():
    result = send_campain_resolved('2e7142ac33',"All System")
    return render_template('fp.html',result=result)


@app.route("/panic")
def panic():
    result = "Error"
    return render_template('fp.html',result=result)



if __name__ == "__main__":
    app.run()

#Enable to test send function
#send_campain()