import feedparser 

from urllib.parse import urlencode

from itertools import product

from pprint import pprint


def get_fuel(product_id,suburb,when):
    params = {
    'Product': product_id,
    'Suburb': suburb,
    'When': when,
  }
    data = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?' + urlencode(params))
    pprint('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?' + urlencode(params))
    return [
        {
            'date': details['date'],
            'address': details['address'],
            'location': details['location'],
            'brand': details['brand'],
            'price': float(details['price']),
            
        }
        for details in data['entries']
   ]
        
fuel_list = get_fuel(2,'south perth','Today')
pprint(fuel_list)
    
tr_list = [
                '<tr><td>{date}</td><td>{address}</td><td>{location}</td><td>{brand}</td><td>{price}</td></tr>'.format(**d)
                for d in  fuel_list
]

thead = '''
    <tr>
        <th>Date</th>
        <th>Address</th>
        <th>Location</th>
        <th>Brand</th>
        <th>Price</th>
    </tr>
'''


html = '<h2>Fuel Table</h2>' + '<table>' + thead + ''.join(tr_list) + '</table>'


with open('table.html', 'w') as f:
    f.write('<style>table, td{border: 1px solid black}</style>' + html)