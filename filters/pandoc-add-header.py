"""
Set all headers to level 1
"""

from panflute import *

first = True

def action(elem, doc):
    global first
    if first:
        m = doc.get_metadata('title', 'Unknown')
        debug(m)
        h1 = Header(Str(m), level=1)
        doc.content.insert(0,h1)
        doc.content.insert(1,Para(Str(m)))
        first = False
        
def finalize(doc):
    pass

def main(doc=None):
    return run_filters(actions=[action], doc=doc, finalize=finalize)

if __name__ == '__main__':
    main()