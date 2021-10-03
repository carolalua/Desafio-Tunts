#Engenharia de Software - Desafio Carolina Aluá Soinegg

import time
import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('desafio-327916-f9b016a7ba99.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open_by_key('1yLbRHsALaqWCH3eX0q8VElFpxxPdvolM89JXACWhtrE')

worksheet = wks.get_worksheet(0)

i = 0
students = 4
max_absences = 60 * 0.25

while (i < 24):
    time.sleep(3) #quota limit
    p1 = int(worksheet.cell(students,4).value)
    p2 = int(worksheet.cell(students,5).value)
    p3 = int(worksheet.cell(students,6).value)

    m = (p1 + p2 + p3)/3

    absences = int(worksheet.cell(students,3).value)
    naf = 0

    if absences > max_absences: 
        situacao = "Reprovado por Falta"
    elif m >= 70:
        situacao = "Aprovado"
    elif m < 50:
        situacao = "Reprovado por Nota"
    else:
        #5 <= (m + naf)/2
        situacao = "Exame Final"
        naf = round((5*2) - (m/10), 1)

    worksheet.update_cell(students, 7, situacao)
    worksheet.update_cell(students, 8, naf)

    i = i + 1
    students = students + 1

    logging.basicConfig(level=logging.INFO)
    logging.info("Student number: " + str(i))