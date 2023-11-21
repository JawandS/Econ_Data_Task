# data src: https://data.census.gov/table/CBP2021.CB2100CBP?q=CBP2021.CB2100CBP&g=040XX00US51$5000000

# import pandas
import pandas as pd

def get_emp_per_estab(df):
    # calculate employees per establishment for District 1 and District 11
    for district in ["District 1 ", "District 11 "]:
        # filter the dataframe to only include the district
        df_district = df[[district in c for c in list(df["Geographic Area Name"])]]
        # get total employees and establishments
        total_establishments = sum(int(val.replace(",", "")) for val in list(df_district["Number of establishments"]))
        total_employees = sum(int(val.replace(",", "")) for val in list(df_district["Number of employees"]))
        # output the results
        print(f"{district} has {total_employees/total_establishments} employees per establishment.")

# find the district with the highest payroll for a particular meaning of NAICS code
def find_max_payroll(df, code_meaning):
    # filter the dataframe to only include the code meaning
    df_code = df[[code_meaning in c for c in list(df["Meaning of NAICS Code"])]]
    # get the district with the highest payroll
    max_payroll = max(int(val.replace(",", "")) for val in list(df_code["Annual payroll ($1,000)"]))
    # get the district with the highest payroll
    district = df_code.loc[[int(val.replace(",", "")) == max_payroll for val in list(df_code["Annual payroll ($1,000)"])]]
    # output the results
    print(f"{district['Geographic Area Name'].iloc[0]} has the highest payroll of {max_payroll} for {code_meaning}.")

# main method
if __name__ == "__main__":
    # read in the csv file
    df = pd.read_csv('data.txt', sep='\t')
    # print the columns
    # print(df.columns)

    # functions
    # get_emp_per_estab(df)

    find_max_payroll(df, "Construction")