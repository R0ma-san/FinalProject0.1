import openpyxl 
from universities import models
import universities

wb = openpyxl.reader.excel.load_workbook(filename='2021.xlsx')

wb.active = 0
sheet = wb.active
for i in range(11, 134): #134
    models.University.objects.create(name=sheet['A'+str(i)].value, price = sheet['B'+str(i)].value,SAT = sheet['C'+str(i)].value+sheet['D'+str(i)].value, deadline_ed = sheet['E'+str(i)].value, deadline_rd = sheet['F'+str(i)].value, TOEFL = sheet['G'+str(i)].value, IELTS=sheet['H'+str(i)].value, GPA=3.5)
