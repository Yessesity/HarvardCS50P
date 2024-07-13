from fpdf import FPDF
from fpdf import Align


def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("D:\My Codes\Practice\CS50P\Week 8\psets\shirtificate\shirtificate.png", Align.C, y=75, h=180)
    pdf.set_font("helvetica", "B", 50)
    pdf.cell(
        0,
        80,
        "CS50 Shirtificate",
        new_x="LMARGIN",
        new_y="NEXT",
        align='C'
        )
    pdf.add_font(family="ComicRelief", fname="D:\Downloads\comic-relief\ComicRelief.ttf")
    pdf.set_font("ComicRelief", "", 30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(
        0,
        90,
        f"{name} took CS50",
        new_x="LMARGIN",
        new_y="NEXT",
        align='C'
        )
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
