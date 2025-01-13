from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.

posts = [
  {
    "slug": "how-to-build-a-website",
    "img": "mountains.jpg",
    "author": "Jane Doe",
    "date": date(2025, 1, 3),
    "title": "How to Build a Website from Scratch",
    "excerpt": "Building a website from scratch might sound intimidating, but with the right tools and approach, it's simpler than you think. In this guide, we'll walk you through the essential steps to get started.",
    "content": "Building a website from scratch requires a combination of planning, design, and coding. First, you'll need to choose a domain name and a hosting provider. Next, you’ll need to decide on the platform—whether you choose a content management system (CMS) like WordPress, or you code your website manually using HTML, CSS, and JavaScript. For beginners, we recommend starting with a website builder that allows you to customize pre-built templates. Throughout this article, we’ll guide you through each step and provide helpful resources to make the process easier."
  },
  {
    "slug": "best-ways-to-boost-your-productivity",
    "img": "woods.jpg",
    "author": "John Smith",
    "date": date(2025, 1, 10),
    "title": "Best Ways to Boost Your Productivity",
    "excerpt": "Feeling unproductive? It's time to change that. In this post, we'll share practical strategies to help you stay focused, organized, and get more done in less time.",
    "content": "Productivity can often be the key to achieving both professional and personal success. A few changes to your daily habits can have a significant impact. Try using the Pomodoro Technique to break your work into focused intervals. Also, prioritize tasks based on importance rather than urgency, and eliminate distractions by setting clear boundaries in your workspace. We'll also discuss tools like task managers and time-tracking apps that can help streamline your workflow."
  },
  {
    "slug": "understanding-mindfulness-meditation",
    "img": "mountains.jpg",
    "author": "Alice Green",
    "date": date(2025, 1, 7),
    "title": "Understanding Mindfulness Meditation",
    "excerpt": "Mindfulness meditation has become a popular practice in recent years. Learn how to practice it and the benefits it can bring to your mental well-being.",
    "content": "Mindfulness meditation is the practice of focusing your mind on the present moment, often by paying attention to your breath, body sensations, or sounds around you. Regular practice has been shown to reduce stress, enhance emotional health, and improve focus. In this article, we'll walk you through how to get started with mindfulness meditation, from finding a quiet space to setting aside time for daily practice."
  },
  {
    "slug": "top-10-travel-destinations-for-2025",
    "img": "woods.jpg",
    "author": "Michael Ray",
    "date": date(2025, 1, 5),
    "title": "Top 10 Travel Destinations for 2025",
    "excerpt": "Looking for your next adventure? Here are the top 10 travel destinations to visit in 2025, offering a mix of culture, nature, and luxury.",
    "content": "2025 is set to be an exciting year for travelers. From the stunning beaches of the Maldives to the rich cultural experiences in Japan, there's something for everyone. Whether you're interested in outdoor adventures, cultural immersion, or simply relaxing in luxury resorts, this list has you covered. We'll also share some tips on how to travel sustainably and make the most of your trips."
  },
  {
    "slug": "simple-healthy-recipes-for-busy-people",
    "img": "mountains.jpg",
    "author": "Sarah Johnson",
    "date": date(2025, 1, 6),
    "title": "Simple Healthy Recipes for Busy People",
    "excerpt": "Eating healthy doesn't have to be time-consuming. Here are five simple and nutritious recipes that you can prepare even on your busiest days.",
    "content": "When you're busy, cooking healthy meals can seem like a challenge. But with a little planning, it's easy to create meals that are both quick and nourishing. From overnight oats for breakfast to easy stir-fry recipes for lunch or dinner, we've got you covered. These meals are full of vegetables, lean proteins, and whole grains, ensuring that you stay energized and satisfied throughout your day."
  }
]

def get_date(post):
    return post['date']


def start_page(req):
    sorted_posts = sorted(posts, key=get_date)
    print(sorted_posts)
    latest_posts = sorted_posts[-3:]
    print(latest_posts)
    return render(req, "blog/start_page.html", {"latest_posts":latest_posts})

def all_posts(req):
    return render(req, "blog/all_posts.html", {"all_posts": posts})

def individual_post(req, slug):
    post = next(post for post in posts if post['slug'] == slug)
    print(post)
    return render(req, "blog/post_details.html", {"identified_post": post})
