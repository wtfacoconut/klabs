#!/usr/bin/python3
schema = {
    'string_with_quotes': {
        'required': True,
        'type': 'string'
    },
    'string_with_without_quotes': {
        'required': True,
        'type': 'string'
    },
    'integer_number': {
        'required': True,
        'type': 'number',
        'min': 11,
        'max': 20
    },
    'floating_point_number': {
        'required': True,
        'type': 'float',
        'min': 0.1,
        'max': 0.99
    },
    'date': {
        'required': True,
        'type': 'date'
    },
    'boolean': {
        'required': True,
        'type': 'boolean'
    },
    'null_value': {
        'required': False,
        'nullable':  True,
        'type': 'boolean'
    }
    # 'metrics': {
    #     'required': True,
    #     'type': 'dict',
    #     'schema': {
    #         'percentage': {
    #             'required': True,
    #             'type': 'dict',
    #             'schema': {
    #                 'value': {
    #                     'required': True,
    #                     'type': 'number',
    #                     'min': 0,
    #                     'max': 100
    #                 },
    #                 'trend': {
    #                     'type': 'string',
    #                     'nullable': True,
    #                     'regex': '^(?i)(down|equal|up)$'
    #                 }
    #             }
    #         }
    #     }
    #}
}

import checker_common as C
import sys
if __name__ == "__main__":
    C.checker(schema, sys.argv[1])