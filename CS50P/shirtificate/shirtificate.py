from fpdf import FPDF

nome = input("Name: ")

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 30)
        #faz o titulo no meio
        self.cell(0, 10, "CS50 Shirtificate", align="C")

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


pdf = PDF()
pdf.add_page()
#camisa
pdf.image("shirtificate.png", x="C",y=70,w=150,h=150)
#texto da camisa
pdf.set_y(120)
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(r=255,b=255,g=255)
pdf.cell(0, 10, f"{nome} took CS50", align="C")
#outputs
pdf.output("shirtificate.pdf")
