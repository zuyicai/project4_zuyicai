from bs4 import BeautifulSoup # need beautifulsoup for scraping
import requests, json, csv # need these to access data on the internet and deal with structured data in my cache
from advanced_expiry_caching import Cache # use tool from the other file for caching

# FILENAME = "data.json" # saved in variable with convention of all-caps constant
# park = Cache(FILENAME) # create a cache -- stored in a file of this name
#
#
# url = "https://www.nps.gov/index.html"
#
# data = park.get(url)
#
# if not data:
#     data = requests.get(url).text
#
#
# soup = BeautifulSoup(data,features = "html.parser")
#
# # al = soup.find(href="/state/al/index.htm")
# # print(al)
# #
# # states = soup.find_all('a')
# # for state in states:
# #     print(state.get('href'))
# #
# s = soup.find_all('ul','dropdown-menu SearchBar-keywordSearch','li')
# for state in s:
#     states = state.get_text()
#     print(states,"\n")
# # print(s)



####cpw's answer
states_name= ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi',
          'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn',
          'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh',
          'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

for i in range(len(states_name)):
    url = "https://www.nps.gov/state/%s/index.htm" % states_name[i]
    FILENAME = "%s_data.json" %states_name[i]# saved in variable with convention of all-caps constant
    program_cache = Cache(FILENAME) # create a cache -- stored in a file of this name
    data = program_cache.get(url)

    if not data:
        data = requests.get(url).text # get the text attribute from the Response that requests.get returns -- and save it in a variable. This should be a bunch of html and stuff
        program_cache.set(url, data, expire_in_days=1) # just 1 day here because news site / for an example in class


# count =  0

with open('parks.csv','w') as f:
    for i in range(len(states_name)):
        with open('%s_data.json'%states_name[i]) as json_f:
            nation = json.load(json_f)
            soup = nation["HTTPS://WWW.NPS.GOV/STATE/%s/INDEX.HTM"%states_name[i].upper()]['values']
            soup = BeautifulSoup(soup, features="html.parser")
            dat = soup.select("div[class='col-md-9 col-sm-9 col-xs-12 table-cell list_left']")
            ty=[]
            na=[]
            lo=[]
            de=[]
            states=[]
            for j in range(len(dat)):
                certain_state=[]
                type = dat[j].find('h2')
                ty.append(type.get_text())
                name = dat[j].find('h3')
                na.append(name.get_text())
                location = dat[j].find('h4')
                lo.append(location.get_text())
                description = dat[j].find('p')
                de.append(description.get_text())
                for k in range(len(states_name)):
                    if states_name[k].upper() in lo[j]:
                        certain_state.append(states_name[k].upper())
                states.append(certain_state)
                states[j]=",".join(states[j])



            for j in range(len(dat)):
                if ty[j] == "":
                    ty[j] = "No information"
                if na[j] == "":
                    na[j] = "No information"
                if lo[j] == "":
                    lo[j] = "No information"
                    states[j]=states_name[i].upper()
                if de[j] == "":
                    de[j] = "No information"
                writecsv = csv.writer(f)
                writecsv.writerow([ty[j], na[j], lo[j], de[j],states[j]])
            
