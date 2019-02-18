from app import app
import urllib.request,json
from .models import source
from .models import news
Source = source.Source
News = news.News

# getting api key
api_key = app.config['NEWS_API_KEY']
# getting the news base url

base_url = app.config['SOURCE_API_BASE_URL']

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        source_results = get_source_response
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_result(source_results_list)
    return source_results
def process_result(source_list):
    '''
    Function that processes the newz result and transform them to a list of objects
    
    Args:
       newz_list: A list of dictionaries that contain newz details
    Returns:
       newz_results:A list of objects
    '''
    source_results =[]
    for source_item in source_list:
       
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        if source:
            source_object = Source(id,name,description)
            source_results.append(source_object)
    return source_results
