import pandas as pd
from reportlab.pdfgen import canvas

def GeneratePDFA4(lista):
  try:
      nome_pdf = str(lista.CODIGO)
      pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))

      if(len(lista.NOME) > 10):
        pdf.setFont("Helvetica-Bold", 40)
        pdf.drawString(40, 560, lista.NOME)
      else:
        pdf.setFont("Helvetica-Bold", 80)
        pdf.drawString(40, 560, lista.NOME)

      pdf.setTitle(nome_pdf)


      pdf.setFont("Helvetica", 30)
      pdf.drawString(45, 525, lista.MARCA.upper())
      
      pdf.setFont("Helvetica-Bold", 20)
      pdf.drawString(45, 500, lista.GRAMAGEM.upper())


      if(len(str(lista.PREÇO).split('.')[0]) < 2):
        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(90,330, 'R$')
        pdf.setFont("Helvetica-Bold", 250)
        pdf.drawString(150,240, str(lista.PREÇO).split('.')[0])
        pdf.setFont("Helvetica-Bold", 100)
        pdf.drawString(280,340, ","+str(lista.PREÇO).split('.')[1])
      else:
        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(80,330, 'R$')
        pdf.setFont("Helvetica-Bold", 250)
        pdf.drawString(120,300, str(lista.PREÇO).split('.')[0])
        pdf.setFont("Helvetica-Bold", 100)
        pdf.drawString(390,380, ","+str(lista.PREÇO).split('.')[1])

      pdf.setFont("Helvetica-Bold", 30)
      pdf.drawString(450,205, lista.TIPO.upper())

      pdf.rotate(15)
      pdf.rect(270, 130, 250, 4, fill=True)
      pdf.rect(310, 110, 185, 4, fill=True)

      pdf.save()
      print('{}.pdf criado com sucesso!'.format(nome_pdf))
  except:
      print('Erro ao gerar {}.pdf'.format(nome_pdf))

produtos = pd.read_excel('produtos.xlsx', engine='openpyxl')

for i, row in produtos.iterrows():
  GeneratePDFA4(row)

