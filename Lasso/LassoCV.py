
src = Path('../Data')
worksheet = openpyxl.load_workbook(src / 'Patient and Treatment Characteristics.xlsx')['Filtered']


# Data reading from excel file
# Volumetric features
volume = np.array([cell.value for (cell, ) in worksheet["D2:D177"]])
surface_area = np.array([cell.value for (cell, ) in worksheet["E2:E177"]])
sphericity = np.array([cell.value for (cell, ) in worksheet["F2:F177"]])
eccentricity = np.array([cell.value for (cell, ) in worksheet["G2:G177"]])
compactness = np.array([cell.value for (cell, ) in worksheet["H2:H177"]])

# DVH features
DVH_max = np.array([cell.value for (cell, ) in worksheet["I2:I177"]])
DVH_mean = np.array([cell.value for (cell, ) in worksheet["J2:J177"]])
DVH_min = np.array([cell.value for (cell, ) in worksheet["K2:K177"]])
DVH_std = np.array([cell.value for (cell, ) in worksheet["L2:L177"]])

bw_loss = np.array([cell.value for (cell, ) in worksheet["U2:U177"]])

