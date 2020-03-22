import json
import requests

def top_commits(resp, org_name, most_committees):

    # Response schema
    top_committees = {'name':'', 'commit_count': 0}
    top_committees_list = []
    res_schema = {'repo_name':'', 'top_committees':[]}
    res_list = []
    #Github API endpoint to get contributors
    base_url = "https://api.github.com/repos/{}/{}/contributors?per_page={}"

    for item in resp['items']:

        response = requests.get(base_url.format(org_name, item['name'], str(most_committees)))
        if response.status_code == 200:
            contributers = json.loads(response.text)
            for contributer in contributers:
                # Iterating through each contributor per repo
                top_committees['name'] = contributer['login']
                top_committees['commit_count'] = contributer['contributions']
                top_committees_list.append(top_committees)
                top_committees = {}
            
        res_schema['repo_name'] = item['name']
        res_schema['top_committees'] = top_committees_list
        res_list.append(res_schema)
        res_schema = {}
        top_committees_list = []
    top_commits = {'repos':res_list}
    return top_commits

def process_request(payload):

    # Github API endpoint to perform repository search
    base_url = "https://api.github.com/search/repositories?q=org:{}&sort=forks&order=desc&per_page={}"
    
    org_name = payload['org'] # Org name
    n = payload['n'] # No. of popular repository
    m = payload['m'] # No. of top committees
    
    #Github API call
    response = requests.get(base_url.format(org_name, str(n)))

    if response.status_code == 200:
        return top_commits(json.loads(response.text), org_name, m)
    else:
        return None