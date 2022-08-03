import pymongo

Connection_String = "mongodb://ian-cosmos-two:QcXz5YKcNW0ulkrI5ZTnDcl1p0cCuooYCq3wHr5EbsxsHcoUfbmBL1owDrrQtmSwNQB2z9wCP1SwwdkU3pP7Ng==@ian-cosmos-two.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@ian-cosmos-two@"
client = pymongo.MongoClient(Connection_String)
db_name = "ian_database"
collection_name = "ian_collection"

items = client[db_name][collection_name]

class Item:
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status

class MongoDB_Items:
    def fetch_items(self):
        tasks = []
        for item in items.find():
            tasks.append(Item(id=item["_id"],title=item["title"], status=item["status"]))
        return tasks

    def add_item(self,title):
        item = {
            "title": title,
            "status": "todo"
        }

        items.insert_one(item)


ian_tasks=MongoDB_Items()
# ian_tasks.add_item("Hello")

all = ian_tasks.fetch_items()

print(all)
for x in all:
    print(x.title)

