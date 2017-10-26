from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from account.models import Profile

def profile_view(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    username = profile.user.username
    username = ''.join([i for i in username if not i.isdigit()])

    context = {
        'profile': profile,
        "username": username.replace("_", " ")
    }

    return render(request, 'home.html',context)


def createuser(request):
    response = {"status": False}

    if request.method == "POST":
        btc = request.POST.get('btc', 0)
        if not btc:
            btc = 0
        msc = request.POST.get('msc', 0)
        if not msc:
            msc = 0
        eth = request.POST.get('eth', 0)
        if not eth:
            eth = 0
        lit = request.POST.get('lit', 0)
        if not lit:
            lit = 0
        dol = request.POST.get('dol', 0)
        if not dol:
            dol = 0
        ass = request.POST.get('ass', 0)
        if not ass:
            ass = 0
        if request.POST.get("username"):
            username = request.POST.get("username")
            is_exist = User.objects.filter(username=username).exists()
            if is_exist:
                response['message'] = "Username Already Exist"
            else:
                user = User.objects.create(
                    username=username
                )
                Profile.objects.create(
                    user=user,
                    btc=int(btc),
                    msc=int(msc),
                    eth=int(eth),
                    lit=int(lit),
                    dol=int(dol),
                    ass=int(ass),
                )
                response['message'] = \
                '''User Created <br>
                    <a href='/{}/' target="_blank">Open Profile</a>
                '''.format(user.username)
                response['status'] = True
    return JsonResponse(response)
