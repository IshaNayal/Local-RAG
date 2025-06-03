

from dotenv import load_dotenv
import os
import requests
import json
import pandas as pd
import glob

pd.options.mode.chained_assignment = None

load_dotenv()


headers = {
    'Authorization': 'Bearer '+os.getenv('BRIGHTDATA_API_KEY'),
    'Content-Type': 'application/json',
}

headers_status = {
    'Authorization': 'Bearer '+os.getenv('BRIGHTDATA_API_KEY'),
}

keywords = pd.read_excel("keywords.xlsx")


file_exists = os.path.isfile(os.getenv("SNAPSHOT_STORAGE_FILE"))


if not file_exists:

    params = {
        "dataset_id": "gd_lr9978962kkjr3nx49",
        "include_errors": "true",
        "type": "discover_new",
        "discover_by": "keyword",
    }

    json_data = []

    for ind in keywords.index:

        json_data.append({"keyword":keywords.loc[ind, "Keyword"],"pages_load":str(keywords.loc[ind, "Pages"])})

    response = requests.post('https://api.brightdata.com/datasets/v3/trigger', params=params, headers=headers, json=json_data)

    result = json.loads(response.content)

    with open(os.getenv("SNAPSHOT_STORAGE_FILE"), "a") as f:
        f.write(str(result["snapshot_id"]))


else:



    files = glob.glob(os.getenv("DATASET_STORAGE_FOLDER")+"*")	

    for f in files:
        os.remove(f)



    f = open(os.getenv("SNAPSHOT_STORAGE_FILE"),"r")
    snapshot_id = f.read()

    response = requests.get('https://api.brightdata.com/datasets/v3/progress/'+snapshot_id, headers=headers_status)
    
    status = response.json()['status']

    print("status")
    print(status)


    snapshot_ready = False

    if(status == "ready"):
        print("Snapshot is ready")
        snapshot_ready = True
    else:
        print("Snapshot is NOT READY YET")


    print("")



    if snapshot_ready:
        print("== > All articles are ready - start writing data to datasets directory")


        response = requests.get('https://api.brightdata.com/datasets/v3/snapshot/'+snapshot_id, headers=headers)

        if not os.path.exists(os.getenv("DATASET_STORAGE_FOLDER")):
             os.makedirs(os.getenv("DATASET_STORAGE_FOLDER"))

        with open(os.getenv("DATASET_STORAGE_FOLDER")+"data.txt", "wb") as f:
            f.write(response.content)

    else:
         print("== > Not all articles are scraped yet - try again in a few minutes")
