#CODE
import requests
import pandas as pd
import matplotlib.pyplot as plt
import pwinput
from typing import Dict, Optional
from datetime import datetime
import config  # Separate config.py file containing API_KEY, Username, Password

class FinancialDataAnalyzer:

    """
    Main class for fetching, processing, and visualizing financial data from NASDAQ API

    """ 
    
    def __init__(self, api_key: str, username: str, password: str):

        """
        Initialize the Financial Data Analyzer.
        
        api_key: NASDAQ Data Link API key from config
        username: Required username for application access
        password: Required password for application access

        """
        self.api_key = config.api_key
        self.api_url = "https://data.nasdaq.com/api/v3/datatables/MER/F1"
        self.username = config.username
        self.password = config.password
        self.raw_data = None
        self.processed_data = None
        
    def authenticate(self) -> bool:

        """

        Security Implementation:
        - Uses pwinput library to mask password entry
        - Validates credentials before allowing API access

        """

        print("-" * 50)
        print("FINANCIAL DATA ANALYSIS TOOL - LOGIN")
        print("-" * 50)
        
        entered_username = input("Enter Username: ")
        
        if entered_username != self.username:
            print("Incorrect username, access denied")
            return False
            
        print(f"Welcome, {self.username}")
        
        entered_password = pwinput.pwinput("Enter Your Password: ")
        
        if entered_password != self.password:
            print("Password incorrect, access denied")
            return False
            
        print("Login successful...")
        print("API Key loaded successfully")
        return True
    
    def fetch_data(self, records_per_page: int = 10000) -> bool:

        """

        Fetches financial data from NASDAQ API

        """
        print("\n" + "-" * 50)
        print("FETCHING DATA FROM NASDAQ API...")
        print("-" * 50)
        
        parameters = {
            'api_key': self.api_key,
            'qopts.per_page': records_per_page
        }
        
        try:
            response = requests.get(self.api_url, params=parameters)
            response.raise_for_status()  # Raise exception for bad status codes
            
            self.raw_data = response.json()
            print(f"Successfully fetched {len(self.raw_data['datatable']['data'])} records")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return False
    
    def process_data(self) -> Optional[pd.DataFrame]:

        """

        Transform raw JSON data into structured DataFrame with cleaned values.

        """
        if not self.raw_data:
            print("No data to process. Please fetch data first.")
            return None
        
        print("\n" + "-" * 50)
        print("PROCESSING AND CLEANING DATA...")
        print("-" * 50)
        
        try:
            # Extract data from nested JSON structure
            data = self.raw_data['datatable']['data']
            columns = [col['name'] for col in self.raw_data['datatable']['columns']]
            
            # Create DataFrame
            df = pd.DataFrame(data, columns=columns)
            print(f"Created DataFrame with {len(df)} rows and {len(df.columns)} columns")
            
            # Convert date column to datetime format
            # errors='coerce' converts invalid dates to NaT (Not a Time) instead of crashing
            df['reportdate'] = pd.to_datetime(df['reportdate'], errors='coerce')
            
            # Select only necessary columns for analysis
            necessary_columns = [
                'reportid',
                'reportdate',
                'reporttype',
                'longname',
                'country',
                'region',
                'indicator',
                'statement',
                'amount'
            ]
            df = df[necessary_columns]
            
            # Clean country codes to readable names
            country_mapping = self._get_country_mapping()
            df['country'] = df['country'].replace(country_mapping)
            print(f"Mapped {len(country_mapping)} country codes to full names")
            
            # Rename columns to snak case for Python convention
            df.columns = [
                'report_id',
                'report_date',
                'report_type',
                'company_name',
                'country',
                'region',
                'indicator',
                'statement',
                'amount'
            ]
            
            # Filter for EBITDA Margin indicator
            filtered_df = df[df['indicator'] == 'EBITDA Margin'].copy()
            print(f"Filtered to {len(filtered_df)} EBITDA Margin records")
            
            # Removes irregular data 'Immutep LTD'
            filtered_df = filtered_df[filtered_df['company_name'] != 'Immutep Ltd']
            print("Removed outlier companies for consistent analysis")
            
            self.processed_data = filtered_df
            return filtered_df
            
        except Exception as e:
            print(f"Error processing data: {e}")
            return None
    
    def visualize_trends(self, window_size: int = 3) -> None:

        """

        Create time-series visualization of EBITDA Margin trends

        """
        if self.processed_data is None or self.processed_data.empty:
            print("No processed data available for visualization.")
            return
        
        print("\n" + "-" * 50)
        print("GENERATING VISUALIZATION...")
        print("-" * 50)
        
        # Calculate mean EBITDA Margin for each reporting date
        time_trend = self.processed_data.groupby('report_date')['amount'].mean()
        
        # Create figure with larger size for readability
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # Plot original data with transparency
        ax.plot(time_trend.index, time_trend.values, alpha=0.3, label='Original Data', linewidth=1, color='lightblue')
        
        # Calculate and plot moving average for trend identification
        smoothed = time_trend.rolling(window=window_size, center=True).mean()
        ax.plot(smoothed.index, smoothed.values, label=f'{window_size}-Period Moving Average', linewidth=2, color='darkblue')
        
        # Configure chart aesthetics
        ax.set_xlabel('Report Date', fontsize=12)
        ax.set_ylabel('Average EBITDA Margin (%)', fontsize=12)
        ax.set_title("EBITDA Margin Over Time (Smoothed)", fontsize=14, fontweight='bold')
        ax.legend(loc='best')
        ax.grid(True, alpha=0.3, linestyle='--')
        
        # Rotate x-axis labels for readability
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        print("Visualization generated successfully")
        plt.show()
    
    @staticmethod
    def _get_country_mapping() -> Dict[str, str]:
        # This takes country codes and converts them to full names, APIS tend to use CC, making it harder to read
        return {
            "AUS": "Australia",
            "BEL": "Belgium",
            "BHS": "Bahamas",
            "BMU": "Bermuda",
            "BRA": "Brazil",
            "CAN": "Canada",
            "CHE": "Switzerland",
            "CHL": "Chile",
            "CYM": "Cayman Islands",
            "DEU": "Germany",
            "DNK": "Denmark",
            "ESP": "Spain",
            "FIN": "Finland",
            "FRA": "France",
            "GBR": "United Kingdom",
            "HKG": "Hong Kong",
            "IDN": "Indonesia",
            "IND": "India",
            "IRL": "Ireland",
            "ISR": "Israel",
            "ITA": "Italy",
            "JPN": "Japan",
            "KOR": "South Korea",
            "LBR": "Liberia",
            "PAN": "Panama",
            "USA": "United States",
            "VGB": "British Virgin Islands"
        }
    
    def run(self) -> None:
        """

        Pipeline Flow:
        - Authenticate user
        - Fetch data from API
        - Process and clean data
        - Generate visualization

        """
        # Authentication
        if not self.authenticate():
            print("\nAuthentication failed. Exiting program.")
            return
        
        # Data Extraction
        if not self.fetch_data():
            print("\nData fetch failed. Exiting program.")
            return
        
        # Data Transformation
        if self.process_data() is None:
            print("\nData processing failed. Exiting program.")
            return
        
        # Visualization
        self.visualize_trends()
        
        print("\n" + "-" * 50)
        print("ANALYSIS COMPLETE")
        print("-" * 50)


def main():
    # Initialize analyzer with credentials from config file
    analyzer = FinancialDataAnalyzer(
        api_key=config.api_key,
        username=config.username,
        password=config.password
    )
    
    # Execute analysis pipeline
    analyzer.run()


if __name__ == "__main__":
    # This ensures the script only runs when executed directly
    main()
