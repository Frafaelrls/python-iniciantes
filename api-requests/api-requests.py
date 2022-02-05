import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = response.json()  # .json transform in a list

for project in my_projects:
    print(f"Project name{project['name']} \nProject url {project['web_url']}"
          f"\n")
