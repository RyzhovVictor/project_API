import requests

#  Создание вызова API и созранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

#  Сохранение ответа API в переменной
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')


# Анализ первого репозитория
repo_dicts = repo_dicts[0]
print(f'\nKeys: {len(repo_dicts)}')
for key in sorted(repo_dicts.keys()):
    print(key)

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f"Name: {repo_dicts['name']}")
    print(f"Owner: {repo_dicts['owner']['login']}")
    print(f"Stars: {repo_dicts['stargazers_count']}")
    print(f"Repository: {repo_dicts['html_url']}")
    print(f"Created: {repo_dicts['created_at']}")
    print(f"Update: {repo_dicts['updated_at']}")
    print(f"Description: {repo_dicts['description']}")

# Обработка результатов
print(response_dict.keys())
