from django.shortcuts import render, get_object_or_404
from .models import About

# Create your views here.
def about_me(request):
    """
    Display the about text.

    **Context**

    **Template:**

    :template:`blog/post_detail.html`
    """

    about = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
