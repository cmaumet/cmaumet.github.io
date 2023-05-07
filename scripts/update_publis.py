from urllib.request import urlopen
import re
import os

script_path = os.path.dirname(os.path.abspath(__file__))

# Read publication list from hal
hal_url = 'http://haltools.archives-ouvertes.fr/Public/afficheRequetePubli.php?auteur_exp=camille,maumet&CB_auteur=oui&CB_titre=oui&CB_article=oui&langue=Anglais&tri_exp=annee_publi&tri_exp2=typdoc&tri_exp3=date_publi&ordre_aff=TA&Fen=Aff&typdoc=(%27ART%27,%27COMM%27,%27OUV%27,%27COUV%27,%27DOUV%27,%27PATENT%27,%27OTHER%27,%27UNDEFINED%27,%27REPORT%27,%27THESE%27,%27HDR%27,%27MEM%27,%27IMG%27,%27VIDEO%27,%27SON%27,%27MAP%27,%27MINUTES%27,%27NOTE%27,%27OTHERREPORT%27,%27SYNTHESE%27)&CB_DOI=oui&invitedCommunication=Non&popularLevel=Non'
# Read talk list from hal
talk_url = 'https://haltools.archives-ouvertes.fr/Public/afficheRequetePubli.php?auteur_exp=camille,maumet&CB_titre=oui&CB_article=oui&langue=Anglais&tri_exp=annee_publi&tri_exp2=typdoc&tri_exp3=date_publi&ordre_aff=TA&Fen=Aff&typdoc=(%27PRESCONF%27)&CB_vignette=oui'

# Publication page
response = urlopen(hal_url)
html = response.read().decode("utf-8") 

with open(os.path.join(script_path, 'include/publications_head.html'), 'r') as f:
    head = f.read()
with open(os.path.join(script_path, 'include/publications_foot.html'), 'r') as f:
    bottom = f.read()

found = re.search(r'<body>(.*)</body>', html, re.DOTALL)
publis = found.group(0).replace("<body>", "").replace("</body>", "")

replacements = (
    ("Camille Maumet", "<b>Camille Maumet</b>"),
)

for to_rep, rep in replacements:
    publis = publis.replace(to_rep, rep)

with open(os.path.join(script_path, '..', 'publications.html'), 'wb') as f:
    f.write((head+publis+bottom).encode('ascii', 'xmlcharrefreplace'))

# Talk page
response = urlopen(talk_url)
html = response.read().decode("utf-8") 

with open(os.path.join(script_path, 'include/talks_head.html'), 'r') as f:
    head = f.read()
with open(os.path.join(script_path, 'include/publications_foot.html'), 'r') as f:
    bottom = f.read()

found = re.search(r'<body>(.*)</body>', html, re.DOTALL)
talks = found.group(0).replace("<body>", "").replace("</body>", "")

# todel = """<p class="SousRubrique">Documents associated with scientific events</p>"""

todel = "Documents associated with scientific events"
talks = talks.replace(todel, "")

# Bigger thumbnails
talks = talks.replace("little", "medium")
talks = talks.replace("class=\"VignetteImg\"", "class=\"VignetteImg\" height=\"150\"")
# talks = talks.replace("border=\"0\"", "border=\"1\"")


with open(os.path.join(script_path, '..', 'talks.html'), 'wb') as f:
    f.write((head+talks+bottom).encode('ascii', 'xmlcharrefreplace'))


# Two last publications
response = urlopen('https://haltools.archives-ouvertes.fr/Public/afficheRequetePubli.php?auteur_exp=camille,maumet&NbAffiche=2&CB_ref_biblio=oui&langue=Anglais&tri_exp=date_publi&ordre_aff=TA&Fen=Aff&invitedCommunication=Non&popularLevel=Non&typdoc=(%27ART%27,%27COMM%27,%27OUV%27,%27COUV%27,%27DOUV%27,%27PATENT%27,%27OTHER%27,%27UNDEFINED%27,%27REPORT%27,%27THESE%27,%27HDR%27,%27MEM%27,%27IMG%27,%27VIDEO%27,%27SON%27,%27MAP%27,%27MINUTES%27,%27NOTE%27,%27OTHERREPORT%27,%27SYNTHESE%27)')
res_talks = urlopen('https://haltools.archives-ouvertes.fr/Public/afficheRequetePubli.php?auteur_exp=camille,maumet&NbAffiche=2&CB_titre=oui&CB_article=oui&langue=Anglais&tri_exp=date_publi&ordre_aff=TA&Fen=Aff&invitedCommunication=Non&popularLevel=Non&typdoc=(%27PRESCONF%27)&CB_vignette=oui')

html_publi = response.read().decode("utf-8") 
html_talk = res_talks.read().decode("utf-8") 
with open(os.path.join(script_path, 'include/index_head.html'), 'r') as f:
    head = f.read()
with open(os.path.join(script_path, 'include/index_title_talk.html'), 'r') as f:
    title_talk = f.read()
with open(os.path.join(script_path, 'include/index_foot.html'), 'r') as f:
    bottom = f.read()
found_publi = re.search(r'<body>(.*)</body>', html_publi, re.DOTALL)
found_talk =  re.search(r'<body>(.*)</body>', html_talk, re.DOTALL)

publis = found_publi.group(0).replace("<body>", "").replace("</body>", "")
talks = found_talk.group(0).replace("<body>", "").replace("</body>", "")

replacements = (
    ("Camille Maumet", "<b>Camille Maumet</b>"),
)

# replacements = (
#     ("Krzysztof Gorgolewski, Gael Varoquaux, Gabriel Rivera\
# , Yannick Schwarz, Satrajit Ghosh, et al.", "Krzysztof Gorgolewski, Gael \
# Varoquaux, Gabriel Rivera, Yannick Schwartz, Satrajit Ghosh, Camille Maumet, \
# Vanessa Sochat, Thomas Nichols, Russell Poldrack, Jean-Baptiste Poline, Tal \
# Yarkoni, Daniel Margulies"),
#     ("Krzysztof Gorgolewski, Gael Varoquaux, Gabriel Rivera\
# , Yannick Schwartz, Vanessa Sochat, et al.", "Krzysztof Gorgolewski, Gael \
# Varoquaux, Gabriel Rivera, Yannick Schwartz, Vanessa Sochat, Satrajit Ghosh\
# , Camille Maumet, Thomas Nichols, Jean-Baptiste Poline, Tal Yarkoni, Daniel \
# Margulies, Russell Poldrack"),
#     ("Krzysztof Gorgolewski, Tal Yarkoni, Satrajit Ghosh, \
# Russel Poldrack, Jean-Baptiste Poline, et al.", "Krzysztof Gorgolewski, \
# Tal Yarkoni, Satrajit Ghosh, Russel Poldrack, Jean-Baptiste Poline, Yannick \
# Schwartz, Thomas Nichols, Camille Maumet, Daniel Margulies"),
#     ("Ruth Pauli, Alexander Bowring, Richard Reynolds, Gang\
#  Chen, Thomas Nichols, et al.", "Ruth Pauli, Alexander Bowring, Richard \
# Reynolds, Gang Chen, Thomas Nichols, Camille Maumet"),
#     ("Krzysztof Gorgolewski, Tibor Auer, Vince Calhoun,\
#  Cameron Craddock, Samir Das, et al.", "Krzysztof Gorgolewski, Tibor Auer, \
# Vince Calhoun,\
#  Cameron Craddock, Samir Das, Eugene Duff, Guillaume Flandin, Satrajit Ghosh,\
#  Tristan Glatard, Yaroslav Halchenko, Daniel Handwerker, Michael Hanke,\
#  David Keator, Xiangrui Li, Zachary Michael, Camille Maumet, Nolan Nichols, \
#  Thomas Nichols, John Pellman, Jean-Baptiste Poline, Ariel Rokem,\
#  Gunnar Schaefer, Vanessa Sochat, William Triplett, Jessica Turner,\
#  Gael Varoquaux, Russell Poldrack"),
#     ("Ruth Pauli, Alexander Bowring, Richard Reynolds, \
# Gang Chen, Thomas E. Nichols, et al.", "Ruth Pauli, Alexander Bowring, Richard\
#  Reynolds, Gang Chen, Thomas E. Nichols, Camille Maumet"),
#     ("Camille Maumet, Tibor Auer, Alexander Bowring, Gang \
# Chen, Samir Das, et al.", "Camille Maumet, Tibor Auer, Alexander Bowring, Gang\
#  Chen, Samir Das, Guillaume Flandin, Satrajit Ghosh, Tristan Glatard, \
# Krzysztof J. Gorgolewski, Karl G. Helmer, Mark Jenkinson, David B. Keator, B. \
# Nolan Nichols, Jean-Baptiste Poline, Richard Reynolds, Vanessa Sochat, \
# Jessica Turner, Thomas E. Nichols"),
#     ("Frontiers in Aging Neuroscience", "Frontiers in Neuroscience"),
#     ("Patricia Clement, Thomas Booth, Fran Borovečki, Kyrre Emblem, Patrícia Figueiredo, et al.", 
#         "Patricia Clement, Thomas Booth, Fran Borovečki, Kyrre Emblem, Patrícia Figueiredo, \
# Lydiane Hirschler, Radim Jančálek, Vera C. Keil, Camille Maumet, et al."),
#     ("Camille Maumet", "<b>Camille Maumet</b>")
# )


for to_rep, rep in replacements:
    publis = publis.replace(to_rep, rep)

with open(os.path.join(script_path, '../index.html'), 'wb') as f:
    f.write((head+publis+title_talk+talks+bottom).encode('ascii', 'xmlcharrefreplace'))
