from ast_nodes import QueriesList, Query, CreateTable, ColumnDefinition, SimpleSelect
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
