import urllib2
import re

# Read publication list from hal
hal_url = 'http://haltools.archives-ouvertes.fr/Public/afficheRequetePubli.php?auteur_exp=camille,maumet&CB_ref_biblio=oui&langue=Anglais&tri_exp=annee_publi&tri_exp2=typdoc&tri_exp3=date_publi&ordre_aff=TA&Fen=Aff&typdoc=(%27ART%27,%27COMM%27,%27PRESCONF%27,%27OUV%27,%27COUV%27,%27DOUV%27,%27PATENT%27,%27OTHER%27,%27UNDEFINED%27,%27REPORT%27,%27THESE%27,%27HDR%27,%27MEM%27,%27LECTURE%27,%27IMG%27,%27VIDEO%27,%27SON%27,%27MAP%27,%27MINUTES%27,%27NOTE%27,%27OTHERREPORT%27,%27SYNTHESE%27)&CB_DOI=oui'
response = urllib2.urlopen(hal_url)
html = response.read()

with open('include/publications_head.html', 'r') as f:
    head = f.read()
with open('include/publications_foot.html', 'r') as f:
    bottom = f.read()

found = re.search(r'<body>(.*)</body>', html, re.DOTALL)
publis = found.group(0).replace("<body>", "").replace("</body>", "")

replacements = (
    ("Krzysztof Gorgolewski, Gael Varoquaux, Gabriel Rivera\
, Yannick Schwarz, Satrajit Ghosh, et al.", "Krzysztof Gorgolewski, Gael \
Varoquaux, Gabriel Rivera, Yannick Schwartz, Satrajit Ghosh, Camille Maumet, \
Vanessa Sochat, Thomas Nichols, Russell Poldrack, Jean-Baptiste Poline, Tal \
Yarkoni, Daniel Margulies"),
    ("Krzysztof Gorgolewski, Gael Varoquaux, Gabriel Rivera\
, Yannick Schwartz, Vanessa Sochat, et al.", "Krzysztof Gorgolewski, Gael \
Varoquaux, Gabriel Rivera, Yannick Schwartz, Vanessa Sochat, Satrajit Ghosh\
, Camille Maumet, Thomas Nichols, Jean-Baptiste Poline, Tal Yarkoni, Daniel \
Margulies, Russell Poldrack"),
    ("Krzysztof Gorgolewski, Tal Yarkoni, Satrajit Ghosh, \
Russel Poldrack, Jean-Baptiste Poline, et al.", "Krzysztof Gorgolewski, \
Tal Yarkoni, Satrajit Ghosh, Russel Poldrack, Jean-Baptiste Poline, Yannick \
Schwartz, Thomas Nichols, Camille Maumet, Daniel Margulies"),
    ("Ruth Pauli, Alexander Bowring, Richard Reynolds, Gang\
 Chen, Thomas Nichols, et al.", "Ruth Pauli, Alexander Bowring, Richard \
Reynolds, Gang Chen, Thomas Nichols, Camille Maumet"),
    ("Krzysztof Gorgolewski, Tibor Auer, Vince Calhoun,\
 Cameron Craddock, Samir Das, et al.", "Krzysztof Gorgolewski, Tibor Auer, \
Vince Calhoun,\
 Cameron Craddock, Samir Das, Eugene Duff, Guillaume Flandin, Satrajit Ghosh,\
 Tristan Glatard, Yaroslav Halchenko, Daniel Handwerker, Michael Hanke,\
 David Keator, Xiangrui Li, Zachary Michael, Camille Maumet, Nolan Nichols, \
 Thomas Nichols, John Pellman, Jean-Baptiste Poline, Ariel Rokem,\
 Gunnar Schaefer, Vanessa Sochat, William Triplett, Jessica Turner,\
 Gael Varoquaux, Russell Poldrack"),
    ("Ruth Pauli, Alexander Bowring, Richard Reynolds, \
Gang Chen, Thomas E. Nichols, et al.", "Ruth Pauli, Alexander Bowring, Richard\
 Reynolds, Gang Chen, Thomas E. Nichols, Camille Maumet"),
    ("Camille Maumet, Tibor Auer, Alexander Bowring, Gang \
Chen, Samir Das, et al.", "Camille Maumet, Tibor Auer, Alexander Bowring, Gang\
 Chen, Samir Das, Guillaume Flandin, Satrajit Ghosh, Tristan Glatard, \
Krzysztof J. Gorgolewski, Karl G. Helmer, Mark Jenkinson, David B. Keator, B. \
Nolan Nichols, Jean-Baptiste Poline, Richard Reynolds, Vanessa Sochat, \
Jessica Turner, Thomas E. Nichols"),
    ("Frontiers in Aging Neuroscience", "Frontiers in Neuroscience"),
    ("Camille Maumet", "<b>Camille Maumet</b>")
)

for to_rep, rep in replacements:
    publis = publis.replace(to_rep, rep)

publis = unicode(publis, "utf-8")

with open('../publications.html', 'w') as f:
    f.write((head+publis+bottom).encode('ascii', 'xmlcharrefreplace'))

# Two last publications
response = urllib2.urlopen('http://haltools.archives-ouvertes.fr/Public/affich\
eRequetePubli.php?auteur_exp=camille,maumet&NbAffiche=2&CB_ref_biblio=oui&lang\
ue=Anglais&tri_exp=annee_publi&tri_exp2=date_publi&ordre_aff=TA&Fen=Aff')

html = response.read()
with open('include/index_head.html', 'r') as f:
    head = f.read()
with open('include/index_foot.html', 'r') as f:
    bottom = f.read()
found = re.search(r'<body>(.*)</body>', html, re.DOTALL)
publis = found.group(0).replace("<body>", "").replace("</body>", "")

for to_rep, rep in replacements:
    publis = publis.replace(to_rep, rep)

publis = unicode(publis, "utf-8")

with open('../index.html', 'w') as f:
    f.write((head+publis+bottom).encode('ascii', 'xmlcharrefreplace'))
