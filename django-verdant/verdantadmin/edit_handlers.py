from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.forms.widgets import TextInput, Textarea, HiddenInput
from django.forms.models import modelform_factory, inlineformset_factory
from django.contrib.contenttypes.models import ContentType

from core.models import Page


def get_form_for_model(model, **kwargs):
    # django's modelform_factory with a bit of custom behaviour
    # (dealing with Treebeard's tree-related fields that really should have
    # been editable=False)
    if issubclass(model, Page):
        kwargs['exclude'] = kwargs.get('exclude', []) + ['content_type', 'path', 'depth', 'numchild']

    return modelform_factory(model, **kwargs)


def extract_panel_definitions_from_form_class(form_class):
    panels = []

    for field_name, field in form_class.base_fields.items():
        try:
            panel_class = field.widget.get_panel()
        except AttributeError:
            panel_class = FieldPanel

        panel = panel_class(field_name)
        panels.append(panel)

    return panels


class EditHandler(object):
    """
    Abstract class providing sensible default behaviours for objects implementing
    the EditHandler API
    """

    # return list of widget overrides that this EditHandler wants to be in place
    # on the form it receives
    @classmethod
    def widget_overrides(cls):
        return {}

    # the top-level edit handler is responsible for providing a form class that can produce forms
    # acceptable to the edit handler
    _form_class = None
    @classmethod
    def get_form_class(cls, model):
        if cls._form_class is None:
            cls._form_class = get_form_for_model(model, widgets=cls.widget_overrides())
        return cls._form_class

    def __init__(self, data=None, files=None, instance=None, form=None):
        if not instance:
            raise ValueError("EditHandler did not receive an instance object")
        self.instance = instance

        if not form:
            raise ValueError("EditHandler did not receive a form object")
        self.form = form


    # Heading / help text to display to the user
    heading = ""
    help_text = ""

    def object_classnames(self):
        """
        Additional classnames to add to the <li class="object"> when rendering this
        within an ObjectList
        """
        return ""

    def field_classnames(self):
        """
        Additional classnames to add to the <li> when rendering this within a
        <ul class="fields">
        """
        return ""

    def render_as_object(self):
        """
        Render this object as it should appear within an ObjectList. Should not
        include the <h2> heading or help text - ObjectList will supply those
        """
        # by default, assume that the subclass provides a catch-all render() method
        return self.render()

    def render_as_field(self):
        """
        Render this object as it should appear within a <ul class="fields"> list item
        """
        # by default, assume that the subclass provides a catch-all render() method
        return self.render()

    def render_js(self):
        """
        Render a snippet of Javascript code to be executed when this object's rendered
        HTML is inserted into the DOM. (This won't necessarily happen on page load...)
        """
        return ""

    def is_valid(self):
        """
        Return false if any of the data that this EditHandler is responsible for handling
        is invalid. (NB very few EditHandlers actually handle data; in particular,
        FieldPanels don't (the accompanying Form instance does it instead).)
        """
        return True

    def pre_save(self):
        """
        Do the manipulations that have to be done before the instance is saved.
        (Again, few if any EditHandlers actually have to do anything here;
        usually the form object will handle it.)
        """
        pass

    def post_save(self):
        """
        Do the manipulations that have to be done after the instance is saved.
        """
        pass

    def rendered_fields(self):
        """
        return a list of the fields of the passed form which are rendered by this
        EditHandler.
        """
        return []

    def render_missing_fields(self):
        """
        Helper function: render all of the fields of the form that are not accounted for
        in rendered_fields
        """
        rendered_fields = self.rendered_fields()
        missing_fields_html = [
            unicode(self.form[field_name])
            for field_name in self.form.fields
            if field_name not in rendered_fields
        ]

        return mark_safe(u''.join(missing_fields_html))


class BaseCompositeEditHandler(EditHandler):
    """
    Abstract class for EditHandlers that manage a set of sub-EditHandlers.
    Concrete subclasses must attach a 'children' property
    """
    _widget_overrides = None
    @classmethod
    def widget_overrides(cls):
        if cls._widget_overrides is None:
            # build a collated version of all its children's widget lists
            widgets = {}
            for handler_class in cls.children:
                widgets.update(handler_class.widget_overrides())
            cls._widget_overrides = widgets

        return cls._widget_overrides

    def __init__(self, data=None, files=None, instance=None, form=None):
        super(BaseCompositeEditHandler, self).__init__(data, files, instance=instance, form=form)

        self.children = [
            handler_class(data, files, instance=self.instance, form=self.form)
            for handler_class in self.__class__.children
        ]

    def render(self):
        return mark_safe(render_to_string(self.template, {
            'self': self
        }))

    def render_js(self):
        return mark_safe(u'\n'.join([handler.render_js() for handler in self.children]))

    def is_valid(self):
        result = True
        for handler in self.children:
            result &= handler.is_valid()
        return result

    def pre_save(self):
        for handler in self.children:
            handler.pre_save()

    def post_save(self):
        for handler in self.children:
            handler.post_save()

    def rendered_fields(self):
        result = []
        for handler in self.children:
            result += handler.rendered_fields()

        return result

class BaseTabbedInterface(BaseCompositeEditHandler):
    template = "verdantadmin/edit_handlers/tabbed_interface.html"

def TabbedInterface(children):
    return type('_TabbedInterface', (BaseTabbedInterface,), {'children': children})


class BaseObjectList(BaseCompositeEditHandler):
    template = "verdantadmin/edit_handlers/object_list.html"

def ObjectList(children, heading=""):
    return type('_ObjectList', (BaseObjectList,), {
        'children': children,
        'heading': heading,
    })


class BaseMultiFieldPanel(BaseCompositeEditHandler):
    template = "verdantadmin/edit_handlers/multi_field_panel.html"

def MultiFieldPanel(children, heading=""):
    return type('_MultiFieldPanel', (BaseMultiFieldPanel,), {
        'children': children,
        'heading': heading,
    })


class BaseFieldPanel(EditHandler):
    def __init__(self, data=None, files=None, instance=None, form=None):
        super(BaseFieldPanel, self).__init__(data, files, instance=instance, form=form)
        self.bound_field = self.form[self.field_name]

        self.heading = self.bound_field.label
        self.help_text = self.bound_field.help_text

    def object_classnames(self):
        widget = self.bound_field.field.widget
        if isinstance(widget, TextInput) or isinstance(widget, Textarea):
            return 'full'
        else:
            return ''

    def field_classnames(self):
        # TODO: insert a classname appropriate to the widget, e.g. "text", "radio", "checkbox"
        if self.bound_field.errors:
            return "error"
        else:
            return ""

    object_template = "verdantadmin/edit_handlers/field_panel_object.html"
    def render_as_object(self):
        return mark_safe(render_to_string(self.object_template, {
            'self': self,
            'field_content': self.render_as_field(show_help_text=False),
        }))        

    field_template = "verdantadmin/edit_handlers/field_panel_field.html"
    def render_as_field(self, show_help_text=True):
        return mark_safe(render_to_string(self.field_template, {
            'field': self.bound_field,
            'show_help_text': show_help_text,
        }))

    def rendered_fields(self):
        return [self.field_name]

def FieldPanel(field_name):
    return type('_FieldPanel', (BaseFieldPanel,), {
        'field_name': field_name,
    })


class BaseRichTextFieldPanel(BaseFieldPanel):
    def render_js(self):
        return mark_safe("makeRichTextEditable(fixPrefix('%s'));" % self.bound_field.id_for_label)

def RichTextFieldPanel(field_name):
    return type('_RichTextFieldPanel', (BaseRichTextFieldPanel,), {
        'field_name': field_name,
    })


class BasePageChooserPanel(BaseFieldPanel):
    field_template = "verdantadmin/edit_handlers/page_chooser_panel.html"

    @classmethod
    def widget_overrides(cls):
        return {cls.field_name: HiddenInput}

    _target_content_type = None
    @classmethod
    def target_content_type(cls):
        if cls._target_content_type is None:
            if cls.page_type:
                cls._target_content_type = ContentType.objects.get_for_model(cls.page_type)
            else:
                # TODO: infer the content type by introspection on the foreign key
                cls._target_content_type = ContentType.objects.get_by_natural_key('core', 'page')

        return cls._target_content_type

    def render_as_field(self, show_help_text=True):
        return mark_safe(render_to_string(self.field_template, {
            'field': self.bound_field,
            'page': getattr(self.instance, self.field_name),
            'show_help_text': show_help_text,
        }))

    def render_js(self):
        page = getattr(self.instance, self.field_name)
        parent = page.get_parent() if page else None
        content_type = self.__class__.target_content_type()

        return mark_safe("createPageChooser(fixPrefix('%s'), '%s/%s', %s);" % (
            self.bound_field.id_for_label,
            content_type.app_label,
            content_type.model,
            (parent.id if parent else 'null'),
        ))

def PageChooserPanel(field_name, page_type=None):
    return type('_PageChooserPanel', (BasePageChooserPanel,), {
        'field_name': field_name,
        'page_type': page_type,
    })


class BaseInlinePanel(EditHandler):
    # get_child_form_class is dependent on get_child_edit_handler_class if a panel list is passed
    #   (so that the edit handler can specify widget overrides on the form);
    # get_child_edit_handler_class is dependent on get_child_form_class if a panel list is NOT passed
    #   (because the edit handler needs to find out its panel list from the form).
    # Look ma, no circular dependency!

    _child_edit_handler_class = None
    @classmethod
    def get_child_edit_handler_class(cls):
        if cls._child_edit_handler_class is None:
            if cls.panels is None:
                form_class = cls.get_child_form_class()
                panels = extract_panel_definitions_from_form_class(form_class)
            else:
                panels = cls.panels

            cls._child_edit_handler_class = MultiFieldPanel(panels, heading=cls.heading)

        return cls._child_edit_handler_class

    _child_form_class = None
    @classmethod
    def get_child_form_class(cls):
        if cls._child_form_class is None:
            if cls.panels is None:
                # go ahead and create the formset without any intervention from panel definitions
                cls._child_form_class = get_form_for_model(cls.related_model)
            else:
                # fetch/build the EditHandler first, and let that specify widget overrides
                edit_handler_class = cls.get_child_edit_handler_class()
                cls._child_form_class = get_form_for_model(cls.related_model, widgets=edit_handler_class.widget_overrides())

        return cls._child_form_class

    _formset_class = None
    @classmethod
    def get_formset_class(cls):
        if cls._formset_class is None:
            form_class = cls.get_child_form_class()
            cls._formset_class = inlineformset_factory(cls.base_model, cls.related_model, form=form_class, extra=0)

            # at this point we can fill in a heading, if we don't have one already
            if not cls.heading:
                relation_name = cls._formset_class.fk.rel.related_name
                cls.heading = relation_name.replace('_', ' ').capitalize()

        return cls._formset_class


    def __init__(self, data=None, files=None, instance=None, form=None):
        super(BaseInlinePanel, self).__init__(data, files, instance=instance, form=form)

        formset_class = self.__class__.get_formset_class()
        self.formset = formset_class(data, files, instance=self.instance)

        child_edit_handler_class = self.__class__.get_child_edit_handler_class()
        self.children = []
        for subform in self.formset.forms:
            # override the DELETE field to have a hidden input
            subform.fields['DELETE'].widget = HiddenInput()
            self.children.append(
                child_edit_handler_class(data, files, instance=subform.instance, form=subform)
            )

        empty_form = self.formset.empty_form
        empty_form.fields['DELETE'].widget = HiddenInput()
        self.empty_child = child_edit_handler_class(data, files, instance=empty_form.instance, form=empty_form)

    template = "verdantadmin/edit_handlers/inline_panel.html"
    def render(self):
        return mark_safe(render_to_string(self.template, {
            'self': self,
        }))

    js_template = "verdantadmin/edit_handlers/inline_panel.js"
    def render_js(self):
        return mark_safe(render_to_string(self.js_template, {
            'self': self,
        }))

    def is_valid(self):
        result = self.formset.is_valid()
        for child in self.children:
            result &= child.is_valid()
        return result

    def pre_save(self):
        for child in self.children:
            child.pre_save()

    def post_save(self):
        self.formset.save()
        for child in self.children:
            child.post_save()

def InlinePanel(base_model, related_model, panels=None, label='', help_text=''):
    return type('_InlinePanel', (BaseInlinePanel,), {
        'base_model': base_model,
        'related_model': related_model,
        'panels': panels,
        'heading': label,
        'help_text': help_text,  # TODO: can we pick this out of the foreign key definition as an alternative? (with a bit of help from the inlineformset object, as we do for label/heading)
    })


# Now that we've defined EditHandlers, we can set up core.Page to have some.
Page.content_panels = [
    FieldPanel('title'),
    FieldPanel('slug'),
]
Page.promote_panels = [
]