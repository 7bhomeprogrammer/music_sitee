from django.shortcuts import render, get_object_or_404
from .models import Song, Artist, Album, Playlist

def home(request):
    return render(request, 'music/home.html')

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {'songs': songs})

def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, 'music/song_detail.html', {'song': song})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'music/artist_list.html', {'artists': artists})

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    return render(request, 'music/artist_detail.html', {'artist': artist})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {'albums': albums})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/album_detail.html', {'album': album})

def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'music/playlist_list.html', {'playlists': playlists})

def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    return render(request, 'music/playlist_detail.html', {'playlist': playlist})