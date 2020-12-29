# ListenAI - Technation Hackathon Project

This project is composed of a series of Python scripts which collect tweets relating to COVID-19's impact on businesses in Canada. This hackathon project was built with `Python 3.6.9`, and uses the [Microsoft Azure Cognitive Services API](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitive-services?view=azure-python) and [Twitter v2 API's recent search functionality](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent).


## Project Background
See [the project website](https://chantellechan1.github.io/technation_hackathon/) for details on the hackathon project, and [a 5 minute background overview video.](https://chantellechan1.github.io/technation_hackathon/video_presentation.html)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all project dependencies.

```bash
pip install requirements.txt
```

## Usage
Prior to running either script or proceeding any further, please create a file called `secrets.py` and fill in all credentials and keys (template provided below).  

If using a virtual environment (recommended) first create and activate it by running:
```bash
python3 -m venv <virtual environment name>
source <virtual environment name>/bin/activate
```

To begin tweet collection, run the following: `python main.py`  
* This script will store tweets, named entities for the tweets, and tweet hashtags in a Postgres database. For our purposes, we used Azure Database for PostgreSQL.   
  
To run sentiment analysis, run: `python analytics.py`  
* Sentiment analysis will give the average sentiment and confidence levels for each tweet, which will be output as an aggregate (in our case, it will be a Canadian national average).

### Secrets Template
```python
# Twitter Labs Keys
API_KEY = ""
API_KEY_SECRET = ""
BEARER_TOKEN = ""

# PostgreSQL DB Details
DB_SECRETS = {
    "host": "",
    "dbname": "",
    "user": "",
    "password": "",
    "sslmode": ""
}

AZURE_SERCRETS = {
    "endpoint": "",
    "key": ""
}
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
