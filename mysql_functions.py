import _mysql
import MySQLdb as mdb

from config import *

con = mdb.connect(host, username, password, DBName , charset='utf8')

# Execute Mysql Query ( select , update , insert , delete ----) , we use this function to update next record
def excuteQuery(query):
        try:
                with con:
                        cur = con.cursor(mdb.cursors.DictCursor)
                        tt=cur.execute(query)
                        rows = cur.fetchall()
			return rows
		return []
        except Exception as ex:
                print str(ex)
		return None

# For insert new row , we use this function to insert posts and comments
def insert_row(query , data):
        try:
                with con:
                        cur = con.cursor()
                        tt=cur.execute(query,data)
			return 1
        except Exception as ex:
                print str(ex);
		return -1
