from frame.db import Db
from frame.error import ErrorCode
from frame.sql import Sql
from frame.value import User


class UsersDB(Db):

    def update(self, user_id, member_password, member_name, member_email):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userupdate % (member_password, member_name, member_email, user_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);
    def delete(self,user_id):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userdelete % (user_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);
    def insert(self,user_id,pwd,name,email,phone):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userinsert % (user_id,pwd,name,email,phone));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(cursor,conn);


    def selectone(self,user_id):
        user = None;
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlistone % user_id);
        c = cursor.fetchone();
        user = User(c[0],c[1],c[2],c[3],c[4],c[5]);
        super().close(cursor,conn);
        return user;

    def select(self):
        all = [];
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist);
        result = cursor.fetchall();
        for c in result:
            users = User(c[0],c[1],c[2],c[3],c[4],c[5]);
            all.append(users);
        super().close(cursor,conn);
        return all;
