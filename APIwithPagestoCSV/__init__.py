def getdata(url,token):
    import pandas as pd
    import requests
    data = []
    results = True
    page = 1
    while results:
        get_data = requests.get(url + f"?page={page}",
                                    headers={'Authorization':f'Token {token}'}).json()
        results = get_data.get("results", [])
        data.extend(results)
        page += 1
    data_export = pd.DataFrame(data)
    data_export.to_csv("data_export.csv")