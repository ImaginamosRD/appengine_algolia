from algoliasearch import algoliasearch
import json

def start_indexing():
    client = algoliasearch.Client("3A3S6V9V9E", "2ad807b0b155e97087794ca16841c04e")
    index = client.init_index('algolia-2')

    batch = json.load(open('airports.json'))
    index.add_objects(batch)

    index.set_settings({'ranking': ['typo', 'geo', 'words', 'attribute', 'proximity', 'exact', 'custom'],
                            "searchableAttributes": ['country', 'city', 'name', 'iata_code'],
                            "customRanking": ['desc(links_count)'],
                            'attributesForFaceting': ['country', 'city']})



