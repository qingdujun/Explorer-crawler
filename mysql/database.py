# -*- coding: utf-8 -*-
from db import Dbsql
class Database(object):
    def __init__(self):
        pass;

    def __enter__(self):
        return self;

    def __exit__(self, type, value, trace):
        if type is not None:
            print(type);
            print(value);  
        self.close();

    def execute(self, sql):
        with Dbsql() as db:
            db.execute(sql);

    def close(self):
        Dbsql().close();
    
    def insert(self, data):
        #for key, value in data.iteritems():
        #    pass;
        pass;

    def delete(self, data):
        pass;

    def update(self, data):
        pass;

    def select(self, data):
        pass;

if __name__ == '__main__':
    with Database() as db:
        pass;