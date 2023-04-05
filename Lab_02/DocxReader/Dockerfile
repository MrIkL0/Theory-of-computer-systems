FROM python:3

COPY DocxReader.py /
COPY Lab_text.docx /

RUN pip install flask python-docx

CMD ["python", "./DocxReader.py" ]