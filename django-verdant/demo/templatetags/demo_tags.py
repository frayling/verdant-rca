from django import template
from demo.models import *

register = template.Library()


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    return context['request'].site.root_page


def has_menu_children(page):
    if page.get_children().filter(live=True, show_in_menus=True):
        return True;
    else:
        return False;


# Retrieves the top menu items - the immediate children of the calling page
# The has_menu_children method is necessary because the bootstrap menu requires a dropdown class to be applied to a parent
@register.inclusion_tag('demo/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().filter(live=True, show_in_menus=True)
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'], #required by the {% pageurl %} tag that we want to use within this template
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('demo/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children().filter(live=True, show_in_menus=True)
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        'request': context['request'], #required by the {% pageurl %} tag that we want to use within this template
    }


# Retrieves the secondary links for the 'also in this section' links - either the children or siblings of the current page
@register.inclusion_tag('demo/tags/secondary_menu.html', takes_context=True)
def secondary_menu(context, calling_page=None):
    pages = []
    if calling_page:
        pages = calling_page.get_children().filter(live=True, show_in_menus=True)

        # If no children, get siblings instead
        if len(pages) == 0:
            pages = calling_page.get_other_siblings().filter(live=True, show_in_menus=True)
    return {
        'pages': pages,
        'request': context['request'],  #required by the {% pageurl %} tag that we want to use within this template
    }


# Retrieves all live pages which are children of the calling page - for standard index listing
@register.inclusion_tag('demo/tags/standard_index_listing.html', takes_context=True)
def standard_index_listing(context, calling_page):
    pages = calling_page.get_children().filter(live=True)
    return {
        'pages': pages,
        'request': context['request'],  # required by the {% pageurl %} tag that we want to use within this template
    }


# Person feed for home page
@register.inclusion_tag('demo/tags/person_listing_homepage.html', takes_context=True)
def person_listing_homepage(context, count=2):
    people = PersonPage.objects.filter(live=True).order_by('?')
    return {
        'people': people[:count],
        'request': context['request'],  # required by the {% pageurl %} tag that we want to use within this template
    }


# Blog feed for home page
@register.inclusion_tag('demo/tags/blog_listing_homepage.html', takes_context=True)
def blog_listing_homepage(context, count=2):
    blogs = BlogPage.objects.filter(live=True).order_by('-date')
    return {
        'blogs': blogs[:count],
        'request': context['request'],  # required by the {% pageurl %} tag that we want to use within this template
    }


# Events feed for home page
@register.inclusion_tag('demo/tags/event_listing_homepage.html', takes_context=True)
def event_listing_homepage(context, count=2):
    events = EventPage.objects.filter(live=True).filter(date_from__gte=date.today()).order_by('date_from')
    return {
        'events': events[:count],
        'request': context['request'],  # required by the {% pageurl %} tag that we want to use within this template
    }


# Advert snippets
@register.inclusion_tag('demo/tags/adverts.html', takes_context=True)
def adverts(context):
    return {
        'adverts': DemoAdvert.objects.all(),
        'request': context['request'],
    }


# Format times e.g. on event page
@register.filter
def time_display(time):
    # Get hour and minute from time object
    hour = time.hour
    minute = time.minute

    # Convert to 12 hour format
    if hour >= 12:
        pm = True
        hour -=12
    else:
        pm = False
    if hour == 0:
        hour = 12

    # Hour string
    hour_string = str(hour)

    # Minute string
    if minute != 0:
        minute_string = "." + str(minute)
    else:
        minute_string = ""

    # PM string
    if pm:
        pm_string = "pm"
    else:
        pm_string = "am"

    # Join and return
    return "".join([hour_string, minute_string, pm_string])