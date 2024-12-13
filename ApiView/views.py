from django.http import JsonResponse


def Home(request):
    return JsonResponse({"Data":"Hii By Django"})


def Users(request):
    return JsonResponse({"Users":[
    {"id":1, "name":"John"},
    {"id":2, "name":"Jane"},
    {"id":3, "name":"Tom"},
    {"id":4, "name":"Jerry"},
    {"id":5, "name":"Alice"},
    {"id":6, "name":"Bob"},
    {"id":7, "name":"Emily"},
    {"id":8, "name":"David"},
    {"id":9, "name":"Sophia"},
    {"id":10, "name":"Sarah"},
]})


def OneUser(request,id):
    users = [
    {"id":1, "name":"John"},
    {"id":2, "name":"Jane"},
    {"id":3, "name":"Tom"},
    {"id":4, "name":"Jerry"},
    {"id":5, "name":"Alice"},
    {"id":6, "name":"Bob"},
    {"id":7, "name":"Emily"},
    {"id":8, "name":"David"},
    {"id":9, "name":"Sophia"},
    {"id":10, "name":"Sarah"},
    ]
    u = ""
    for user in users:
        if user['id'] == id:
            u = user
            break

    if u == "":
        return JsonResponse({"error":"User not found"})
    else:
        return JsonResponse(u)