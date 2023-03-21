

# import xlsxwriter module
import xlsxwriter
 
# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('student.xlsx')
 
# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()
 
# Use the worksheet object to write
# data via the write() method.
worksheet.write(0, 0, 'NIM')
worksheet.write(0, 1, 'Nama')
worksheet.write(0, 2, 'Alamat')

worksheet.write(1, 0, '1317049')
worksheet.write(1, 1, 'eben manurung')
worksheet.write(1, 1, 'bekasi')

worksheet.write(2, 0, '1317039')
worksheet.write(2, 1, 'dina sihombing')
worksheet.write(2, 2, 'bekasi')

worksheet.write(3, 0, '1317079')
worksheet.write(3, 1, 'william sitorus')
worksheet.write(3, 2, 'bogor')




 
# Finally, close the Excel file
# via the close() method.
workbook.close()