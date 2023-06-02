import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():

    print('Please enter sales data from the last market.')
    print('data should be six number, separated by commas.')
    print('Exemple: 10,20,30,40,50\n')
    
    data_str = input('Enter your data here:')
    
    sales_data = data_str.split(',')
    validate_data(sales_data)
    
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError, if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """    
    try:
        if len(values) != 6:
            raise ValueError(
                f'Exactly 6 values required, you provide {len(values)}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')
        
get_sales_data()