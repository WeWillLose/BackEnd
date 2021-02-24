import numpy as np
from django.http import HttpResponse, HttpResponseBadRequest
from docx import Document
from docx.shared import Inches
from rest_framework.views import APIView

from docxApp.common.utils import *


def write_list(data=None):
    otchet = Document()
    tables = Document("template.docx")
    if data is None:
        data = read_docx_tables("data.docx")
    balls = []
    count = 0

    balls.append(data[2]["Баллы"].sum())
    balls.append(data[3]["Баллы"].sum())
    balls.append(data[4]["Баллы"].sum())
    balls.append(data[4]["Баллы"][0])
    balls.append(data[4]["Баллы"][1])
    balls.append(balls[0]+balls[1]+balls[2])
    #balls.append(1 if list(balls[5]) == 2 else 0) # is present 3.1
    balls.append(data[6]["Баллы"].sum()) # 3.2.1
    balls.append(data[7]["Баллы"].sum())
    balls.append(data[8]["Баллы"].sum()) #3.2.3
    print(balls[-1])
    balls.append(data[9]["Баллы"].sum()) #3.3
    balls.append(data[10]["Баллы"].sum()) #3.4
    balls.append(data[11]["Баллы"].sum()) #3.5
    balls.append(data[12]["Баллы"].sum()) #3.6
    balls.insert(6, np.array(3333))  # sum 3
    balls.append(np.array(3333))  # sum 4
    balls.append(data[13]["Баллы"].sum())  # 4.1
    balls.append(data[14]["Баллы"].sum())  # 4.2
    balls.append(data[15]["Баллы"].sum())  # 4.3
    balls.append(data[16]["Баллы"].sum())  # 4.4
    balls.append(np.array(3333))  # sum 5
    #balls.append()  # 5.1 is present
    balls.append(data[18]["Баллы"].sum())  # 5.2
    balls.append(data[19]["Баллы"].sum())  # 5.3
    balls.append(data[20]["Баллы"].sum())  # 5.4
    balls.append(np.array(3333))  # sum 6
    balls.append(np.array(3333))  # sum 6.1
    balls.append(data[21]["Баллы"].sum())  # 6.1.1
    balls.append(data[22]["Баллы"].sum())  # 6.1.2
    balls.append(data[23]["Баллы"].sum())  # 6.1.3
    balls.append(data[24]["Баллы"].sum())  # 6.1.4
    balls.append(data[25]["Баллы"].sum())  # 6.2
    balls.append(data[26]["Баллы"].sum())  # 7
    balls.append(data[27]["Баллы"].sum())  # 8
    balls.append(np.array(3333))  # sum 9
    balls.append(data[28]["Баллы"][0])  # 9.1
    balls.append(data[28]["Баллы"][1])  # 9.2
    balls.append(data[28]["Баллы"][2])  # 9.3
    balls.append(data[28]["Баллы"][3])  # 9.4
    balls.append(data[28]["Баллы"][4])  # 9.5
    balls.append(data[29]["Баллы"].sum())  # 10
    balls.append(data[30]["Баллы"].sum())  # 11
    balls.append(np.array(3333))  # sum all


def write(name, data):
    with open(name, "wb") as file:
        for i in data:
            file.write(i)

class Template(APIView):

    def get(self, request):
        return HttpResponse(open('template.html', 'r'))

class MovieListView(APIView):
    """Вывод файла"""

    def post(self, request):
        r = request
        for f in request.FILES:
            # file name content_type
            try:
                pars_doc(request.FILES.get(f))
            except ValueError as ve:
                print(ve)
                return HttpResponseBadRequest(ve)

        zipped_file = zip_files(request.FILES)
        response = HttpResponse(zipped_file, content_type='application/octet-stream')
        return response
