from abc import ABC, abstractmethod

class Bot:
    def __init__(self, name, version, copies, alive, filename):
        self.name = name
        self.version = version
        self.copies = copies
        self.alive = alive
        self.filename = filename
        self.bot_dict = {}
        
    def make_bot_dict(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(',')
            
            for header in headers:
                self.bot_dict[header] = []
            for line in lines[1:]:
                values = line.strip().split(',')
                for i, value in enumerate(values):
                    self.bot_dict[headers[i]].append(value)
        
        return self.bot_dict
    
    

filename = 'C:/Users/Emu\Documents/Masters-AI/bot_list.txt'

bot = Bot()