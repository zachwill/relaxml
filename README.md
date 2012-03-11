relaxml
=======

Converting XML to a dictionary should be easy.

Most of the current XML to dict projects are either unmaintained, slow,
or not well-tested. This shouldn't be the case.


Installation
------------

You can either clone this repo or use `pip`.

    pip install relaxml


Usage
-----

```python
>>> from relaxml import xml

>>> some_xml = open('file.xml')
>>> xml(some_xml)
{'ohai': {'xml': 'data'}}

>>> import requests as req
>>> content = req.get('http://lots.ofxml.com').text
>>> xml(content)
{'ohai': {'xml': 'data'}}
```
