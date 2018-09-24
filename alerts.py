import pymongo
import time
import sendgrid
import os
from sendgrid.helpers.mail import *


#### COMMANDS FOR ENVT. VAR ####
# echo "MONGODB_PASSWORD='YOUR PASSWORD HERE'" > mongodb.env
# echo "mongodb.env" >> .gitignore
# source ./mongodb.env

# settings.py
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity:
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / 'mongodb.env'
load_dotenv(dotenv_path=env_path)

def read():
    #pending = collection.find({"status":"pending"})
    pending = collection.find()
    for tx in pending:
        print(tx)
        send_email(str(tx))

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
try:
    client = pymongo.MongoClient("mongodb://rahulvyas:" + os.environ.get('MONGODB_PASSWORD') + "@cluster0-shard-00-00-xagmg.mongodb.net:27017,cluster0-shard-00-01-xagmg.mongodb.net:27017,cluster0-shard-00-02-xagmg.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
    db=client['test_db']

    collection = db['test_collection']
    posts = db.posts
    
    read()
    
except:
    print("MONGODB_PASSWORD envt variable not set!")


def recurring_read():
    for i in range(1,3):
        read()
        time.sleep(5)


def send_email(pendingrequest):

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("rahulvyas@plaak.com")
    to_email = Email("chaishepherd@plaak.com")
    subject = "TEST Alert: Pending " + "ETH" + "request"
    content = Content("text/plain", "This mail is an alert for the pending withdrawal request" + pendingrequest)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)

