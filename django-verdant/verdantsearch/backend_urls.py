from django.conf.urls import patterns, url


urlpatterns = patterns("verdantsearch.views",
    url(r"^editorspicks/$", "editorspicks.index", name="verdantsearch_editorspicks_index"),
    url(r"^editorspicks/add/$", "editorspicks.add", name="verdantsearch_editorspicks_add"),
    url(r"^editorspicks/(\d+)/$", "editorspicks.edit", name="verdantsearch_editorspicks_edit"),
    url(r"^editorspicks/(\d+)/delete/$", "editorspicks.delete", name="verdantsearch_editorspicks_delete"),

    url(r"^searchterms/chooser/$", "searchterms.chooser", name="verdantsearch_searchterms_chooser"),
    url(r"^searchterms/chooser/results/$", "searchterms.chooserresults", name="verdantsearch_searchterms_chooserresults"),
)