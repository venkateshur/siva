import requests
import pandas as pd
import xmltodict


def get_service(api, response_type="json"):
    response = requests.get(api)
    if response_type == "json":
        j = response.json()
        df = pd.DataFrame([[d['v'] for d in x['c']] for x in j['rows']],
                          columns=[d['label'] for d in j['cols']])
    else:
        response = requests.get(api)
        dict_data = xmltodict.parse(response.content)
        df = pd.DataFrame.from_dict(dict_data)

    return df


def post_service(api, df, pay_load_type="json"):
    headers_json = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    headers_xml = {'Content-type': 'application/xml', 'Accept': 'text/plain'}
    for i in df.index:
        if pay_load_type == "json":
            pay_load = df.loc[i].to_json("row{}.json".format(i))
            requests.post(api, data=pay_load, headers=headers_json)
        else:
            xml = ['<item>']
            for field in df.index:
                xml.append('  <field name="{0}">{1}</field>'.format(field, df[field]))
            xml.append('</item>')
            pay_load = '\n'.join(xml)
            requests.post(api, data=pay_load, headers=headers_xml)




