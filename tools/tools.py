
import requests

#### OTHER TOOLS AVAILABLE FOR THE CALLER ####

def wiki_search(keyword:str)->str:
    """
    This tool simply requests a wikipedia page with the description of the search.
    If the page requested is not available, an error will be thrown.

    Args:
        keyword (str): The keyword to search on wikipedia (1 or 2 words). 

    Returns:
        str: A descriptive text of the searched keyword.
    """
    
    url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="+keyword
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        json_data = response.json()  # Extract JSON content
        page = next(iter(json_data["query"]["pages"].values()))
        return page["extract"]
   
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
   
    except Exception as err:
        print(f"Other error occurred: {err}")