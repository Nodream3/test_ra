# noinspection PyPackageRequirements
from django.shortcuts import render
from django.http import HttpResponse

from test_auth.settings import SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET
from . import forms
import json
from requests_oauthlib import OAuth1Session
from social_django.models import UserSocialAuth
from .models import *

app_name = 'test1'


def test1(request):
    return render(request, 'test1/test1.html')


def form_name_view(request):
    form = forms.test_form1()
    if request.method == 'POST':
        form = forms.test_form1(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'test1/form_page.html', {'form': form})


def data_list(request):
    context = {
        'test_list': test_data1.objects.all(),
    }
    return render(request, 'test1/datalist.html', context)


def runAPI(request):
    APIWK.objects.all().delete()

    user = UserSocialAuth.objects.get(user_id=request.user.id)

    CK = SOCIAL_AUTH_TWITTER_KEY
    CS = SOCIAL_AUTH_TWITTER_SECRET
    AT = user.extra_data['access_token']['oauth_token']
    ATS = user.extra_data['access_token']['oauth_token_secret']
    twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

    url = "https://api.twitter.com/1.1/friends/list.json"  # エンドポイントURL貼り付け
    filename = 'aaaaa.json'

    params = {'user_id': [request.user.id], 'count': [200]}  # パラメータが必要なエンドポイントの場合、json形式でここに記載

    res = twitter.get(url, params=params)

    if res.status_code == 200:  # 正常通信出来た場合
        receivejson = json.loads(res.text)  # 受け取ったデータをjsonオブジェクトで持つ

        for x in receivejson['users']:
            WKtwitter_id = x['screen_name']
            WKuser_name = x['name']
            APIWK.objects.create(user_name=WKuser_name, twitter_id=WKtwitter_id)

    else:
        receivejson = json.loads(res.text)  # 受け取ったデータをjsonオブジェクトで持つ
        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(receivejson, outfile, indent=4, ensure_ascii=False)
            print(res.status_code)

    context = {
        'APIWK': APIWK.objects.all(),
    }
    return render(request, 'test1/friend_list.html', context)


def friend_list(request):
    context = {
        'APIWK': APIWK.objects.all(),
    }
    return render(request, 'test1/friend_list.html', context)
