import os
import sys

from pdf2image import convert_from_path

def main(pdf_path, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(pdf_path, 'rb') as f:
        print("converting_from_path...")
        pages = convert_from_path(pdf_path)
        for i, page in enumerate(pages):
            print("processing page:")
            print(i)
            page_path = os.path.join(output_dir, f"slide-{i+1}.png")
            page.save(page_path, "PNG")
            print("page saved")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_png.py <pdf_path> <output_dir>")
        sys.exit()
        
    pdf_path = sys.argv[1]
    print(pdf_path)
    output_dir = sys.argv[2]
    print(output_dir)
    print("Running program")
    main(pdf_path, output_dir)
