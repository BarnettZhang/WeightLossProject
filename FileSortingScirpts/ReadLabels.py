import xlrd
from pathlib import Path


src = Path('')
# Directory of the file
loc = (src / 'contour_names.xlsx')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

collection = []
l_parotid_count = 0
r_parotid_count = 0
mandible_count = 0
cochlea_count = 0
brainstem_count = 0

l_parotid_label = []
r_parotid_label = []
mandible_label = []
cochlea_label = []
brainstem_label = []

l_parotid_miss = []

for row in range(0, 215):
    l_p_bool = False
    for column in range(0, 76):
        if 'parotid' in str(sheet.cell_value(row, column)).lower() and 'l' in str(sheet.cell_value(row, column)).lower() and 'plan' not in str(sheet.cell_value(row, column)).lower() and 'sub' not in str(sheet.cell_value(row, column)).lower():
            l_parotid_count += 1
            l_p_bool = True
            if str(sheet.cell_value(row, column)) not in l_parotid_label:
                l_parotid_label.append(str(sheet.cell_value(row, column)))
            break
    if not l_p_bool:
        l_parotid_miss.append(row+1)
    for column in range(0, 76):
        if 'parotid' in str(sheet.cell_value(row, column)).lower() and 'r' in str(sheet.cell_value(row, column)).lower() and 'l' not in str(sheet.cell_value(row, column)).lower() and 'sub' not in str(sheet.cell_value(row, column)).lower():
            r_parotid_count += 1
            if str(sheet.cell_value(row, column)) not in r_parotid_label:
                r_parotid_label.append(str(sheet.cell_value(row, column)))
            break
    for column in range(1, 76):
        if 'mandible' in str(sheet.cell_value(row, column)).lower():
            mandible_count += 1
            if str(sheet.cell_value(row, column)) not in mandible_label:
                mandible_label.append(str(sheet.cell_value(row, column)))
            break
    for column in range(1, 76):
        if 'cochlea' in str(sheet.cell_value(row, column)).lower():
            cochlea_count += 1
            if str(sheet.cell_value(row, column)) not in cochlea_label:
                cochlea_label.append(str(sheet.cell_value(row, column)))
            break
    for column in range(1, 76):
        if 'brainstem' in str(sheet.cell_value(row, column)).lower():
            brainstem_count += 1
            if str(sheet.cell_value(row, column)) not in brainstem_label:
                brainstem_label.append(str(sheet.cell_value(row, column)))
            break
    collection.append(sheet.row(row))

print(l_parotid_count, r_parotid_count, mandible_count, cochlea_count, brainstem_count)
print(l_parotid_miss)
print(len(l_parotid_miss))
