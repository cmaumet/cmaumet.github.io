import urllib2
import re

# Read publication list from hal
response = urllib2.urlopen('http://haltools.inria.fr/Public/afficheRequete\
Publi.php?auteur_exp=camille,maumet&CB_ref_biblio=oui&langue=Anglais&tri_exp=\
annee_publi&tri_exp2=typdoc&tri_exp3=date_publi&ordre_aff=TA&Fen=Aff')
html = response.read()

with open('include/publications_head.html', 'r') as f:
    head = f.read()
with open('include/publications_bottom.html', 'r') as f:
    bottom = f.read()

found = re.search(r'<body>(.*)</body>', html, re.DOTALL)
publis = found.group(0).replace("<body>", "").replace("</body>", "")

publis = publis.replace("Krzysztof Gorgolewski, Gael Varoquaux, Gabriel Rivera\
, Yannick Schwarz, Satrajit Ghosh, et al.", "Krzysztof Gorgolewski, Gael \
Varoquaux, Gabriel Rivera, Yannick Schwartz, Satrajit Ghosh, Camille Maumet, \
et al.")
publis = publis.replace("Krzysztof Gorgolewski, Gael Varoquaux, Gabriel Rivera\
, Yannick Schwartz, Vanessa Sochat, et al.", "Krzysztof Gorgolewski, Gael \
Varoquaux, Gabriel Rivera, Yannick Schwartz, Vanessa Sochat, Satrajit Ghosh\
, Camille Maumet, et al.")
publis = publis.replace("Krzysztof Gorgolewski, Tal Yarkoni, Satrajit Ghosh, \
Russel Poldrack, Jean-Baptiste Poline, et al.", "Krzysztof Gorgolewski, \
Tal Yarkoni, Satrajit Ghosh, Russel Poldrack, Jean-Baptiste Poline, Yannick \
Schwartz, Thomas Nichols, Camille Maumet, Daniel Margulies")
publis = publis.replace("Camille Maumet", "<u>Camille Maumet</u>")
publis = unicode(publis, "utf-8")

with open('../publications.html', 'w') as f:
    f.write((head+publis+bottom).encode('ascii', 'xmlcharrefreplace'))