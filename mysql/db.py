# -*- coding: utf-8 -*-
import pymysql
import threading

class Dbsql(object):
    _instance_lock = threading.Lock();

    def __new__(self, *args, **kwargs):
        if not hasattr(Dbsql, "_instance"):
            with Dbsql._instance_lock:
                if not hasattr(Dbsql, "_instance"):
                    Dbsql._instance = object.__new__(self);
                    self.db = pymysql.connect(host="localhost", user="root", passwd="12345678", db="cdosdb", port=3306, charset='utf8');
        return Dbsql._instance

    def __init__(self):
        pass;

    def __enter__(self):
        return self;

    def __exit__(self, type, value, trace):
        if type is None:
            self.db.commit();
        else:
            print(type);
            print(value);
            self.db.rollback();
        cursor = self.db.cursor();
        cursor.close();

    def execute(self, sql):
        cursor = self.db.cursor();
        cursor.execute(sql);
    
    def close(self):
        self.db.close();

if __name__ == '__main__':
    with Dbsql() as db:
        pass;