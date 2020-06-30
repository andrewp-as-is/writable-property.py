<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/writable-property.svg?maxAge=3600)](https://pypi.org/project/writable-property/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/writable-property.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/writable-property.py/actions)

### Installation
```bash
$ [sudo] pip install writable-property
```

#### Examples
```python
>>> from writable_property import writable_property

>>> class Class:
    @writable_property
    def prop(self):
        return "value"

>>> obj = Class()
>>> obj.prop
"value"

>>> obj.prop = "new"
>>> obj.prop
"new"
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>