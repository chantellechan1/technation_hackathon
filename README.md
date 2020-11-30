# ListenAI - Technation Hackathon Project

This project is composed of a series of Python scripts which collect tweets relating to COVID-19's impact on businesses in Canada. This hackathon project was built with `Python 3.6.9`, and uses the [Microsoft Azure Cognitive Services API](https://docs.microsoft.com/en-us/python/api/overview/azure/cognitive-services?view=azure-python) and [Twitter v2 API's recent search functionality](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all project dependencies.

```bash
pip install requirements.txt
```

## Usage
If using a virtual environment (recommended) first create and activate it by running:
```bash
python3 -m venv <virtual environment name>
source <virtual environment name>/bin/activate
```

Tweet collection occurs by running `python main.py`. This script will store tweets, named entities for the tweets, and tweet hashtags in a Postgres database. For our purposes, we used Azure Database for PostgreSQL. Sentiment analysis will give the average sentiment and confidence levels for each tweet, which will be output as an aggregate (in our case, it will be a Canadian national average). Sentiment analysis occurs by running `python analytics.py`. Prior to running either script, please fill in all necessary credentials and keys in `secrets.py`.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
