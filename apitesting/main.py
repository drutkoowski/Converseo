import requests

headers = {
    "Content-Type": "application/json"
}


def get_token():
    endpoint = 'http://127.0.0.1:8000/api/token/'
    req = requests.post(endpoint, json={"username": "test", "password": "test"}, headers=headers)
    print(req.text)


def test():
    headers_test = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyNzUxNjYyLCJpYXQiOjE2NzI3NTEzNjIsImp0aSI6IjA3NTA4NWNlZDgwODQ5MmI4M2FlYzkxNTFhMDRjYjUzIiwidXNlcl9pZCI6MX0.6HqbUXnT02StIys55IkG05O_VxN5C_GWPKVLCfi5xhw"
    }
    endpoint = 'http://127.0.0.1:8000/api/user/'
    req = requests.get(endpoint, headers=headers_test)
    print(req.text)


# test()
def signup_user():
    headers_test = {
        "Content-Type": "application/json",
    }
    endpoint = 'http://127.0.0.1:8000/api/user/create'
    req = requests.post(endpoint, headers=headers_test,
                        json={"username": "test2", "password": "test2", "email": 'test2@o2.pl', 'gender': 'male', 'birth_date': '2023-01-03'})
    print('output', req.text)


# signup_user()

if __name__ == '__main__':
    pass
