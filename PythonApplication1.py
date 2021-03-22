from feedparser import parse

from pprint import pprint


def get_fuel(product_id,suburb,when):
    url = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product='+str(product_id)+'&Suburb='+str(suburb)+'&Day='+str(when)+''
    data = parse(url)
    fuel_list = [
        {
            'date': details['date'],
            'address': details['address'],
            'location': details['location'],
            'brand': details['brand'],
            'price': float(details['price']),
            
        }
    for details in data['entries']
    ]
    pprint(fuel_list)
    return fuel_list

# define variables for product_id
Unleaded_Petrol = 1
Premium_Unleaded = 2

# Calling function
felicia_today = get_fuel(Premium_Unleaded,'south%20perth','today')
felicia_tomorrow = get_fuel(Premium_Unleaded,'south%20perth','tomorrow')
felicia_combined = felicia_today + felicia_tomorrow

def by_price(item):
    return item['price']
sorted_felicia_combined = sorted(felicia_combined, key = by_price)

Fuel_html_list = ''
for word in sorted_felicia_combined:
    Fuel_html_list = Fuel_html_list + '<td>' + word['date'] + '</td>'
    Fuel_html_list = Fuel_html_list + '<td>' + word['address'] + '</td>'
    Fuel_html_list = Fuel_html_list + '<td>' + word['location'] + '</td>'
    Fuel_html_list = Fuel_html_list + '<td>' + word['brand'] + '</td>'
    Fuel_html_list = Fuel_html_list + '<td>' + str(word['price']) + '</td>'
    Fuel_html_list = Fuel_html_list + '</tr>'


Fuel_html = f'''
<html>
<head>
<style>

</style>
</head>
<body>

<h2>Fuel Table</h2>


<table>
    <tr>
        <th>Date</th>
        <th>Address</th>
        <th>Location</th>
        <th>Brand</th>
        <th>Price</th>
    </tr>

<tr>
    {Fuel_html_list}
</tr>

</table>

</body>
</html>

'''
f = open('render.html','w')
f.write(Fuel_html)
f.close()
