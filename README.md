- Financial Data Analysis Tool 

A Python-based financial analysis application that integrates with the NASDAQ Data Link API to analyze EBITDA Margin trends across global companies.

Project Purpose

This project was created to:
- Learn API Integration**: Gain hands-on experience with RESTful APIs and authentication workflows
- Explore Python Capabilities**: Utilize pandas for data manipulation and matplotlib for visualization
- Demonstrate Banking Skills: Showcase ability to analyze financial metrics relevant to banking and consultancy roles

- Business Context

EBITDA Margin (Earnings Before Interest, Taxes, Depreciation, and Amortization Margin) is a critical financial metric used by:
- Banking Analysts - to assess company operational efficiency
- Solutions Consultants - to evaluate client financial health
- Investment Advisors - to compare companies across industries

This tool automates the extraction, cleaning, and visualization of EBITDA Margin data, demonstrating skills essential for financial technology roles.

- Key Features

- Secure Authentication: Username/password verification before API access
- RESTful API Integration**: Connects to NASDAQ Data Link MER/F1 endpoint
- Data Cleaning Pipeline: 
  - Converts country codes to readable names
  - Handles date parsing errors gracefully
  - Removes outliers for consistent analysis
- Time-Series Analysis: Calculates moving averages to identify trends
- Interactive Visualization: Generates professional charts with matplotlib
- Modular Architecture: Object-oriented design for maintainability

- Technologies Used

| Technology | Purpose | Why I Chose It |
|------------|---------|----------------|
| Python | Core language | Industry standard for data analysis |
| Requests| HTTP API calls | Simple, reliable library for REST APIs |
| Pandas | Data manipulation | Essential tool for financial data analysis |
| Matplotlib | Data visualization | Create professional charts and graphs |
| Seaborn| Enhanced styling | Improve visual appeal of charts |
| pwinput | Secure password input | Mask credentials for security |

- Prerequisites

- Python 3.7 or higher
- NASDAQ Data Link API key ([Get one here](https://data.nasdaq.com/sign-up))
- pip (Python package manager)


- Install dependencies

pip install requests pandas matplotlib seaborn pwinput


- Create config file (IMPORTANT)

- config.py
api_key = "YOUR_NASDAQ_API_KEY_HERE"
username = "your_username"
password = "your_password"


You'll be prompted to:
1. Enter your username
2. Enter your password (hidden input)
3. Wait for data fetching and processing
4. View the generated EBITDA Margin trend chart

- Project Architecture

financial-data-analyzer/
│
├── financial_analyzer.py    # Main application
├── config.py                 # API credentials
├── README.md                 # This file
├── requirements.txt          # Python dependencies


Code Structure

FinancialDataAnalyzer
│
├── __init__()           # Initialize with credentials
├── authenticate()       # Verify user credentials
├── fetch_data()         # GET request to NASDAQ API
├── process_data()       # Clean and transform data
├── visualize_trends()   # Generate matplotlib chart
└── run()                # Orchestrate entire pipeline



- Key Transformations:

- Date Parsing: Converts strings to datetime objects with error handling
- Country Mapping: Translates ISO codes (e.g."USA") to "United States"
- Filtering: Isolates EBITDA Margin indicator from broader dataset
- Outlier Removal: Removes anomalous companies (Immutep Ltd)

- Analysis & Visualization:

- Groups data by report date
- Calculates mean EBITDA Margin for each period
- Applies 3-period moving average to smooth volatility
- Generates dual-line chart (original + smoothed data)

- Technical Skills

- API Authentication**: Working with API keys and authentication workflows
- Data Cleaning**: Handling real-world messy data (missing values, outliers, date parsing)
- Pandas Proficiency**: DataFrame manipulation, groupby operations, datetime handling
- Error Handling**: Using try-except blocks and graceful degradation
- OOP Principles**: Designing classes with single responsibility and clear interfaces

- Banking/Finance Concepts

- EBITDA Margin: Understanding this key profitability metric
- Time-Series Analysis: Applying moving averages to identify trends
- Data Quality: Recognizing importance of outlier removal in financial analysis

- Software Engineering

- Configuration Management: Separating credentials from code
- Code Documentation: Writing clear docstrings and comments
- Modular Design: Breaking code into reusable, testable functions

- Security Considerations

- Credentials stored in separate `config.py` file
- Password input masked with `pwinput` library
- API key never hardcoded in main script

- Resources & References

- [NASDAQ Data Link API Documentation](https://docs.data.nasdaq.com/)
- Pandas Documentation - (https://pandas.pydata.org/docs/)
- Matplotlib Tutorials - (https://matplotlib.org/stable/tutorials/index.html)
- EBITDA Explained - https://www.investopedia.com/terms/e/ebitda.asp
- https://www.youtube.com/watch?v=Na8h09Goovk (Base inspiration, added tweaks and made it more project Portfolio worthy)

- About me

I'm an aspiring Solutions Consultant/Architect interested in banking technology and financial systems. This project represents my first complete API integration and demonstrates my commitment to:
- Learning by building practical applications
- Writing clean, documented code
- Understanding business context behind technical solutions
- Preparing for roles in financial technology


- Contributing

This is a learning project, but feedback is welcome! Feel free to:
- Open issues for bugs or suggestions
- Submit pull requests with improvements
- Reach out with questions or advice


Built with Love and Python | My First API Integration Project | 2025
