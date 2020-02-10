EXPECTEDDATA = [
    ('https://api.openbrewerydb.org/breweries/1',
     {"id": 1, "name": "5 Rivers Brewing LLC", "brewery_type": "planning", "street": "", "city": "Spanish Fort",
      "state": "Alabama", "postal_code": "36527-3161", "country": "United States", "longitude": "-87.9152724",
      "latitude": "30.6749127", "phone": "2516897483", "website_url": "http://5riversbrewing.com",
      "updated_at": "2018-08-23T23:19:56.771Z", "tag_list": []}),
    ('https://api.openbrewerydb.org/breweries/2',
     {"id": 2, "name": "Avondale Brewing Co", "brewery_type": "micro", "street": "201 41st St S", "city": "Birmingham",
      "state": "Alabama", "postal_code": "35222-1932", "country": "United States", "longitude": "-86.774322",
      "latitude": "33.524521", "phone": "2057775456", "website_url": "http://www.avondalebrewing.com",
      "updated_at": "2018-08-23T23:19:57.825Z", "tag_list": []}),
    ('https://api.openbrewerydb.org/breweries/3',
     {"id": 3, "name": "Back Forty Beer Co", "brewery_type": "micro", "street": "200 N 6th St", "city": "Gadsden",
      "state": "Alabama", "postal_code": "35901-3361", "country": "United States", "longitude": "-86.005006",
      "latitude": "34.016888", "phone": "2564674912", "website_url": "http://www.backfortybeer.com",
      "updated_at": "2018-08-23T23:19:58.654Z", "tag_list": []}),
    ('https://api.openbrewerydb.org/breweries/4',
     {"id": 4, "name": "Band of Brothers Brewing Company", "brewery_type": "micro", "street": "1605 23rd Ave",
      "city": "Tuscaloosa", "state": "Alabama", "postal_code": "35401-4653", "country": "United States",
      "longitude": "-87.5621551272424", "latitude": "33.1984907123707", "phone": "2052665137", "website_url": None,
      "updated_at": "2018-08-23T23:19:59.462Z", "tag_list": []})
]

EXPECTEDID = [
    ('https://api.openbrewerydb.org/breweries/autocomplete?query=dog',
     ['530', '542', '1221', '2268', '3025', '3068', '3136', '4121', '4263', '4555', '5359', '5925', '7152', '7424',
      '7704']),
    ('https://api.openbrewerydb.org/breweries/autocomplete?query=milk',
     ['3163', '7891', '5508', '7893', '7913', '1703', '7806', '7932', '7892', '816', '7552', '4825', '3751', '4329',
      '4537']),
    ('https://api.openbrewerydb.org/breweries/autocomplete?query=blablabla',
     [])
]

TESTDATABREEDS = [
    (['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'])
]

TESTKEYS = ['id', 'name', 'brewery_type', 'street', 'city', 'state', 'postal_code',
      'country', 'longitude', 'latitude', 'phone', 'website_url', 'updated_at', 'tag_list']