from PyPDF2 import PdfReader, PdfWriter, PageObject
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal  # Tipo de hoja:letter o legal
from io import BytesIO
import math

def create_number_overlay(numbers, positions):
    """Crea una capa con múltiples números rotados y en color blanco."""
    packet = BytesIO()
    # Cambiar pagesize a legal
    c = canvas.Canvas(packet, pagesize=legal)
    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(1, 1, 1)  # Color blanco
    
    # Agregar cada número en sus posiciones correspondientes
    for number, (x, y) in zip(numbers, positions):
        c.saveState()
        c.translate(x, y)
        c.rotate(90)  # Rotar el texto para hacerlo vertical
        c.drawString(0, 0, str(number))
        c.restoreState()
    
    c.save()
    packet.seek(0)
    return packet

def number_tickets(input_pdf_path, output_pdf_path, start_number=11001, total_tickets=250):
    """Numera los boletos en el PDF."""
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    # Ajustar posiciones Y para tamaño oficio (legal es más alto que letter)
    positions = [
        # Boleto 1: inicio y final
        (52, 902), (570, 902),  
        
        # Boleto 2: inicio y final
        (52, 727), (570, 727),  
        
        # Boleto 3: inicio y final
        (52, 545), (570, 545),  
        
        # Boleto 4: inicio y final
        (52, 352), (570, 352),  
        
        # Boleto 5: inicio y final
        (52, 167), (570, 167),  
    ]
    
    # Calcular número total de páginas necesarias
    total_pages = math.ceil(total_tickets / 5)
    current_number = start_number
    
    # Procesar cada página
    for _ in range(total_pages):
        # Crear lista de números para esta página
        page_numbers = []
        for i in range(0, len(positions), 2):
            if current_number <= (start_number + total_tickets - 1):
                page_numbers.extend([current_number, current_number])
                current_number += 1
        
        if page_numbers:
            # Crear una copia limpia de la página plantilla usando tamaño legal
            template_page = PageObject.create_blank_page(width=legal[0], height=legal[1])
            template_page.merge_page(reader.pages[0])
            
            # Crear y aplicar el overlay con los números
            overlay = PdfReader(create_number_overlay(page_numbers, positions))
            overlay_page = overlay.pages[0]
            
            # Fusionar la plantilla con el overlay
            template_page.merge_page(overlay_page)
            
            # Agregar la página numerada al nuevo PDF
            writer.add_page(template_page)
    
    # Guardar el PDF final
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)

if __name__ == "__main__":
    number_tickets(
        input_pdf_path="bol_oficio.pdf",
        output_pdf_path="boletos_finales.pdf",
        start_number=11001,
        total_tickets=250
    )