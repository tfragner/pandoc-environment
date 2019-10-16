"""
Set all headers to level 1
"""

from panflute import *
from collections import OrderedDict

last = []
first = True
def action(elem, doc):
    global first
    if first:
        meta = doc.get_metadata()
        if not 'versionen' in meta.keys():
            first = False
            return
        last.append(meta['versionen'][-1])
        rows = []
        versions = []
        for x in meta['versionen']:
            version = Para(Str(x['version']))
            ersteller = Para(Str(x['ersteller']))
            erstelldatum = Para(Str(x['erstelldatum']))
            pruefer = Para(Str(x['pruefer']))
            pruefdatum = Para(Str(x['pruefdatum']))
            freigeber = Para(Str(x['freigeber']))
            freigabedatum = Para(Str(x['freigabedatum']))
            versions.append(TableRow(TableCell(Para(Str(x['version']))), TableCell(Para(Str(x['kurzbeschreibung'])))))
            rows.append(TableRow(TableCell(version), TableCell(ersteller), TableCell(erstelldatum), TableCell(pruefer), TableCell(pruefdatum), TableCell(freigeber), TableCell(freigabedatum)))

        header = TableRow(TableCell(Para(Str('Ver'))), TableCell(Para(Str('Ersteller'))), TableCell(Para(Str('Datum'))), TableCell(Para(Str('Prüfer'))), TableCell(Para(Str('Datum'))), TableCell(Para(Str('Freigeber'))), TableCell(Para(Str('Datum'))))
        table = Table(*rows, header=header,width=[1,2,4,2,4,2,4])
        header2 = TableRow(TableCell(Para(Str('Ver'))), TableCell(Para(Str('Ersteller'))))
        table2 = Table(*versions, header=header2, width=[1,10])
        h0 = Header(Str("Änderungsnachweise"), level=2)
        h1 = Header(Str("Versionen"), level=3)
        h2 = Header(Str("Änderungen"), level=3)
        
        doc.content.insert(0, table2)
        doc.content.insert(0, table)
        doc.content.insert(0, Para(Strong(Str(meta['slug']))))
        first = False

        
def finalize(doc):
    if len(last) > 0:
        author = MetaString(last[0]['ersteller'])
        date = MetaString(last[0]['erstelldatum'])
        kurzbeschreibung = MetaString(last[0]['kurzbeschreibung'])
        doc.metadata['author'] = author
        doc.metadata['version'] = MetaString(last[0]['version'])
        doc.metadata['ersteller'] = MetaString(last[0]['ersteller'])
        doc.metadata['erstelldatum'] = MetaString(last[0]['erstelldatum'])
        doc.metadata['pruefer'] = MetaString(last[0]['pruefer'])
        doc.metadata['pruefdatum'] = MetaString(last[0]['pruefdatum'])
        doc.metadata['freigeber'] = MetaString(last[0]['freigeber'])
        doc.metadata['freigabedatum'] = MetaString(last[0]['freigabedatum'])
        doc.metadata['date'] = date
        doc.metadata['kurzbeschreibung'] = kurzbeschreibung

def main(doc=None):
    return run_filters(actions=[action], doc=doc, finalize=finalize)

if __name__ == '__main__':
    main()