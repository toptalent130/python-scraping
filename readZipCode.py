import pandas as pd
def readZipCode():
    # pip install xlrd
    zipcodes = pd.read_excel (r'C:\\Users\\Charlie\\Downloads\\Compressed\\WebScraping-main\\zipcode.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    df = pd.DataFrame(zipcodes, columns=['zip_code'])
    return [ row["zip_code"] for index, row in df.iterrows() ]
