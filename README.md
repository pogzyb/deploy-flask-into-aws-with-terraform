# flask-postgres
Simple Flask application/api with a Postgres database

#### Setup:
1. Install Docker Desktop: https://docs.docker.com/docker-for-mac/install/
2. Clone this Repo: <code>$ git clone https://github.com/pogzyb/flask-postgres.git</code>
3. Run: <code>$ docker-compose up --build</code>

#### Usage:<br>

<b>-- UI</b>
1. Navigate to localhost:5000
2. Submit a name in the form
3. Return to localhost:5000
4. List of People will be updated

<b>-- API</b>
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
