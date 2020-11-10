



import os
from xlrd import open_workbook


class getExcel():
    def get_xls(self,xls_name, sheet_name):
        cls = []
        # get xls file's path
        self.proDir= os.path.dirname(os.path.dirname(__file__))
        xlsPath = os.path.join(self.proDir, "testFile", xls_name).replace("\\",'/')
        # open xls file
        file = open_workbook(xlsPath)
        # get sheet by name
        sheet = file.sheet_by_name(sheet_name)
        # get one sheet's rows

        nrows = sheet.nrows

        for i in range(nrows):

                cls.append(sheet.row_values(i))
        return cls


print(getExcel().get_xls("case_interface.xlsx","interface"))



