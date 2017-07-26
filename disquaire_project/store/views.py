from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

from .models import Album, Artist, Contact, Booking



def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    context = {
        'albums': albums,
    }
    return render(request, 'store/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artists = [artist.name for artist in album.artists.all()]
    artists_name = " ".join(artists)
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id
    }
    return render(request, 'store/detail.html', context)

def listing(request):
    albums_list = Album.objects.filter(available=True)
    paginator = Paginator(albums_list, 12)

    page = request.GET.get('page')
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        albums = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        albums = paginator.page(paginator.num_pages)

    return render(request, 'store/listing.html', {'albums': albums})


def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        albums = Album.objects.filter(title__icontains=query)
    if not albums.exists():
        # Don't do this but keep it as an example.
        # artists = Artist.objects.filter(name__icontains=query)
        # ids = [artist.id for artist in artists ]
        # albums = Album.objects.filter(id__in=ids)
        albums = Album.objects.filter(artists__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'albums': albums,
        'query': title
    }
    return render(request, 'store/search.html', context)


def contact(request):
    email = request.POST.get('email')
    name = request.POST.get('name')
    album_id = request.POST.get('album_id')
    try:
        contact = Contact.objects.create(
            email=email,
            name=name
        )
        album = Album.objects.get(id=album_id)
        album.available = False
        booking = Booking.objects.create(
            contact=contact,
            created_at=timezone.now(),
            album=album
        )
        context = {
            'title': "Merci !",
            'message': "Nous vous contacterons dès que notre radio retrouvera le chemin des ondes (en résumé : très vite)."
        }
    except:
        context = {
            'title': "Mince !",
            'message': "Une erreur technique est arrivée. Ne vous en faites pas : nous sommes déjà sur le pont du navire pour investiguer. Recommencez votre requête, moussaillon !"
        }
    return render(request, 'store/thanks.html', context)
