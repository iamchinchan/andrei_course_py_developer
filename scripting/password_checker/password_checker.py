import hashlib
import requests


def password_api(hashed_pass):
    url = "https://api.pwnedpasswords.com/range/" + hashed_pass
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the api and try again!"
        )
    return res


def pass_to_hash(password):
    hashed_pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return hashed_pass


print(pass_to_hash("password123"))
