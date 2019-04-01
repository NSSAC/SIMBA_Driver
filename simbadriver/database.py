import cx_Oracle

class Database:

    def __init__(self, SIMBA):
        self.SIMBA = SIMBA
        
        self.schema = {
            "type" : "object",
            "properties" : {
                "host" : {"type" : "string"},
                "port" : {"type" : "number"},
                "database" : {"type" : "string"},
                "user" : {"type" : "string"},
                "password" : {"type" : "string"},
                "oracle_service" : {"type" : "string"},
                },
            "required" : [
                "host",
                "port",
                "database",
                "user",
                "password",
                "oracle_service"
                ]
            }
        
        self.data = self.SIMBA.getConfiguration().loadJsonFile("database.json", self.schema)
        
        try:
            cx_Oracle.connect(host = self.data["host"],
                             port = self.data["port"],
                             dbname = self.data["database"],
                             user = self.data["user"],
                             password = self.data["password"])
            
        except:
            pass
        
        return
            
        
    def getConnectionInfo(self):
        return self.data
    
    def getHost(self):
        return self.data["host"]
        
    def getPort(self):
        return self.data["port"]
        
    def getDatabase(self):
        return self.data["database"]
        
    def getUser(self):
        return self.data["user"]
        
    def getPassword(self):
        return self.data["password"]
