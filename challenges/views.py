from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    'january': 'This are january Challenges',
    'february': 'This are february Challenges',
    'march': 'This are march Challenges',
    'april': 'This are april Challenges',
    'may': 'This are may Challenges',
    'june': 'This are june Challenges',
    'july': 'This are july Challenges',
    'august': 'This are august Challenges',
    'september': 'This are september Challenges',
    'october': 'This are october Challenges',
    'november': 'This are november Challenges',
    'december': None
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month-1]
        redirect_path = reverse('monthly-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
        raise Http404()


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'title': month,
            'sub_title': challenge_text
        })
    except:
        raise Http404()
        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
