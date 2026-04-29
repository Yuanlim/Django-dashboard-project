from apps.accounts.domain.types.profile import CreateProfileInput


class TestServiceBase():
    
    # fail message constructor
    def does_not_exist_report(self, data: int|str):
        return f"{data} doesn't exist in country table and it should not be happened."
    
    def create_report(self, data: CreateProfileInput):
        
        returnStr = ""
        for key in data:
            returnStr += key + ": " + data[key] + "\n"
        return returnStr + "Create fail."