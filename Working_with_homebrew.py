import requests
import json
import time

r = requests.get('https://formulae.brew.sh/api/formula.json')

packages_json = r.json()

# package_name_list = [x['name'] for x in packages_json]

# packages_str = json.dumps(packages_json[0], indent=2)
# print(packages_str)

# for pckg_name in package_name_list:
#     print(pckg_name)

results = []

t1 = time.perf_counter()

for package in packages_json:
    package_name = package['name']
    package_desc = package['desc']

    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

    r2 = requests.get(package_url)
    package_json = r2.json()

    install_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    install_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    install_365 = package_json['analytics']['install_on_request']['365d'][package_name]

    data = {
        'name': package_name,
        'description': package_desc,
        'analytics': {
            '30d': install_30,
            '90d': install_90,
            '365': install_365,
        }
    }

    results.append(data)

    time.sleep(r.elapsed.total_seconds())

    print(f"Got {package_name} in {r.elapsed.total_seconds()} seconds")

t2 = time.perf_counter

print(f"Finished in {t2 - t1} seconds")

with open('package_info.json', 'w') as f:
    json.dump(results, f, indent=2)
