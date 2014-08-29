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
    result = send_campain()
    return render_template('fp.html',result=result)

@app.route("/fp-ok")
def fp_ok():
    result = send_campain_resolved()
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