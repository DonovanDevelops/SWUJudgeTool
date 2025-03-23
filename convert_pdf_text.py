# Need to `pip install PyPDF2` for this
import PyPDF2

def pdf_to_text(inputs, outputs):
    for index, file in enumerate(inputs):
        pdf_path = file
        # Open the PDF file in read-binary mode
        with open(pdf_path, 'rb') as pdf_file:
            # Create a PdfReader object instead of PdfFileReader
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Initialize an empty string to store the text
            text = ''

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

        # Write the extracted text to a text file
        with open(outputs[index], 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

if __name__ == "__main__":
    doc_names = ['rule_text/cr.txt', 'rule_text/med.txt', 'rule_text/tr.txt']
    doc_array = [
        'rules_documents/SWH_Comp_Rules_4_0_1994d2beb6.pdf',
        'rules_documents/Fantasy_Flight_Games_Master_Event_Document_v_1_2_716cb2ef0e.pdf',
        'rules_documents/SWU_Tournament_Regulations_v1_3_ca8a772c2f.pdf'
    ]

    pdf_to_text(doc_array, doc_names)

    print("PDFs converted to text successfully!")