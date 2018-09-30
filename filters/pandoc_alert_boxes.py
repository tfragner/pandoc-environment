#!/usr/bin/env python
import panflute as pf
import re

"""
Pandoc filter that causes emphasis to be rendered using
the custom macro '\myemph{...}' rather than '\emph{...}'
in latex.  Other output formats are unaffected.
"""

def alertboxes(e, doc):
    if type(e) == pf.Div and doc.format == 'latex':
        if 'notebox' in e.classes:
            left = pf.RawBlock('\\notebox{', format='latex')
            right = pf.RawBlock('}', format='latex')
            e.content = [left] + list(e.content) + [right]
            return e
        if 'tipbox' in e.classes:
            left = pf.RawBlock('\\tipbox{', format='latex')
            right = pf.RawBlock('}', format='latex')
            e.content = [left] + list(e.content) + [right]
            return e
        if 'warningbox' in e.classes:
            left = pf.RawBlock('\\warningbox{', format='latex')
            right = pf.RawBlock('}', format='latex')
            e.content = [left] + list(e.content) + [right]
            return e
        if 'cautionbox' in e.classes:
            left = pf.RawBlock('\\cautionbox{', format='latex')
            right = pf.RawBlock('}', format='latex')
            e.content = [left] + list(e.content) + [right]
            return e
        if 'importantbox' in e.classes:
            left = pf.RawBlock('\\importantbox{', format='latex')
            right = pf.RawBlock('}', format='latex')
            e.content = [left] + list(e.content) + [right]
            return e
        if 'compliancebox' in e.classes:
            left = pf.RawBlock('\\awesomebox{\\abIconCertificate}{2pt}{compliance}{', format='latex')
            right = pf.RawBlock('}', format='latex')
            e.content = [left] + list(e.content) + [right]
            return e


if __name__ == "__main__":
    pf.toJSONFilter(alertboxes)

