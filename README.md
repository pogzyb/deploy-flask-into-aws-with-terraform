# Flask and Postgres (with Docker and Terraform!)
Here is a simple Flask Application connected to a Postgres Database...
(and it's Containerized with Docker and deployable with Terraform in AWS!)

#### Local Setup (Flask-app/Docker only):
1. Install Docker Desktop: https://docs.docker.com/docker-for-mac/install/
2. Clone this Repo: <code>$ git clone https://github.com/pogzyb/flask-postgres.git</code>
3. Run: <code>$ docker-compose up --build</code>

#### AWS Setup (Using Terraform in AWS)
1. Make an AWS account
2. Install Terraform
3. <code>$ cd terraform</code>
4. <code>$ terraform apply</code>

#### Application Usages:<br>

As a Web App:
1. Start the services with docker-compose
2. Navigate to http://localhost:8080/
3. Click buttons!


As an API:
1. Start the services with docker-compose
2. Open a new python shell: <code>$ python </code>
3. POST (add a new person)
<pre><code>import requests

r = requests.post(
  url="http://localhost:5000/new",
  json={"name": "joe"}
)

print(r.json())
// copy the uid!
</code></pre>

4. GET (retrieve data about a person)
<pre><code>import requests

uid = "<_paste_uid_here_>"
r = requests.get(
  url="http://localhost:5000/one/{0}".format(uid)
)

print(r.json())
// data for an individual person
</code></pre>
