from fpdf import FPDF

# Layout (P , L)
# Unity('mm', 'cm', 'in')
# format('A4')

pdf = FPDF('P', 'mm', 'A4')

# Add a page
pdf.add_page()

# specify font(Arial)
# 'B' for bold '' for regular, 'I' for italics ,'U' for under line combinations (ei 'BU')
# pdf.set_font('Arial', 'B', 16)
# Add text
pdf.image('image.png', 10, 8, 45)
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 14)

pdf.cell(1000, 25, "                                                                   title", ln=True)
pdf.cell(1000, 25, "oi",'')
pdf.output('p.pdf')
