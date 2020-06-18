from ast_nodes import *
import json


class Queries:

    def select_query(query: SimpleSelect):
        fields = query._column_results
        lp = query._where[0]
        if(query._where[1].isdigit()):
            rp = int(query._where[1])
        else:
            rp = query._where[1]
        operand = query._oper
        table = query._table_name
        # db = Condition.read_json()
        with open('./sw_templates.json', 'r') as f:
            tables = json.loads(f.read())
            if table in tables:
                print(tables[table])
                if operand == '=':
                    for row in tables[table]:
                        if row[lp] == rp:
                            for fi in fields:
                                print(row[fi])
                if operand == '>':
                    for row in tables[table]:
                        if row[lp] > rp:
                            for fi in fields:
                                print(row[fi])
                if operand == '<':
                    for row in tables[table]:
                        if row[lp] < rp:
                            for fi in fields:
                                print(row[fi])
                if operand == '>=':
                    for row in tables[table]:
                        if row[lp] >= rp:
                            for fi in fields:
                                print(row[fi])
                if operand == '<=':
                    for row in tables[table]:
                        if row[lp] <= rp:
                            for fi in fields:
                                print(row[fi])
            else:
                print("There is no such table in file")

    def insert_query(query: Insert):
        table = query._table_name
        d = dict(short='dict', long='dictionary')
        keys = query._column_name
        values = query._values
        new_tab = ()
        with open('./sw_templates.json') as f:
            tables = json.loads(f.read())
            dict_out = {}
            for k, v in zip(keys, values):
                dict_out[k] = v
            tables[table].append(dict_out)
            new_tab = tables
        with open('./sw_templates.json', 'w') as f:
            json.dump(new_tab, f)
        for table in tables.items():
            print(table)

    def delete_all_query(query: Delete):
        table = query._table_name
        with open('./sw_templates.json', 'r') as f:
            tables = json.loads(f.read())
            tables[table] = []
        with open('./sw_templates.json', 'w') as f:
            json.dump(tables, f)
            print(tables)