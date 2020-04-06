#!/usr/bin/env python3
import csv
from pprint import pprint

import requests


def generate_csv(datarows):
    """Helper to generate CSV from JSON"""
    with open('output.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Active',
                                                     'Admin2',
                                                     'Combined_Key',
                                                     'Confirmed',
                                                     'Country_Region',
                                                     'Deaths',
                                                     'FIPS',
                                                     'Incident_Rate',
                                                     'Last_Update',
                                                     'Lat',
                                                     'Long_',
                                                     'OBJECTID',
                                                     'People_Tested',
                                                     'Province_State',
                                                     'Recovered'])
        writer.writeheader()
        writer.writerows(datarows)


def get_data():
    """Helper for getting COVID cases map data"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.163 Safari/537.36',
        'origin': 'https://www.arcgis.com', 'referer': 'https://www.arcgis.com/apps/opsdashboard/index.html'}

    a = requests.get('https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Nc2JKvYFoAEOFCG5JSI6/'
                     'FeatureServer/1/query?f=json&where=1%3D1&returnGeometry=true&'
                     'spatialRel=esriSpatialRelIntersects&maxAllowableOffset=39135&'
                     'geometryType=esriGeometryEnvelope&inSR=102100&outFields=*&outSR=102100&resultType=tile',
                     headers=headers)

    return a.status_code, a.json()


if __name__ == '__main__':
    data = get_data()
    if data[0] == 200:
        countries = [i['attributes'] for i in data[1]['features']]
        generate_csv(countries)
        pprint(countries)
    else:
        print(data[1])
