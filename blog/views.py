#from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post


#all_posts = [
    # {
    #     "slug": "hike-in-the-mountains",
    #     "image": "mountain.jpg",
    #     "author": "Sravan",
    #     "date": date(2020, 1, 7),
    #     "title": "Mountain Hiking",
    #     "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
    #     "content":"""
    #         Hiking is a long, vigorous walk, usually on trails or footpaths in the countryside. 
    #         Walking for pleasure developed in Europe during the eighteenth century. 
    #         Religious pilgrimages have existed much longer but they involve walking long distances 
    #         for a spiritual purpose associated with specific religions.

    #         "Hiking" is the preferred term in Canada and the United States; the term walking is 
    #         used in these regions for shorter, particularly urban walks. In the United Kingdom and 
    #         the Republic of Ireland, the word "walking" describes all forms of walking, whether it 
    #         is a walk in the park or backpacking in the Alps. The word hiking is also often used in 
    #         the UK, along with rambling (a slightly old-fashioned term), hillwalking, and fell 
    #         walking (a term mostly used for hillwalking in northern England). The term bushwalking 
    #         is endemic to Australia, having been adopted by the Sydney Bush Walkers club in 1927. 
    #         In New Zealand a long, vigorous walk or hike is called tramping. It is a popular 
    #         activity with numerous hiking organizations worldwide, and studies suggest that all 
    #         forms of walking have health benefits.
    #         """
    # },
    # {
    #      "slug": "sunset-at-the-ocean",
    #     "image": "ocean.jpg",
    #     "author": "Sravan",
    #     "date": date(2020, 4, 7),
    #     "title": "Ocean Sunset",
    #     "excerpt": "One day, all your worries will set like the sun does and deserved happiness will come gushing like waves at the beach do.",
    #     "content": """
    #         Always beautiful, ocean sunsets are never quite the same, influenced as they are by 
    #         atmospheric conditions, the weather, the season and the state of the sea itself.  
    #         Nevertheless, this natural spectacle is also tinged with an element of fear, acquired 
    #         from the collective experience of our distant ancestors who had no knowledge of 
    #         astronomy and had many reasons to fear the darkness.

    #         While we no longer light bonfires or make sacrifices to bring back our life-giving 
    #         sun, its daily disappearance does unveil the disturbing truth that our civilization is 
    #         relatively insignificant.  Countless suns shine from the night sky, challenging the 
    #         delusions that fuel our personal comfort and self-importance. 
    #         """
    # },
    # {
    #      "slug": "beauty-in-the-forest",
    #     "image": "forest.jpg",
    #     "author": "Sravan",
    #     "date": date(2020, 7, 7),
    #     "title": "Forest Beauty",
    #     "excerpt": "For in the true nature of things, if we rightly consider, every green tree is far more glorious than if it were made of gold and silver.",
    #     "content": """
    #         A forest is a piece of land with many trees. Many animals need forests to live and 
    #         survive. Forests are very important and grow in many places around the world. They 
    #         are an ecosystem which includes many plants and animals.

    #         Temperature and rainfall are the two most important things for forests. Many places 
    #         are too cold or too dry for them. Forests can exist from the equator to near the polar 
    #         regions, but different climates have different kinds of forests. In cold climates conifers 
    #         dominate, but in temperate zone and tropical climates forests are mainly made up of 
    #         flowering plants. Different rainfall also makes different kinds of forest. No forests exist 
    #         in deserts, just a few trees in places where their roots can get at some underground water.
    #         """
    # }

#]

def get_date(post):
    return post["date"]


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]           #We use this instead of comment lines
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
         "posts" : latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html",{
        "all_posts": all_posts
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    #identified_post = next(post for post in all_posts if post["slug"]==slug)
    return render(request, "blog/post-detail.html", {
        "post" : identified_post,
        "post_tags" : identified_post.tags.all()
    })