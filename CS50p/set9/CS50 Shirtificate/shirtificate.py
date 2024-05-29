from fpdf import FPDF

class Shirtificate:
    def __init__(self, name):
        self.name = name
        self.func2()

    @classmethod
    # get
    def func1(cls):
        name = input("Name: ")
        name = name.strip()
        name = cls(name)
        return(name)
    # generate
    def func2(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)
        pdf.set_font("Helvetica", "B", 50)
        pdf.cell(0, 50, txt="CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", x=5, y=80, w=200)
        pdf.set_font("Helvetica", "B", size=30)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(-189, 250, align="C", txt=f"{self.name} took CS50")
        pdf.output("shirtificate.pdf")

def main():
    Shirtificate.func1()

if __name__ == "__main__":
    main()
