
import requests
from .config import *
from  .Exceptions import AcesstokenError,UnDefineConfigError
from . import Get_job_type
from typing import Union

def set_nick(uid:str,TDS_token:str) -> dict:
    """set nick tiktok sử dụng token của trao đổi sub"""
    try:
        params = {
            "fields":"instagram_run",
            "id":uid,
            "access_token":TDS_token
        }
        response = requests.get(api_url,params=params)
        response.raise_for_status()
        data = response.json()
        if AcesstokenError.is_error(data): raise AcesstokenError(TDS_token)
        return data

    except requests.HTTPError as e:
        print(f"[ERR] : Lỗi khi set id {uid} ! {e}")
    except AcesstokenError as e:
        print(e)
    


def get_job(mode:Get_job_type,TDS_token:str) -> Union[dict,list]:
    try:
        params = {
            "fields":mode,
            "access_token":TDS_token
        }
        response = requests.get(api_url,params=params)
        response.raise_for_status()
        data = response.json()
        if AcesstokenError.is_error(data): raise AcesstokenError(TDS_token)
        if UnDefineConfigError.is_error(data): raise UnDefineConfigError(TDS_token,"instagram")
        return data
    
    except requests.HTTPError as e:
        print(f"[ERR] : Lỗi khi lấy job, mode = {mode} , token = {TDS_token}")
    except AcesstokenError as e:
        print(e)
    except UnDefineConfigError as e:
        print(e)
    


    