import pymongo
import json
from pymongo import MongoClient


# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["GuviGeek"]
collection = db["GeekNetwork"]


with open(r"C:/Users/Senthil/STUDENTS.json") as f:
    for file in f:
        myDict = json.loads(file)
        print(myDict)
        
        
'''
    

Tot_sum=collection.aggregate([{"$unwind":"$scores"}, {"$group":{
                               "_id":"$_id",
                               "Total":{"$sum":"$scores.score"}}
                               
                                }])
for i in Tot_sum:
    print(i)
    '''


'''    
 
Agg_sum=collection.aggregate([{"$unwind":"$scores"}, {"$group":{
                               "_id":"$name",
                               "Average":{"$avg":"$scores.score"}}
                               
                                }])
for i in Agg_sum:
    print(i)
    '''
'''
max_score=collection.aggregate([{"$unwind":"$scores"}, {"$group":{
                               "_id":"$name",
                               "max_mark":{"$max":"$scores.score"}}
                               
                                }])
for i in max_score:
    print(i)
'''
'''      
sortavg=[]
Agg_sum=collection.aggregate([
    
{"$unwind":"$scores"}, {"$group":{
                               "_id":"$_id",
                               "Average":{"$avg":"$scores.score"}
                               }}, {"$sort":{"Average":-1}}
                               
                                 ]
                                   )
for i in Agg_sum:
    sortavg.append(i)
res=collection.bulk_write(sortavg)
myclient.close()
'''
'''
low_mark=collection.aggregate([{"$project":{"name":"$name","score":"$scores","Lowmark":{ "$lt": [ "$avg", 40 ]}}},
                                    {"$unwind":"$scores"}, {"$group":{
                                    "_id":"$name",
                                    "Average":{"$avg":"$scores.score"}}
                                                                                                                       }   

                               
                                 ]
                                   )
for i in low_mark:
    print(i)
    '''