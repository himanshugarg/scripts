import sys
import os
import json
import pdb
import xml.etree.ElementTree as ET
import zipfile

def parseNavPoint(nodes):
    title = './{{{daisy}}}navLabel/{{{daisy}}}text'.format(**nsmap)
    path  = './{{{daisy}}}content'.format(**nsmap)
    nav   = './{{{daisy}}}navMap/{{{daisy}}}navPoint'.format(**nsmap)

    zf    = zipfile.ZipFile(sys.argv[1])
    ncx   = [n for n in zf.namelist() if n.lower().endswith(nodes[0].attrib['href'].lower())][0]
            
    return [{
       'title': node.findall(title)[0].text,
       'path' : os.path.join(pathPrefix, node.findall(path)[0].attrib['src'])
     } for node in ET.fromstring(zf.read(ncx)).findall(nav)]

def text(nodes):
    return nodes[0].text

def href(nodes):
    return os.path.join(pathPrefix, nodes[0].attrib['href'])

nsmap = { 'dc'   : 'http://purl.org/dc/elements/1.1/',
          'idpf' : 'http://www.idpf.org/2007/opf',
          'daisy': 'http://www.daisy.org/z3986/2005/ncx/' }

output = {
  "title":          ("./{{{idpf}}}metadata/dc:title".format(**nsmap), text),
  "author":         ("./{{{idpf}}}metadata/dc:creator".format(**nsmap), text),
  "publisher":      ("./{{{idpf}}}metadata/dc:publisher".format(**nsmap), text),
  "coverImagePath": ('./{{{idpf}}}manifest/{{{idpf}}}item[@id="cover-image"]'.format(**nsmap), href),
  "chapters":       ('./{{{idpf}}}manifest/{{{idpf}}}item[@id="ncx"]'.format(**nsmap), parseNavPoint)
}

zf   = zipfile.ZipFile(sys.argv[1])
opf  = [n for n in zf.namelist() if n.lower().endswith('.opf')][0]
pathPrefix = os.path.join('/', os.path.dirname(opf)) # path prefix

doc  = ET.fromstring(zf.read(opf))
# for k, v in output.iteritems():
#    (xpath, f) = v
#    output[k]  = f(doc.findall(xpath, namespaces=nsmap))

metadata = doc.find('./{{{idpf}}}metadata'.format(**nsmap), namespaces=nsmap)
manifest = doc.find('./{{{idpf}}}manifest'.format(**nsmap), namespaces=nsmap)
spine    = doc.find('./{{{idpf}}}spine'.format(**nsmap), namespaces=nsmap)
print "METADATA"
for child in metadata:   
    if child.text:
        print child.tag, child.text.encode('utf-8') 

print "SPINE"
for child in spine:
    x = './{{{idpf}}}manifest/*'.format(**nsmap)
    x = x + '[@id="%s"]' % (child.attrib['idref'])
    if doc.find(x, namespaces=nsmap) is not None:
        print doc.find(x, namespaces=nsmap).attrib['href']