# flask-postgres
Simple Flask API with a Postgres Database

#### Setup (Flask-app/Docker only):
1. Install Docker Desktop: https://docs.docker.com/docker-for-mac/install/
2. Clone this Repo: <code>$ git clone https://github.com/pogzyb/flask-postgres.git</code>
3. Run: <code>$ docker-compose up --build</code>

#### Setup (Using Terraform in AWS)
1. Make an AWS account
2. Install Terraform
3. 

#### Usage:<br>

1. Open a new python shell: <code>$ python </code>
2. POST (add a new person)
<pre><code>import requests

r = requests.post(
  url="http://localhost:5000/new",
  json={"name": "joe"}
)

print(r.json())
// copy the uid!
</code></pre>

3. GET (retrieve data about a person)
<pre><code>import requests

uid = "<_paste_uid_here_>"
r = requests.get(
  url="http://localhost:5000/one/{0}".format(uid)
)

print(r.json())
// data for an individual person
</code></pre>
