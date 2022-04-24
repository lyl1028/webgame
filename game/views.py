from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align: center">术士之战</h1>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Falioss.gcores.com%2Fuploads%2Fimage%2F13c926bc-01c2-4c56-b532-ed2da92d1423_watermark.png&refer=http%3A%2F%2Falioss.gcores.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1653386335&t=79e8a0d937a7818da43e60405f98c7b7">'
    
    return HttpResponse(line1 + line2)


