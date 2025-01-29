import sqlite3
from sqlite3 import connect
import   time
#
# connect = sqlite3.connect("tgbd.db")
# cursor = connect.cursor()
# cursor.execute("create table blockeduser (id integer primary key autoincrement,"
#                "username text not null,"
#                "userid integer unique not null,"
#                "blockingdate text not null,"
#                "termtime integer not null,"
#                "riason not null)")


def name_id_write(name,id):
    try:
        connect = sqlite3.connect("tgbd.db")
        cursor = connect.cursor()
        rt=time.time()
        cursor.execute("INSERT INTO userdata (username, userid, registrationdate) values (? ,? ,?)",[name,id,rt])
        connect.commit()
        connect.close()
    except:
        print(name,"this user is welldone")

def blocking(name,id,term,ris):
        connect = sqlite3.connect("tgbd.db")
        cursor = connect.cursor()
        bt=time.time()
        cursor.execute("INSERT INTO blockeduser (username, userid, blockingdate ,termtime,riason) values (? ,? ,?,?,?)",[name,id,bt,term,ris])
        connect.commit()
        connect.close()
        print(name,"user baned")





