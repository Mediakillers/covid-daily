import csv
import sys
from datetime import datetime
from shutil import copyfile

sys.path.append('/home/a4iv1kv14b88/covid_map/modules')
from modules import requests

NOW = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

response = requests.get('https://api.findcovidtesting.com/api/v1/location')
if not response.status_code == 200:
    exit(1)
fields = max([list(i.keys()) for i in response.json()])
with open('/home/a4iv1kv14b88/covid_map/outputs/venues_{}.csv'.format(NOW),
          'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(response.json())
copyfile("/home/a4iv1kv14b88/covid_map/outputs/venues_{}.csv".format(NOW),
             "/home/a4iv1kv14b88/genasys.com/public_html/wp-content/uploads/venues.csv")
