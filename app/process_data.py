import json
def get_data():
    import http.client
    con = http.client.HTTPSConnection("api.coindesk.com")
    con.request("GET", "/v1/bpi/currentprice.json")
    res = con.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))

def process():
    data = get_data()
    #(a,b,*c) = data
    #rep = (a,b,*c)
    #return (rep)
    return (data)