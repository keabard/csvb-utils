from PyPDF2 import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

PDF_INPUTS = {
    'checkbox': {
        'type_de_licence': {
            'competition_salle': {'x': 17, 'y': 723, 'font': ('Helvetica-Bold', 14)},
            'competition_beach': {'x': 17, 'y': 712, 'font': ('Helvetica-Bold', 14)},
            'encadrement': {'x': 17, 'y': 701, 'font': ('Helvetica-Bold', 14)},
            'dirigeant': {'x': 17, 'y': 691, 'font': ('Helvetica-Bold', 14)},
            'competition_lib': {'x': 17, 'y': 680, 'font': ('Helvetica-Bold', 14)},
            'volley_pour_tous': {'x': 17, 'y': 669, 'font': ('Helvetica-Bold', 14)}
        },
        'type_de_demande': {
          'creation': {'x': 17, 'y': 620, 'font': ('Helvetica-Bold', 14)},
          'renouvellement': {'x': 17, 'y': 610, 'font': ('Helvetica-Bold', 14)},
          'mutation_nationale': {'x': 17, 'y': 599, 'font': ('Helvetica-Bold', 14)},
          'mutation_regionale': {'x': 17, 'y': 588, 'font': ('Helvetica-Bold', 14)}
        },
        'sexe': {
            'feminin': {'x': 432, 'y': 642, 'font': ('Helvetica-Bold', 14)},
            'masculin': {'x': 468, 'y': 642, 'font': ('Helvetica-Bold', 14)}
        },
        'nationalite': {
            'francaise': {'x': 217, 'y': 577, 'font': ('Helvetica-Bold', 14)},
            'afr': {'x': 270, 'y': 577, 'font': ('Helvetica-Bold', 14)},
            'etrangere': {'x': 375, 'y': 577, 'font': ('Helvetica-Bold', 14)},
            'etr_fivb': {'x': 485, 'y': 577, 'font': ('Helvetica-Bold', 14)},
            'etr_fivb-etr': {'x': 190, 'y': 567, 'font': ('Helvetica-Bold', 14)},
            'etr_fivb-ue': {'x': 338, 'y': 567, 'font': ('Helvetica-Bold', 14)}
        },
        'certificat_medical': {
            'salle': {'x': 17, 'y': 389, 'font': ('Helvetica-Bold', 14)},
            'beach': {'x': 17, 'y': 377, 'font': ('Helvetica-Bold', 14)}
        },
        'assurances': {
            'connaissance': {'x': 17, 'y': 251, 'font': ('Helvetica-Bold', 14)},
            'contrat_collectif': {'x': 17, 'y': 240, 'font': ('Helvetica-Bold', 14)},
            'option_complementaire': {'x': 17, 'y': 229, 'font': ('Helvetica-Bold', 14)},
            'pas_de_contrat': {'x': 17, 'y': 208, 'font': ('Helvetica-Bold', 14)}
        },
        'options': {
            'autre_gsa_saison_prec': {'x': 17, 'y': 157, 'font': ('Helvetica-Bold', 14)},
            'autre_gsa_saison_cour': {'x': 17, 'y': 147, 'font': ('Helvetica-Bold', 14)},
            'infos_courrier': {'x': 17, 'y': 137, 'font': ('Helvetica-Bold', 14)},
            'coords_partenaires': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)}
        }
    },
    'text': {
        'coordonnees': {
            'numero_licence': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'nom': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'prenom': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'taille': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'date_naissance': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'adresse': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'code_postal': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'ville': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'telephone': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'portable': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)},
            'email': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)}
        },
        'certificat_medical': {
            'monsieur_madame': {'x': 17, 'y': 127, 'font': ('Helvetica-Bold', 14)}
        }
    }
}

# Step 1
input1 = PdfFileReader(open("Formulaire_demande_licences_2016_2017.pdf", "rb"))

# Step 2
packet = StringIO.StringIO()
can = canvas.Canvas(packet, pagesize=letter)
can.setFont('Helvetica-Bold', 14)
can.drawString(17, 127, 'X')
can.save()
packet.seek(0)
input2 = PdfFileReader(packet)

# Step 3
page = input1.getPage(0)
page.mergePage(input2.getPage(0))
output = PdfFileWriter()
output.addPage(page)

# Step 4
outputStream = file("sortie.pdf", "wb")
output.write(outputStream)


# read your PDF using PdfFileReader(), we'll call this input
# create a new pdf containing your text to add using ReportLab, save this as a string object
# read the string object using PdfFileReader(), we'll call this text
# create a new PDF object using PdfFileWriter(), we'll call this output
# iterate through input and apply .mergePage(text.getPage(0)) for each page you want the text added to, then use output.addPage() to add the modified pages to a new document