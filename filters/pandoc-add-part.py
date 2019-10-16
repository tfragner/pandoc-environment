"""
Set all headers to level 1
"""

from panflute import *

first = True

def action(elem, doc):
    global first
    if first:
        m = doc.get_metadata('title', 'Unknown')
        h1 = RawBlock('\part{'+ m + '}', format='latex')
        doc.content.insert(0,h1)
        first = False
        
def finalize(doc):
    pass

def main(doc=None):
    return run_filters(actions=[action], doc=doc, finalize=finalize)

if __name__ == '__main__':
    main()