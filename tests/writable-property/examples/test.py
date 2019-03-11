#!/usr/bin/env python
from writable_property import writable_property


class Class:
    @writable_property
    def prop(self):
        return "value"


obj = Class()
for value in ["value", "new", None]:
    obj.prop = value
    assert obj.prop == value
