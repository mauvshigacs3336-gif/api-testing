import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"


response = requests.get(f"{BASE_URL}/1")

print("GET")
print("Status:", response.status_code)
print(response.json())


data = {
    "name": "Mauvshiga",
    "username": "mauvshiga_updated",
    "email": "mauvshiga@example.com",
    "id": "45"
}

response = requests.put(
    f"{BASE_URL}/1",
    json=data
)

print("\nPUT")
print("Status:", response.status_code)
print(response.json())


data = {
    "name": "Mauvshiga Updated"
}

response = requests.patch(
    f"{BASE_URL}/1",
    json=data
)

print("\nPATCH")
print("Status:", response.status_code)
print(response.json())



response = requests.get(f"{BASE_URL}/1")

print("\nGET AGAIN")
print("Status:", response.status_code)
print(response.json())


response = requests.delete(f"{BASE_URL}/1")

print("\nDELETE")
print("Status:", response.status_code)
print(response.text)