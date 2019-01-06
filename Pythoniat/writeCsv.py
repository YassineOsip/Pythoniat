import xlsxwriter
workbook = xlsxwriter.Workbook('stats.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1','COUNTRY')
worksheet.write('B1','POPULATION')
worksheet.write('A2','INDIA')
worksheet.write('B2','10000')
worksheet.write('A3','CHINA')
worksheet.write('B3','20000')

workbook.close()