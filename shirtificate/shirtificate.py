from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 20)
        self.cell(0, 10, 'CS50 Shirtificate', align='C')

    def shirt(self, name):
        # Center the shirt image horizontally
        shirt_image = 'shirtificate.png'
        image_width = 100  # Adjust the width as needed
        x_position = (self.w - image_width) / 2
        self.image(shirt_image, x_position, 40, image_width)

        # Set font and color for the name
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(255, 255, 255)  # Black color for the text

        # Center the name on top of the shirt without adding extra space
        self.set_xy(x_position, 40)
        self.multi_cell(image_width, 60, name, 0, 'C')

def main():
    # Get user's name
    name = input("Enter your name: ")
    user_name = name + " " + "took CS50"

    # Create PDF instance
    pdf = Shirtificate(orientation="P", format="A4")
    pdf.add_page()

    # Generate shirtificate with the user's name
    pdf.shirt(user_name)

    # Output to a file
    pdf_output = 'shirtificate.pdf'
    pdf.output(pdf_output)
    print(f"Shirtificate generated successfully: {pdf_output}")

if __name__ == "__main__":
    main()
