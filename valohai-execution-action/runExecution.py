import requests
import json
import os

# Authenticate yourself with the token
auth_token = 'udhv7v8Y5wEIj8wLvLWxeNLgQALANIsExOqPa0sR'
headers = {'Authorization': 'Token %s' % auth_token}
project_id = '0171c4a6-4e6c-21e6-0611-4c591adfa8a0'

# Fetch all new changes from the repository
# Define the branches that Valohai should have access to on Project->Settings->Repository
# You can use a '*' wildcard in the fetch reference
fetchResponse = requests.post(('https://app.valohai.com/api/v0/projects/{0}/fetch/').format(project_id), data={'id': project_id}, headers=headers)
fetchResponse.raise_for_status()


# Define the payload
# GITHUB_SHA contains the commit hash that Valohai uses
new_exec_payload = {
  "project": "0171c4a6-4e6c-21e6-0611-4c591adfa8a0",
  "commit": os.getenv('GITHUB_SHA'),
  "step": "Execute python train.py",
}

# Send a POST request to create a new execution
# You can get a sample request from app.valohai.com
# When creating a new execution select "Show as API call" at the bottom of the page
createExecutionResponse = requests.post('https://app.valohai.com/api/v0/executions/', data=new_exec_payload, headers=headers)
createExecutionResponse.raise_for_status()

# Print the response you've received back
print('# API Response:\n')
print(json.dumps(createExecutionResponse.json(), indent=4))