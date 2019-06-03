from  django.http import  HttpResponse

def home(request):
    response=HttpResponse(content_type='text/html')
    response.write("testing")
    response.write("testing")
    response.write("testing")
    response.write("testing")
    response.content = "Aditya"
    response.status_code=200
    return response

# def home(request):
#     # print(request)
#     # print(dir(request))
#     # print(request.method)
#     # print(request.is_ajax())
#     # print(request.is_ajax)
#     print(request.get_full_path())
#     return HttpResponse("<h1>Hello Worlds</h1>")