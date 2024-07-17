from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

table_file = pd.read_csv("Smalldata/stations.txt", skiprows=17)
table = table_file[['STAID', 'STANAME                                 ']].squeeze()

@app.route("/")
def home():
    return render_template("tutorial.html", data=table.to_html())

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    filename = f"Smalldata/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temprature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    result = {"station": station, "date": date, "temprature": temprature}
    return result


@app.route("/api/v1/<station>")
def full(station):
    filename = f"Smalldata/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    result = df.to_dict(orient="records")
    return result

@app.route("/api/v1/<station>/year/<year>")
def yearly(station, year):
    filename = f"Smalldata/TG_STAID{station.zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20)
    df['    DATE'] = df['    DATE'].astype(str)
    result = df[df['    DATE'].str.startswith(year)].to_dict(orient="records")
    return result


@app.route("/about/")
def about():
    return render_template("about.html")\

@app.route("/contact/")
def contact():
    return render_template("contact.html")\

@app.route("/store/")
def store():
    return render_template("store.html")

if __name__ == "__main__":
    app.run(debug=True)
