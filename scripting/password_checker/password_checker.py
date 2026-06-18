import hashlib
import requests


def password_api(hashed_pass):
    url = "https://api.pwnedpasswords.com/range/" + hashed_pass
    res = requests.get(url)
    # print(f"res status code is  :{res.status_code}")
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the api and try again!"
        )
    return res


def pass_to_hash(password):
    hashed_pass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return hashed_pass[:5], hashed_pass[5:]


def check_if_pawned(password):

    first_hash, tail_hash = pass_to_hash(password)
    response = password_api(first_hash)
    for hash, val in (hash.split(":") for hash in response.text.splitlines()):
        if tail_hash == hash:
            return val
    return 0


if __name__ == "__main__":
    print(f"Password has been pawned: {check_if_pawned("fakepassword123")} many times")
