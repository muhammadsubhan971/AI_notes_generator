
from fpdf import FPDF
import re


def pdf1(text):
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', '', 10)
    pdf.set_auto_page_break(auto=True, margin=10)
    
    bold_pattern = re.compile(r'\*\*(.*?)\*\*|__(.*?)__')
    underline_pattern = re.compile(r'_(.*?)_|~~(.*?)~~')
    bullet_pattern = re.compile(r'\*(.*)', re.MULTILINE)
    h1_pattern = re.compile(r'^#\s+(.+)', re.MULTILINE)
    h2_pattern = re.compile(r'^##\s+(.+)', re.MULTILINE)
    
    segments = re.split(r'(\*\*.*?\*\*|__.*?__|_.*?_|~~.*?~~|-\s.*)', text)
    
    for segment in segments:
        if bold_pattern.match(segment):
            pdf.set_font('Arial', 'B', 12)
            clean_text = re.sub(r'\*\*|__', '', segment)
        elif underline_pattern.match(segment):
            pdf.set_font('Arial', '', 10)
            pdf.set_text_color(0, 0, 255)  
            clean_text = re.sub(r'_+|~+', '', segment)
        elif h1_pattern.match(segment):
            pdf.set_font('Arial', 'B', 16)
            clean_text = re.sub(r'^#\s+', '', segment)
        elif h2_pattern.match(segment):
            pdf.set_font('Arial', 'B', 14)
            clean_text = re.sub(r'^##\s+', '', segment)
        elif bullet_pattern.match(segment):
            pdf.set_font('Arial', '', 10)
            pdf.cell(5, 5, "•", ln=0)  
            clean_text = re.sub(r'\*', '', segment)
        else:
            pdf.set_font('Arial', '', 10)
            pdf.set_text_color(0, 0, 0)
            clean_text = segment
        
        pdf.multi_cell(0, 5, clean_text.encode('latin-1', 'ignore').decode('latin-1'))
    
    pdf.output("notes.pdf")

