# Utitities
import json

def jsonDefault(object):
    return object.__dict__

def console_offset():
    print "\n\n"

def maybe_parse_int(val):
    try:
        return int(val)
    except ValueError as verr:
        pass

def enum(**enums):
    return type('Enum', (), enums)


Action = enum(CREATE=1, READ=2, UPDATE=3, DELETE = 4)
HttpMethods = enum(GET=1, POST=2, PATCH=3, DELETE = 4)
