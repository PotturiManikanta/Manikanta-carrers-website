from flask import *

app = Flask(__name__)


JOBS=[
  {
  'id':1,
  'title':'Java',
  'location':'Online',
  'salary':'Rs.10,000'
},
{
  'id':2,
  'title':'Python',
  'location':'Offline',
  'salary':'Rs.20,000'
},
{
  'id':3,
  'title':'Fullstack',
  'location':'Online',
  'salary':'Rs.70,000'
},
{
  'id':4,
  'title':'Datastructures',
  'location':'Online',
  'salary':'Rs.50,000'
}
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS,company_name='Manikanta')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
