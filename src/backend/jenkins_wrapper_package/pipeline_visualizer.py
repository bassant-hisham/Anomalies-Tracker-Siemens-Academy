import requests
import json

jenkins_url = 'http://localhost:9090'
pipeline_name = 'Ethernet-Task1-Job1'
username = 'AhmedSh'
api_token = '114b7687f31196a9655f472320e628af6e'

url = f'{jenkins_url}/blue/rest/organizations/jenkins/pipelines/{pipeline_name}/runs/404/'
response = requests.get(url, auth=('AhmedSh', '114b7687f31196a9655f472320e628af6e'))


if response.status_code == 200:
    run_details = response.json()
    nodes_url = jenkins_url + run_details['_links']['nodes']['href']
    nodes_response = requests.get(nodes_url, auth=(username, api_token))
    
    if nodes_response.status_code == 200:
        stages = nodes_response.json()
        results_first_char = []  # Initialize an empty list to store the first characters
        for stage in stages:
            first_char = stage['result'][0] if stage['result'] else 'N/A'  # Get first char or use 'N/A'
            results_first_char.append(first_char)
            print(f"Stage: {stage['displayName']}, Result: {first_char}, Status: {stage['state']}, Duration: {stage['durationInMillis']} ms")
    else:
        print(f"Error fetching stages: {nodes_response.status_code}")
else:
    print(f"Error: {response.status_code}")


result = ""
for i in results_first_char:
    if i == 'S':
        result += f'\033[92m{i}\033[0m|'
    else:
        result += f'\033[91m{i}\033[0m|'  

print(result)


