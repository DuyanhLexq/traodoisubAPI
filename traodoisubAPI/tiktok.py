import requests
from .config import *
from .Exceptions import AcesstokenError, UnDefineConfigError
from . import Get_job_type
from typing import Union

def set_nick(uid, TDS_token) -> dict:
    """
    Đặt nick TikTok sử dụng token của trao đổi sub.

    Args:
        uid (str): ID của người dùng TikTok.
        TDS_token (str): Token của trao đổi sub (Access token).

    Returns:
        dict: Dữ liệu phản hồi từ server sau khi đặt nick.

    Raises:
        AcesstokenError: Nếu token không hợp lệ hoặc hết hạn.
        requests.HTTPError: Nếu xảy ra lỗi HTTP trong quá trình yêu cầu.
    """
    try:
        params = {
            "fields": "tiktok_run",
            "id": uid,
            "access_token": TDS_token
        }
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        data = response.json()
        if AcesstokenError.is_error(data):
            raise AcesstokenError(TDS_token)
        return data

    except requests.HTTPError as e:
        print(f"[ERR] : Lỗi khi đặt id {uid}! {e}")
    except AcesstokenError as e:
        print(e)
    except Exception as e:
        print(f"[ERR] : Lỗi không xác định khi đặt nick! {e}")


def get_job(mode: Get_job_type, TDS_token: str) -> Union[dict, list]:
    """
    Lấy danh sách công việc dựa trên chế độ và token cung cấp.

    Args:
        mode (Get_job_type): Chế độ công việc muốn lấy (ví dụ: "tiktok", "facebook").
        TDS_token (str): Token của trao đổi sub (Access token).

    Returns:
        Union[dict, list]: Dữ liệu phản hồi từ server về công việc.

    Raises:
        AcesstokenError: Nếu token không hợp lệ hoặc hết hạn.
        UnDefineConfigError: Nếu chế độ không xác định hoặc cấu hình sai.
        requests.HTTPError: Nếu xảy ra lỗi HTTP trong quá trình yêu cầu.
    """
    try:
        params = {
            "fields": mode,
            "access_token": TDS_token
        }
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Kiểm tra lỗi HTTP
        data = response.json()
        if AcesstokenError.is_error(data):
            raise AcesstokenError(TDS_token)
        if UnDefineConfigError.is_error(data):
            raise UnDefineConfigError(TDS_token, "tiktok")
        return data

    except requests.HTTPError as e:
        print(f"[ERR] : Lỗi khi lấy công việc, mode = {mode}, token = {TDS_token}! {e}")
    except AcesstokenError as e:
        print(e)
    except UnDefineConfigError as e:
        print(e)
    except Exception as e:
        print(f"[ERR] : Lỗi không xác định khi lấy công việc! {e}")
