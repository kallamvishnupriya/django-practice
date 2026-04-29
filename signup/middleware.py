class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        #before view
        print("Request came:", request.path)
        #view
        response = self.get_response(request)
        #after view
        print("Response sent")
        return response