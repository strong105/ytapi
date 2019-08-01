from django.contrib.sites import requests
from django.shortcuts import render
from ybsearch import models
from .forms import SearchForm
import json
from django.shortcuts import redirect

UTAPI = "AIzaSyBPBLE3yjMhaOz_LbHRA_WkDyyXx6GMX3"


def post_list(request):

        form = SearchForm(request.POST)

        if request.method == 'POST':
            search = form.data['search']
            # search = search['search']
            # print(search)

            payload = {'part': 'snippet',
                       'key': 'AIzaSyBPBLE3yjMhaOz_LbHRA_WkDyyXx6GMX3s',
                       'order': 'viewCount',
                       'q': search,
                       'maxResults': 50}

            resp = requests.Session().get('https://www.googleapis.com/youtube/v3/search',
                                       params=payload)

            resp_dict = json.loads(resp.content)
            # print(resp_dict)
            for item in resp_dict['items']:
                # print('['items'][0]['id']['videoId']')
                if item['id']['kind'] != 'youtube#video':
                    continue
                token = resp_dict['items'][0]['id']['videoId']
                print(token)
            return redirect('searchresult.html')
        return render(request, 'ybsearch/post_list.html', {'form': form})

def searchresult():
    pass