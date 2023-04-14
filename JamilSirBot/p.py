import gspread
from datetime import datetime

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(2)))
    return str(len(str_list)+1)

sa = gspread.service_account(filename="service_account.json")
sh = sa.open("Gspread")

worksheet_list = sh.worksheets()  #joto gula worksheet ase shob gulam nam dekhabe
# worksheet = sh.add_worksheet(title="A worksheet", rows=100, cols=20) #worksheet add kortese

# Open the spreadsheet by name
spreadsheet_name = 'Gspread'
sheet_name = 'Daily Updates'
sheet = sa.open(spreadsheet_name).worksheet(sheet_name)

# Search for the specific ID in the first row
print("Your ID: ")
id_to_find = input()                           #Je ID ta search korbo sheta ei variable e boshbe
date = datetime.today().strftime('%d/%m/%Y')                               #Je date er update nicchi sheta ekhane boshbe
first_row = sheet.row_values(1)
index_of_id = first_row.index(id_to_find) + 1  # add 1 because index starts from 0

# Find the first empty cell in the column
column = sheet.col_values(index_of_id)
first_empty_cell_index = len(column) + 1

# Insert your input data in the first empty cell in the column
spent_time = '6 hours'
cell_to_update = sheet.cell(first_empty_cell_index, index_of_id)
cell_to_update.value = spent_time
sheet.update_cell(len(sheet.col_values(1))+1, index_of_id, spent_time)
sheet.update_cell(len(sheet.col_values(1))+1, 1, date)









