from PIL import Image
import os

def convert_jpg_to_pdf(jpg_path, pdf_path=None, dpi=(300, 300)):
    """
    Convert a JPG image to a high-quality PDF
    
    Parameters:
    jpg_path: str, path to input JPG file
    pdf_path: str, path for output PDF file (optional)
    dpi: tuple, resolution for the output (default 300 DPI)
    """
    # If no PDF path specified, use the same name as JPG but with .pdf extension
    if pdf_path is None:
        pdf_path = os.path.splitext(jpg_path)[0] + '.pdf'
    
    # Open the image and convert to RGB mode (removes any alpha channel)
    with Image.open(jpg_path) as image:
        # Convert to RGB if not already
        if image.mode != 'RGB':
            image = image.convert('RGB')
            
        # Set the DPI information
        image.info['dpi'] = dpi
        
        # Save as PDF with high quality
        image.save(
            pdf_path,
            'PDF',
            resolution=dpi[0],
            save_all=True,
            quality=100
        )
    
    return pdf_path


#convert_jpg_to_pdf('./figs/RMF-2.jpg', './figs/RMF-2-hq.pdf')

