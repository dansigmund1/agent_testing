import os
import json
import psycopg2
import sqlite3
import argparse

class CheckSetup:
    def __init__(self):
        return
    
    def db_connect(self):
        with open("files/db.json") as db_f:
            dbs = json.load(db_f)
        return dbs
    
    def get_workflows(self):
        with open("files/workflows.json") as wf_f:
            wfs = json.load(wf_f)
        return wfs
    
    def generate_report(self, dbs, wfs):
        for db in dbs:
            for wf in wfs:
                print(f"DB: {db}")
                print(f"WF: {wf}")
        return

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--date', help="Date to check", required=True)
    args = parser.parse_args()

    cs = CheckSetup()
    dbs = cs.db_connect()
    wfs = cs.get_workflows()
    cs.generate_report(dbs, wfs)