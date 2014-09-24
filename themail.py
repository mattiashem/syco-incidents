import mailchimp
from flask import Flask
from flask import render_template
import datetime
app = Flask(__name__)

def get_mailchimp_api():
	    return mailchimp.Mailchimp('XXXXXXXXXXXXXXXXXX') #your api key


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

#Create an campain
def send_campain():
    try:
        m = get_mailchimp_api()
        titel = "FareOffice Incident Started "+ str(datetime.datetime.time(datetime.datetime.now()))
        campain = campaigns = m.campaigns.create("regular",    {"list_id": "2e7142ac33", "subject":titel, "from_email":"sysop@fareoffice.com","from_name":"System Operations","template_id":"101969"}, { "html": " "})
        print campain
        sent = m.campaigns.send(campain['id'])
        return sent


    except mailchimp.Error, e:
        #messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
        print e


#Create an campain
def send_campain_resolved():
    try:
        m = get_mailchimp_api()
        titel = "FareOffice Incident Resolved"+ str(datetime.datetime.time(datetime.datetime.now()))
        campain = campaigns = m.campaigns.create("regular",    {"list_id": "2e7142ac33", "subject":titel, "from_email":"sysop@fareoffice.com","from_name":"System Operations","template_id":"102389"}, { "html": " "})
        print campain
        sent = m.campaigns.send(campain['id'])
        return sent


    except mailchimp.Error, e:
        #messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
        print e



def list_campains():
    '''
    List all campains with that id
    :return:
    '''
    try:
        campaigns =  m.campaigns.list({'campaign_id':'6034113a2c'})
        campaign = campaigns['data'][0]
        print campaign


    except mailchimp.Error, e:
        #messages.error(request,  'An error occurred: %s - %s' % (e.__class__, e))
        print e

if __name__ == "__main__":
    app.run()

#Enable to test send function
#send_campain()