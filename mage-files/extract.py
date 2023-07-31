# Import necessary libraries
import io
import pandas as pd
import requests

# Check if 'data_loader' and 'test' functions are not already in the global scope, and if not, import them.
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# Define a data loader function using the 'data_loader' decorator.
# The function loads data from the specified API endpoint and returns a pandas DataFrame.
@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # URL of the API endpoint that contains the data in CSV format.
    url = 'https://storage.googleapis.com/uber-data-engineering-project-darshil/uber_data.csv'
    
    # Send a GET request to the API endpoint and retrieve the response.
    response = requests.get(url)

    # Convert the response text to a pandas DataFrame using io.StringIO and pd.read_csv.
    return pd.read_csv(io.StringIO(response.text), sep=',')

# Define a test function using the 'test' decorator.
# This function is used for testing the output of the data loader function.
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # Check if the output is not None, which indicates that the data was loaded successfully.
    assert output is not None, 'The output is undefined'
