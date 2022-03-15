from pydoc import describe


def describe_city(city, country='iceland'):
    print(f"{city.title()} is in {country.title()}.")

describe_city('rekjavic')
describe_city('london',country='the uk')
describe_city('paris',country='france')