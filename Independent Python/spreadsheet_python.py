import xlrd

path = "College Emails.xlsx"

inputWorkbook = xlrd.open_workbook(path)
inputWorksheet = inputWorkbook.sheet_by_index(0)

names = []
emails = []

for i in range(1,inputWorksheet.nrows):
    names.append(inputWorksheet.cell_value(i,0))
    emails.append(inputWorksheet.cell_value(i,1))
    

