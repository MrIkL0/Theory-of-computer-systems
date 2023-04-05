import docx

lab_doc = docx.Document("Lab_text.docx")

all_paragraphs = lab_doc.paragraphs

for paragraph in all_paragraphs:
    print(paragraph.text)