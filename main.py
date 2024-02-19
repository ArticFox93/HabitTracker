import requests
from datetime import datetime

USERNAME = "type your username here"  # chance to someone have same name, try type unique username
TOKEN = "type your token here"  # write a bunch of random letters (example - roweihdsfpfpod), min. 8-128 lettters
GRAPH_ID = "type your name of graph"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "token": TOKEN,
    "id": GRAPH_ID,
    "name": "Programming time Graph",  # name of your graph on the page
    "unit": "min",  # you can change it to "hour" or something like that
    "type": "int",  # change to "float" if you want to use decimal numbers
    "color": "shibafu"  # read thought the documentation https://docs.pixe.la/entry/post-graph to change color
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response2 = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today_date = datetime.now()
# today_date = datetime(year=2024, month=2, day=18) - yesterday

choice = input("What do you want to do? (add, update, delete): ")
if choice == "add":
    pixel_params = {
        "date": today_date.strftime("%Y%m%d"),
        "quantity": input("How many minutes did you programmed today?: ")
    }
    try:
        response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
    except:
        response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

elif choice == "update":
    update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date.strftime("%Y%m%d")}"

    update_pixel_params = {
        "quantity": input("Update to? (min): "),
    }
    try:
        response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
    except:
        response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)

elif choice == "delete":
    delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date.strftime("%Y%m%d")}"
    try:
        response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    except:
        response = requests.delete(url=delete_pixel_endpoint, headers=headers)
else:
    print("bad request")
print(f"Your link to your graph: {pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}.html")