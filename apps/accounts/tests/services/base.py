class TestServiceBase():
    
    # fail message constructor
    def does_not_exist_report(self, data: int|str):
        return f"{data} doesn't exist in country table and it should not be happened."