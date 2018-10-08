#!/usr/bin/env python
import panflute as pf
import re

"""
Pandoc filter that causes emphasis to be rendered using
the custom macro '\myemph{...}' rather than '\emph{...}'
in latex.  Other output formats are unaffected.
"""


def latex(s):
    return pf.RawInline(s, format='latex')

def html(s):
    return pf.RawInline(s, format='html')

def youtubevideo(e, doc):
    if type(e) == pf.Link and doc.format == 'latex':
        if type(e.content[0]) == pf.Image and 'youtube.com' in e.url:
            image = e.content[0]
            width = 0.0
            youtube = latex('\\vspace{-3.3em}\\todo[caption=' + pf.stringify(e) + ', color=black!0, linecolor=blue!50]{\\qrcode[height=1.75cm]{' + e.url + '}}')
            if "width" in image.attributes:
                if '%' in image.attributes['width']:
                    width = str(float(image.attributes['width'][:-1]) / 100) + '\\linewidth'
                else:
                    width = str(int(image.attributes['width'][:-2]) / 300.0) + 'in'
                graphic = latex('\\begin{figure}\\centering\\includegraphics[width='+ width + ']{' + image.url + '}\\caption{' + pf.stringify(image) + '}\\end{figure}')
            else:
                graphic = latex('\\begin{figure}\\centering\\includegraphics{' + image.url + '}\\caption{' + pf.stringify(image) + '}\\end{figure}')
            return [graphic, youtube]
        elif 'youtube.com' in e.url:
            if "for-image" in e.attributes:
                youtube = latex('\\vspace{-2.5em}\\todo[caption=' + pf.stringify(e) + ', color=black!0, linecolor=blue!50]{\\qrcode[height=1.75cm]{' + e.url + '}}')
            else:
                youtube = latex('\\todo[caption=' + pf.stringify(e) + ', color=black!0, linecolor=blue!50]{\\qrcode[height=1.75cm]{' + e.url + '}}')
            return [youtube]
    elif type(e) == pf.Link and doc.format == 'html':
        if 'youtube.com' in e.url:
            regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})?&?(?P<params>.*)')
            match = regex.match(e.url)
            if match:
                params = match.group('params').split('&')
                for param in params:
                    if 't=' in param:
                        youtube = html('<div style="text-align: center;"><iframe height="250" src="' + 'https://www.youtube.com/embed/' + match.group('id') + '?rel=0&start=' + param.split('=')[1] + '" frameborder="0" allow="encrypted-media" allowfullscreen></iframe></div>')
                        return [youtube]
                youtube = html('<div style="text-align: center;"><iframe height="250" src="' + 'https://www.youtube.com/embed/' + match.group('id') + '?rel=0" frameborder="0" allow="encrypted-media" allowfullscreen></iframe></div>')
                return [youtube]


if __name__ == "__main__":
    pf.toJSONFilter(youtubevideo)
