import json
import requests
import re


URL = 'https://www.googleapis.com/fusiontables/v1/query?key=AIzaSyAYkamn8YeEjHRpv892i26Mfv6i09eEdPM&sql=SELECT%20beach_id,%20name,%20county,%20mid_lat,%20mid_lon,%20samples,%20pct_samples_bav,%20loc_valid%20FROM%201uK8UlIIOG59txfGjH2WxrDIr_KIxR9lGixkqTple%20WHERE%20state%20=%20%27FL%27&typed=true&callback=jQuery17105043562010396272_1404232573870&_=1404232574998'

def getData():
    """Use requests to snag data from Google
    Fusion Tables and transorms the response
    from JSONP to JSON."""
    ## First, use requests (or urllib) to snag the data
    data = requests.get(URL).content
    ## To transform from JSONP to JSON, we need to strip
    ## the function call from the front. The following regex
    ## grabs everything before the first mustache bracket.
    jsonp_regex = r"^([^\{]+)"
    ## Using our regex pattern above, we swap out the function
    ## call with an empty string.
    cleaned_data = re.sub(jsonp_regex, "", data)
    ## Now we just need to remove the end of the function call
    cleaned_data = cleaned_data[:-2]
    ## With out now-clean data, we then load into the json
    ## module.
    data = json.loads(cleaned_data)
    return data


def main():
    """Take the json response and pull out just the relevant
    information."""
    json_data = getData()
    for row in json_data["rows"]:
        ## transform all to strings so you can join
        ## them below
        r = [str(d) for d in row]
        ## I'm just printing the response here, but this
        ## is where you'll likely save the data to a text
        ## file.
        print ",".join(r)

if __name__ == "__main__":
    main()
    
'''annotations/code by Patrick Sweet (mostly)
and to get it to csv, see below'''

import csv
import json
import requests
 
url = 'https://www.googleapis.com/fusiontables/v1/query?key=AIzaSyAYkamn8YeEjHRpv892i26Mfv6i09eEdPM&sql=SELECT%20beach_id,%20name,%20county,%20mid_lat,%20mid_lon,%20samples,%20pct_samples_bav,%20loc_valid%20FROM%201uK8UlIIOG59txfGjH2WxrDIr_KIxR9lGixkqTple%20WHERE%20state%20=%20%27FL%27&typed=true&callback=jQuery17105043562010396272_1404232573870&_=1404232574998'
jtext = requests.get(url).text.split('jQuery17105043562010396272_1404232573870(')[1].strip(');')
beaches_dict = json.loads(jtext)
 
with open('beach_data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(beaches_dict['columns'])
    for each in beaches_dict['rows']:
        writer.writerow(each)

