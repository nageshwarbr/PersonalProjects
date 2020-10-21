import json
import requests
response=requests.get("https://formulae.brew.sh/api/formula.json")
packages_json=json.loads(response.text)
for packages in packages_json:
    package_name=packages['name']
    package_desc=packages['desc']
    package_url=requests.get(f'https://formulae.brew.sh/api/formula/{package_name}.json')
    packages_str=json.loads(package_url.text)
    install_30=packages_str['analytics']['install_on_request']['30d'][package_name]
    install_90=packages_str['analytics']['install_on_request']['90d'][package_name]
    install_365=packages_str['analytics']['install_on_request']['365d'][package_name]
    print(package_name,package_desc,install_30,install_90,install_365)

