from django.http import HttpResponse
from django.shortcuts import render
from tapsearch.document_indexer import Indexer
import json
from image_search.index_and_search import ImageSearch
import io
from PIL import Image
import os
import numpy as np
from tapsearch.settings import BASE_DIR
import cv2
from tapsearch.pypdf2_test import read_pdf



# initialization step, initializing the global index object
indexer = Indexer()
# initializing the global feature extractor class
IS = ImageSearch()






def index_document(request):
    if request.method == "POST":
        document = request.POST.get('document',"")
        indexer.index_doc(document)
        request.url = ""
        return render(request, "search_page.html")
    else:
        request.url=""
        return render(request, "search_page.html")


def get_main_page(request):
    if len(indexer.index) > 1:
        return render(request, "search_page.html")
    else:
        return render(request, "index_docs.html")
    
    
def get_index_page(request):
        return render(request, "index_docs.html")



def search(request):
    print(request.method)
    if request.method == "POST" :
        query = request.POST.get("query","")
        print(query)
        status, results = indexer.search(query)
        print(results)
        final = {"status":status, "results":results}
        response = HttpResponse(json.dumps(final))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, access-control-allow-origin"
        return response
    else:
        print("No QUERY")
        response = HttpResponse("")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, access-control-allow-origin"
        return response


def clear_index(request):
    print(request.method)
    if request.method == "GET":
        indexer.clear_index()
        response = HttpResponse("")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, access-control-allow-origin"
        return response



def image_search_page(request):
    if request.method == "GET":
        return render(request, "image_search_results.html")



def image_search(request):
    if request.method == "POST" :
        file = request.FILES["image"]
        filename = file.name
        image = file.read()
        image = Image.open(io.BytesIO(image))
        
        image.save("static/filename.png")
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        results = IS.search_image(image=image)
        print(results)
        response = HttpResponse(json.dumps(results))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, access-control-allow-origin"
        return response
    else:
        print("No QUERY")
        response = HttpResponse("")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, access-control-allow-origin"
        return response
    
    
    
def index_images(request):
    if request.method == "POST" :
        files = request.FILES.getlist("images_to_index")
        for file in files:
            print(file.name)
            image = file.read()
            image = Image.open(io.BytesIO(image))
            image.save(os.path.join(BASE_DIR, 'staticfiles',file.name))
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            IS.index_image(imagename=file.name, image=image)
        
        response = HttpResponse(json.dumps("success"))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, access-control-allow-origin"
        return response
    else:
        print("No QUERY")
        response = HttpResponse("")
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type, access-control-allow-origin"
        return response


def upload_pdf(request):
    file = request.FILES
    print("THE FILE HAS BEEN RECEIVED.")
    try:
        stream = io.BytesIO(file["pdf"].read())
        text = read_pdf(stream)
        # now index the text so obtained
        indexer.index_doc(text)
    except:
        print("")
    print("Indexing done.")
    return render(request, "search_page.html") 
        





