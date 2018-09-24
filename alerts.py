import pymongo
import time
import sendgrid
import os
from sendgrid.helpers.mail import *
# pprint library is used to make the output look more pretty
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
try:
    client = pymongo.MongoClient("mongodb://rahulvyas:" + os.environ.get('MONGODB_PASSWORD') + "@cluster0-shard-00-00-xagmg.mongodb.net:27017,cluster0-shard-00-01-xagmg.mongodb.net:27017,cluster0-shard-00-02-xagmg.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
    db=client['test_db']

    collection = db['test_collection']
    posts = db.posts

    def read():
        #pending = collection.find({"status":"pending"})
        pending = collection.find()
        for tx in pending:
            print(tx)
    
    read()

except:
    print("MONGODB_PASSWORD envt variable not set!")





def recurring_read():
    for i in range(1,3):
        read()
        time.sleep(5)


#recurring_read()


def send_email():

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("rahul.class@gmail.com")
    to_email = Email("rahulvyas@plaak.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


#send_email()


#export MONGODB_PASSWORD=Your mongodb password here
#os.environ.get('MONGODB_PASSWORD')