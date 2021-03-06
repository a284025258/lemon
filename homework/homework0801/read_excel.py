import openpyxl


class ReadExcel(object):
    def __init__(self, filename, sheet_name):
        self.filename = filename
        self.sheet_name = sheet_name

    def open(self):
        """打开文件  读数据与写数据必须分别创建 Excel 对象，否则不会正确写入"""
        self.workbook = openpyxl.load_workbook(self.filename)
        self.sheet = self.workbook[self.sheet_name]

    def read_data(self) -> list:
        """读数据"""
        self.open()
        rows = list(self.sheet.rows)
        # 获取第一行的单元格数据并添加到 title 列表
        title = [row.value for row in rows[0]]
        # 获取第一行之外的所有单元格数据
        cases = []
        for row in rows[1:]:
            data = [r.value for r in row]
            cases.append(dict(zip(title, data)))
        return cases

    def write_data(self, row, col, value):
        """写数据"""
        self.open()
        self.sheet.cell(row=row, column=col, value=value)
        self.workbook.save(self.filename)


if __name__ == "__main__":
    read_excel = ReadExcel(r"./cases.xlsx", "register")
    read_excel.read_data()
    # read_excel.write_excel(6, 1, "test")
