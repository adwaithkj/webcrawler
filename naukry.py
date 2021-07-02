import requests
from bs4 import BeautifulSoup

url = "https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="

headers = {
    "appid": "109",
    "systemid": "109"
}

f = requests.get(url, headers=headers)

data = f.json()

jobid = 1

for i in data['jobDetails']:
    print(i['title'], i['companyName'])
    soup = BeautifulSoup(i["jobDescription"])
    f = open(str(jobid)+".txt", "w")
    f.write(i['title'])
    f.write(i['companyName'])
    f.write("\n\n")
    f.write(soup.text)
    f.close()
    jobid += 1
