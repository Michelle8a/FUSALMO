#pip install pymongo
import pymongo 

user = "UserCluster"
password = "PassCluster"

url = "mongodb+srv://"+user+":"+password+"@micluster.uxuewyn.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(url)
