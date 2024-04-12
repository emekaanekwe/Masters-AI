

class Bot:
    def __init__(self, id, name, active):
        self.id = id
        self.name = name
        self.actie = active
    
    def get_id(self):
        self.id = 1
        return self.id
    

bot_id = Bot
bot_id.get_id(1)