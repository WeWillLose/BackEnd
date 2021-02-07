import io
import zipfile

from django.http import HttpResponse, FileResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from typing import List

from .serializers import FileSerializer


# for f in request.FILES:
#     with open(f, "wb") as file:
#         data = request.FILES.get(f)
#         for i in data:
#             file.write(i)

def zip_files(files):
    outfile = io.BytesIO()  # io.BytesIO() for python 3
    with zipfile.ZipFile(outfile, 'w') as zf:
        for n, f in enumerate(files):
            tmp = files.get(f).file
            print(type(tmp))
            print(dir(tmp))
            zf.writestr("{}.docx".format(n), tmp.getvalue())
    return outfile.getvalue()


class MovieListView(APIView):
    """Вывод файла"""

    def post(self, request):
        print(request.FILES)
        print("------------")
        for ind,f in enumerate(request.FILES):
            with open(f, "wb") as file:
                data = request.FILES.get(f)
                for i in data:
                    file.write(i)
        zipped_file = zip_files(request.FILES)
        response = HttpResponse(zipped_file, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename=my_file.zip'
        return response



