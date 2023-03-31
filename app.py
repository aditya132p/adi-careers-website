from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
    'id':1,
    'title': 'Software enginer',
    'location': 'Mumbai,India',
    'salary': 'Rs. 1200000'
},
    {
    'id':2,
    'title': 'Software Developer',
    'location': 'Bengular,India',
    'salary': 'Rs. 2300000'
},
{
    'id':3,
    'title': 'Data Analys',
    'location': 'Delhi,India',
    'salary': 'Rs. 1400000'
},
{
    'id':4,
    'title': 'Web Developer',
    'location': 'Pune,India',
    'salary': 'Rs. 1800000'
},
{
    'id':5,
    'title': 'FrontEnd Developer',
    'location': 'Noida,India',
    'salary': 'Rs. 1900000'
}
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

    
@app.route("/api/jobs")
def list_job():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
