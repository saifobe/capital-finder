from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
 
class handler(BaseHTTPRequestHandler):

    # method to handle HTTP GET Request 
    def do_GET(self):

        s = self.path
        url_components = parse.urlsplit(s)
        query_strings_list = parse.parse_qsl(url_components.query)
        dic = dict(query_strings_list)
        country = dic.get("country")
        capital = dic.get("capital")
        result = ""

        if country:
            url = f"https://restcountries.com/v3.1/name/{country}"
            
            try:
                res = requests.get(url)
                data = res.json()
                capital_res = data[0]["capital"][0]
                result = f"The capital of {country} is {capital_res}"
            except:
                result = "Country not found"
            
        if capital:
            url = f"https://restcountries.com/v3.1/capital/{capital}"
            
            try:
                res = requests.get(url)
                data = res.json()
                country_res = data[0]["name"]["common"]
                result = f"{capital}is the capital of {country}."
            except:
                result = "Capital not found"
       
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(result.encode('utf-8'))
        return