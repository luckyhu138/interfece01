import os
from xml.etree import ElementTree as ElementTree

class getXml():
    def get_xml(self):
        dat = {}
        self.proDir = os.path.dirname(os.path.dirname(__file__))
        sql_path = os.path.join(self.proDir, "testFile", "SQL.xml").replace("\\", "/")
        tree = ElementTree.parse(sql_path)
        for db in tree.findall("database"):
            db_name = db.get("name")
            dat['db_name'] = db_name
            # print(db_name)
            for tb in db.getchildren():
                table_name = tb.get("name")
                # print(table_name)
                dat['tb_name'] = table_name
                for data in tb.getchildren():
                    sql_id = data.get("id")
                    #lstrip去掉一句话开头的空格
                    dat[sql_id] = data.text.split('\n')[1].lstrip()
        return dat

    def getSql(self,sql_id):
        dat=self.get_xml()
        sql=dat[sql_id]
        return sql


