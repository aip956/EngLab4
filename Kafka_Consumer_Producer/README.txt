To run:
cd into Kafka_Consumer_Producer

In terminal:
Start/build the container:
docker-compose up -d
Start the app:
uvicorn main:app --reload
uvicorn app.main:app --reload (if in the app dir)
(needed to pip install uvicorn fastaip aiokafka)
Access FastAPI Swagger:
http://127.0.0.1:8000/docs
http://localhost:8000/docs

Post a message:
topic: my_topic
message: Hello Kafka!
Should return code 200


Get the consumed messages:
Get, execute
{
  "messages": [
    {
      "topic": "my_topic",
      "message": "Hello Kafka!"
    }
  ]
}

Stop process in foreground:
Control-C 
Gracefully shut down:
docker-compose stop
Remove containers:
docker-compose down

in eng4 repo; just once
git branch --set-upstream-to=origin/<remote_branch_name> <local_branch_name>


git checkout main (to make sure I'm in main)
Make a branch:
git pull (most up to date files)
git checkout -b anthea/subject (creates the branch)

In branch:
git add .
git commit -m "message"
git push 

pull request (pull from my branch to main):
git merge (harder; can do in gui)

sorting/streams in topics of events
meet on monday
