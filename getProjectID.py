
token1 = "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"
token2 = "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"


import requests
import pandas as pd
import json
headers = {"Authorization": "Bearer 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"}


def run_query(query): 
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

              
query = """
{
    user(login: "Shrish236") {
      projectsV2(first: 20) {
        nodes {
          id
          title
        }
      }
    }
}
"""

result = run_query(query) # Execute the query
print(result.json())
# data = pd.DataFrame.from_dict(result)
# output = []
# for fields in result['data']['node']['items']['nodes']:
#   d = {}
#   for data in fields['fieldValues']['nodes']:
#     if len(data)!=0:
#       d[data['field']['name']] = data['text']
#   output.append(d)
# print(pd.DataFrame(output))