from django.shortcuts import render, redirect
from NotTwitter.models import Profile, NotATweet
from NotTwitter.forms import NotATweetForm

def dashboard(request):
    form = NotATweetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            not_tweet = form.save(commit=False)
            not_tweet.user = request.user
            not_tweet.save()
            return redirect('NotTwitter:dashboard')

    followed_not_tweets = NotATweet.objects.filter(
        user__profile__in=request.user.profile.followed.all()
    ).order_by('-created_at')

    return render(
        request, 
        'NotTwitter/dashboard.html', 
        {'form' : form, 'not_tweets' : followed_not_tweets}
    )

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'NotTwitter/profile_list.html', {'profiles' : profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, 'NotTwitter/profile.html', {'profile' : profile})