from reportlab.pdfgen import canvas

def GeneratePDF():
    try:
        nome_pdf = "teste01"
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))

        pdf.setFont("Helvetica-Bold", 70)
        pdf.drawString(100, 600, "CERVEJA")
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica", 30)
        pdf.drawString(100, 560, "SKOL")
        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(260, 560, "300ML")
        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(120, 380, "R$")
        pdf.setFont("Helvetica-Bold", 150)
        pdf.drawString(180, 360, "50")
        pdf.setFont("Helvetica-Bold", 80)
        pdf.drawString(350, 410, ",49")
        pdf.setFont("Helvetica-Bold", 30)
        pdf.drawString(470, 350, "UND")

        pdf.rotate(15)
        pdf.rect(300, 250, 250, 4, fill=True)
        pdf.rect(340, 230, 185, 4, fill=True)

        pdf.save()
        print('{}.pf criado com sucesso!'.format(nome_pdf) )
    except:
        print('erro ao gerar {}.pdf'.format(nome_pdf))

GeneratePDF()            

        
