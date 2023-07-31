# Import necessary libraries
from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

# Check if 'data_exporter' function is not already in the global scope, and if not, import it.
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# Define a data exporter function using the 'data_exporter' decorator.
# This function exports data to a BigQuery warehouse based on the provided configuration settings.
@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """

    # Set the path to the configuration file 'io_config.yaml' using the 'get_repo_path' function from 'repo_manager'.
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    
    # Define the configuration profile to use (in this case, it's set to 'default').
    config_profile = 'default'

    # Loop through each key-value pair in the 'data' dictionary.
    # The 'key' represents the table name, and the 'value' is a DataFrame containing the data to be exported.
    for key, value in data.items():
        # Define the destination table ID in the format 'data-with-soham.uber_data_engineering_yt.{key}'.
        # 'key' will be replaced with the actual table name.
        table_id = 'data-with-soham.uber_data_engineering_yt.{}'.format(key)
        
        # Create a BigQuery object and configure it using the 'ConfigFileLoader' with the specified configuration file and profile.
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            # Export the DataFrame 'value' to the BigQuery table specified by 'table_id'.
            DataFrame(value),
            table_id,
            if_exists='replace',  # Specify resolution policy if the table name already exists (replace existing table).
        )
