from django.shortcuts import render
from django.http import HttpResponse


movies = [
    {
        'movie_id': 0,
        'movie_title': 'Star Wars',
        'movie_synopsis': 'The Imperial Forces, under orders from cruel Darth Vader, hold Princess Leia hostage in '
                          '\ntheir efforts to quell the rebellion against the Galactic Empire. Luke Skywalker and '
                          '\nHan Solo, captain of the Millennium Falcon, work together with the companionable '
                          '\ndroid duo R2-D2 and C-3PO to rescue the beautiful princess, help the Rebel Alliance '
                          '\nand restore freedom and justice to the Galaxy.',
        'movie_details': 'Released: 1977, Runtime: 121 min, Gross USA: $322,740,140'
    },
    {
        'movie_id': 1,
        'movie_title': 'Monty Python and the Holy Grail',
        'movie_synopsis': "History is turned on its comic head when, in 10th century England, King Arthur travels "
                          "\nthe countryside to find knights who will join him at the Round Table in Camelot. "
                          "\nGathering up the men is a tale in itself but after a bit of a party at Camelot, "
                          "\nmany decide to leave only to be stopped by God who sends them on a quest: "
                          "\nto find the Holy Grail. After a series of individual adventures, the knights "
                          "\nare reunited but must face a wizard named Tim, killer rabbits and lessons in the use "
                          "\nof holy hand grenades. Their quest comes to an end however when the police intervene - "
                          "\njust what you would expect in a Monty Python movie.",
        'movie_details': 'Released: 1975, Runtime: 91 min, Gross USA: $1,229,197'
    },
    {
        'movie_id': 2,
        'movie_title': 'Brazil',
        'movie_synopsis': "Sam Lowry is a harried technocrat in a futuristic society that is needlessly convoluted "
                          "\nand inefficient. He dreams of a life where he can fly away from technology "
                          "\nand overpowering bureaucracy, and spend eternity with the woman of his dreams. "
                          "\nWhile trying to rectify the wrongful arrest of one Harry Buttle, "
                          "\nLowry meets the woman he is always chasing in his dreams, Jill Layton. "
                          "\nMeanwhile, the bureaucracy has fingered him responsible for a rash of terrorist bombings, "
                          "\nand both Sam and Jill's lives are put in danger.",
        'movie_details': 'Released: 1985, Runtime: 132 min, Gross USA: $9,929,135'
    }
]


# Create your views here.

def index(request):
    return HttpResponse('Hello There')


def mov(request):
    print("MOVIES!!")
    return render(request, 'movie_app/movies.html', {'movie_list': movies})


def movie_details(request, movie_id):
    return render(request, 'movie_app/movie_details.html', {'entry': movies[movie_id]})


def movie_synopsis(request, movie_id):
    return render(request, 'movie_app/movie_synopsis.html', {'entry': movies[movie_id]})
