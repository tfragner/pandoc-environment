#!/usr/bin/env python
import panflute as pf

"""
Pandoc filter that renders QR Codes for youtube videos in LaTex
and an iframe in HTML
"""


def latex(s):
    return pf.RawInline(s, format='latex')

def html(s):
    return pf.RawInline(s, format='html')

def youtubevideo(e, doc):
    if type(e) == pf.Link and doc.format == 'latex':
        if 'youtube.com' in e.url or 'youtu.be' in e.url:
            if "for-image" in e.attributes:
                youtube = latex('\\vspace{-2.5em}\\todo[caption=' + pf.stringify(e) + ', color=black!0, linecolor=blue!50]{\\qrcode[height=1.75cm]{' + e.url + '}}')
            else:
                youtube = latex('\\todo[caption=' + pf.stringify(e) + ', color=black!0, linecolor=blue!50]{\\qrcode[height=1.75cm]{' + e.url + '}}')
            return [youtube]

if __name__ == "__main__":
    pf.toJSONFilter(youtubevideo)
