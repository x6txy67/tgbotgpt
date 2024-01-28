class UserInteractionHandler:
    def __init__(self, users_collection, bot):
        self.users_collection = users_collection
        self.bot = bot

    def add_user(self, user):

        try:
            self.users_collection.insert_one(user)
            return True
        except:
            return False
        
    def find_user(self, user):
        return self.users_collection.find_one(user)

    def get_all_users(self):
        return [user["_id"] for user in self.users_collection.find({}, {"_id": 1})]
