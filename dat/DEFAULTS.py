default_dict =  {'PARAMS1': 
                    {'Default Path'                     : 'dat/params1.test',
                    'DAT':
                        {'Section 1':
                            {'param 1 int'              : '1',
                            'param 2 float'             : '0.25',
                            'param 3 string'            : 'string',
                            'param 4 list'              : 'can, be, list',
                            'param 5 dict'              : '{"or":"dictionary"}'
                                                        }}},
                 
                'PARAMS2':
                    {'Default Path'                     : 'dat/params2.test',
                    'DAT':
                        {'Section 1':
                             {'param 1 required'        : '*',
                             'param 2'                  : '1, 2, 3, 4, 5',
                             'param 3'                  : '20'},
                        'Section 2':
                            {'param 1'                  : 'True',
                             'param 2'                  : 'False'
                                                        }}}}