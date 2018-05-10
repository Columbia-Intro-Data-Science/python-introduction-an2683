from flask import Flask, render_template, request, url_for
import datetime
from flask_sqlalchemy import SQLAlchemy
#from flask_table import Table, Col

app = Flask(__name__)
app.debug = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="an2683",
    password="101Proof",
    hostname="an2683.mysql.pythonanywhere-services.com",
    databasename="an2683$LOAD_FCAST",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

class LoadForecastUpdate(db.Model):

    __tablename__ = "LoadForecastUpdate"

    Date = db.Column(db.Date, primary_key=True)
    HE= db.Column(db.Integer, primary_key=True)
    Zone = db.Column(db. String(4096), primary_key=True)
    Forecast_Demand_MW= db.Column(db.DECIMAL)
    Forecast_Temp_DryBulb_F = db.Column(db.DECIMAL)

#engine = create_engine(SQLALCHEMY_DATABASE_URI)

# class LoadForecastUpdate(db.Model):
#     __tablename__ = "LoadForecastUpdate"
#     he = db.Column(db.Integer,db.ForeignKey("LoadForecastUpdate.HE"),primary_key=True)
# #     zne = db.Column(db.VarChar(255,db.ForeignKey("LoadForecastUpdate.Zone"),primary_key=True)
comments = []
@app.route('/', methods=['GET'])
def dropdown():
    regions = ['ISONE', '.Z.CONNECTICUT', '.Z.MAINE', '.Z.NEMASSBOST','.Z.NEWHAMPSHIRE','.Z.RHODEISLAND','.Z.SEMASS','.Z.VERMONT','	.Z.WCMASS']
    today = datetime.date.today( )
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    dates = [yesterday, today, tomorrow]

    return render_template('regions.html', regions=regions,dates=dates)

@app.route("/query_results" , methods=['GET', 'POST'])
def query_results():
    reg = request.form.get('regions')
    dt = request.form.get('dates')
    #return(str(reg) + " " + str(dt)) # just to see what select is
    #cur = db.cursor()
    #cur.execute("Select * from LoadForecastUpdate;")
    #data=cur.fetchall()
    # comment = Comment(content=request.form["contents"])
    # db.session.add(comment)
    # db.session.commit()

    return render_template('query_results.html', comments=LoadForecastUpdate.query.filter_by(Zone=reg,Date=dt))
    #return("Hello Jersey City") # just to see what select is

# @app.route('/', methods=['GET'])
# def dropdown1():
#     today = datetime.date.today( )
#     yesterday = today - datetime.timedelta(days=1)
#     tomorrow = today + datetime.timedelta(days=1)
#     dates = [yesterday, today, tomorrow]
#     return render_template('regions.html', dates=dates)
# @app.route("/")
# def hello():
#     return "Hello Jersey City 2!"

if __name__ == "__main__":
    app.run()