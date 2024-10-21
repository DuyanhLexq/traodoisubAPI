
class AcesstokenError(Exception):
    def __init__(self,token:str):
        self.msg = f"AcesstokenError: Token không hợp lệ !, token của bạn '{token}'"
    
    @staticmethod
    def is_error(data:dict)->bool:
        if not isinstance(data,dict):return False

        if data.get("error",False):
            return data["error"] == "Access token không hợp lệ! xin thử lại"
        
        return False
    
    def __str__(self):
        return self.msg

class UnDefineConfigError(Exception):
    def __init__(self,token:str,type_:str):
        self.msg = f"UnDefineConfigError: Bạn chưa cấu hình nick cho {type_} , token = '{token}'"
    @staticmethod
    def is_error(data:dict) -> bool:
        if not isinstance(data,dict):return False
        if data.get("error",False):
            return data["error"] == "Vui lòng cấu hình nick rồi quay lại sau nhé!"
        return False

        
