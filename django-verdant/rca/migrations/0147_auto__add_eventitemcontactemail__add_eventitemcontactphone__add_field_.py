# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventItemContactEmail'
        db.create_table(u'rca_eventitemcontactemail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='contact_email', to=orm['rca.EventItem'])),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'rca', ['EventItemContactEmail'])

        # Adding model 'EventItemContactPhone'
        db.create_table(u'rca_eventitemcontactphone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('page', self.gf('modelcluster.fields.ParentalKey')(related_name='contact_phone', to=orm['rca.EventItem'])),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'rca', ['EventItemContactPhone'])

        # Adding field 'EventItem.contact_title'
        db.add_column(u'rca_eventitem', 'contact_title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'EventItem.contact_address'
        db.add_column(u'rca_eventitem', 'contact_address',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'EventItem.contact_link'
        db.add_column(u'rca_eventitem', 'contact_link',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'EventItem.contact_link_text'
        db.add_column(u'rca_eventitem', 'contact_link_text',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'EventItemContactEmail'
        db.delete_table(u'rca_eventitemcontactemail')

        # Deleting model 'EventItemContactPhone'
        db.delete_table(u'rca_eventitemcontactphone')

        # Deleting field 'EventItem.contact_title'
        db.delete_column(u'rca_eventitem', 'contact_title')

        # Deleting field 'EventItem.contact_address'
        db.delete_column(u'rca_eventitem', 'contact_address')

        # Deleting field 'EventItem.contact_link'
        db.delete_column(u'rca_eventitem', 'contact_link')

        # Deleting field 'EventItem.contact_link_text'
        db.delete_column(u'rca_eventitem', 'contact_link_text')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wagtailcore.page': {
            'Meta': {'object_name': 'Page'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pages'", 'to': u"orm['contenttypes.ContentType']"}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'feed_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'has_unpublished_changes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'seo_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'show_in_menus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.advert': {
            'Meta': {'object_name': 'Advert'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'adverts'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'plain_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'show_globally': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'rca.advertplacement': {
            'Meta': {'object_name': 'AdvertPlacement'},
            'advert': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'advert_placements'", 'to': u"orm['wagtailcore.Page']"})
        },
        u'rca.alumniindex': {
            'Meta': {'object_name': 'AlumniIndex', '_ormbases': [u'wagtailcore.page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.alumniindexad': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'AlumniIndexAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.AlumniIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.alumniindexrelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'AlumniIndexRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.AlumniIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.alumnipage': {
            'Meta': {'object_name': 'AlumniPage', '_ormbases': [u'wagtailcore.page']},
            'biography': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'listing_intro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'profile_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
        },
        u'rca.contactuspage': {
            'Meta': {'object_name': 'ContactUsPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.currentresearchpage': {
            'Meta': {'object_name': 'CurrentResearchPage', '_ormbases': [u'wagtailcore.page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.currentresearchpagead': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'CurrentResearchPageAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.CurrentResearchPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.customcontentmodule': {
            'Meta': {'object_name': 'CustomContentModule'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.customcontentmoduleblock': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'CustomContentModuleBlock'},
            'content_module': ('modelcluster.fields.ParentalKey', [], {'related_name': "'blocks'", 'to': u"orm['rca.CustomContentModule']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'item_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.customecontentmoduleplacement': {
            'Meta': {'object_name': 'CustomeContentModulePlacement'},
            'custom_content_module': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.CustomContentModule']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'custom_content_module_placements'", 'to': u"orm['wagtailcore.Page']"})
        },
        u'rca.eventindex': {
            'Meta': {'object_name': 'EventIndex', '_ormbases': [u'wagtailcore.page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.eventindexad': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventIndexAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.EventIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.eventindexrelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventIndexRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.EventIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.eventitem': {
            'Meta': {'object_name': 'EventItem', '_ormbases': [u'wagtailcore.page']},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'audience': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'contact_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'contact_link_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cost': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'eventbrite_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'external_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'external_link_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'listing_intro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'middle_column_body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'specific_directions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'specific_directions_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'rca.eventitemcarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventItemCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.EventItem']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.eventitemcontactemail': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventItemContactEmail'},
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_email'", 'to': u"orm['rca.EventItem']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.eventitemcontactphone': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventItemContactPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_phone'", 'to': u"orm['rca.EventItem']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.eventitemdatestimes': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventItemDatesTimes'},
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'dates_times'", 'to': u"orm['rca.EventItem']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'time_from': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'time_to': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.eventitemrelatedarea': {
            'Meta': {'object_name': 'EventItemRelatedArea'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_areas'", 'to': u"orm['rca.EventItem']"})
        },
        u'rca.eventitemrelatedprogramme': {
            'Meta': {'object_name': 'EventItemRelatedProgramme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_programmes'", 'to': u"orm['rca.EventItem']"}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.eventitemrelatedschool': {
            'Meta': {'object_name': 'EventItemRelatedSchool'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_schools'", 'to': u"orm['rca.EventItem']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.eventitemspeaker': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'EventItemSpeaker'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'speakers'", 'to': u"orm['rca.EventItem']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.gallerypage': {
            'Meta': {'object_name': 'GalleryPage', '_ormbases': [u'wagtailcore.page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.gallerypagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'GalleryPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.GalleryPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.homepage': {
            'Meta': {'object_name': 'HomePage', '_ormbases': [u'wagtailcore.page']},
            'background_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'news_item_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'news_item_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'packery_news': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'packery_rcanow': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'packery_staff': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'packery_standard': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'packery_student_work': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'packery_tweets': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.homepagead': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'HomePageAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.HomePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.homepagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'HomePageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.HomePage']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.jobpage': {
            'Meta': {'object_name': 'JobPage', '_ormbases': [u'wagtailcore.page']},
            'campus': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'closing_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'download_info': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'interview_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'listing_intro': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'other_department': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ref_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'required_hours': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'responsible_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'salary': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.jobsindex': {
            'Meta': {'object_name': 'JobsIndex', '_ormbases': [u'wagtailcore.page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.jobsindexad': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'JobsIndexAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.JobsIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.jobsindexrelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'JobsIndexRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.JobsIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.newsindex': {
            'Meta': {'object_name': 'NewsIndex', '_ormbases': [u'wagtailcore.page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.newsindexad': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'NewsIndexAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.NewsIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.newsitem': {
            'Meta': {'object_name': 'NewsItem', '_ormbases': [u'wagtailcore.page']},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'listing_intro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'rca_content_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.newsitemcarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'NewsItemCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.NewsItem']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.newsitemlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'NewsItemLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.NewsItem']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.newsitemrelatedprogramme': {
            'Meta': {'object_name': 'NewsItemRelatedProgramme'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_programmes'", 'to': u"orm['rca.NewsItem']"}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.newsitemrelatedschool': {
            'Meta': {'object_name': 'NewsItemRelatedSchool'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_schools'", 'to': u"orm['rca.NewsItem']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.programmedocuments': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ProgrammeDocuments'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'documents'", 'to': u"orm['rca.ProgrammePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.programmepage': {
            'Meta': {'object_name': 'ProgrammePage', '_ormbases': [u'wagtailcore.page']},
            'background_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'contact_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'contact_link_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'download_document_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'download_document_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'facilities_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'facilities_link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'facilities_text': ('wagtail.wagtailcore.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'head_of_programme': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.StaffPage']"}),
            'head_of_programme_link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'head_of_programme_statement': ('wagtail.wagtailcore.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'programme_video': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'programme_video_poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.programmepagead': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ProgrammePageAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.ProgrammePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.programmepagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ProgrammePageCarouselItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.ProgrammePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'rca.programmepagecontactemail': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ProgrammePageContactEmail'},
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_email'", 'to': u"orm['rca.ProgrammePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.programmepagecontactphone': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ProgrammePageContactPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_phone'", 'to': u"orm['rca.ProgrammePage']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.programmepageoursites': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ProgrammePageOurSites'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'our_sites'", 'to': u"orm['rca.ProgrammePage']"}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ProgrammePageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.ProgrammePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.programmepagestudentstory': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ProgrammePageStudentStory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'student_stories'", 'to': u"orm['rca.ProgrammePage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('wagtail.wagtailcore.fields.RichTextField', [], {})
        },
        u'rca.rcaimage': {
            'Meta': {'object_name': 'RcaImage'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dimensions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'eprint_docid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'permission': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'photographer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rca_content_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'width': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.rcanowindex': {
            'Meta': {'object_name': 'RcaNowIndex', '_ormbases': [u'wagtailcore.page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.rcanowpage': {
            'Meta': {'object_name': 'RcaNowPage', '_ormbases': [u'wagtailcore.page']},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.rcanowpagepagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'RcaNowPagePageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.RcaNowPage']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.rcarendition': {
            'Meta': {'unique_together': "(('image', 'filter'),)", 'object_name': 'RcaRendition'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'filter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['wagtailimages.Filter']"}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'renditions'", 'to': u"orm['rca.RcaImage']"}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'rca.researchinnovationpage': {
            'Meta': {'object_name': 'ResearchInnovationPage', '_ormbases': [u'wagtailcore.page']},
            'background_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'contact_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'contact_link_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'intro_link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'news_carousel_area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'teasers_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.researchinnovationpagead': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchInnovationPageAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.ResearchInnovationPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.researchinnovationpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchInnovationPageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.ResearchInnovationPage']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.researchinnovationpagecontactemail': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchInnovationPageContactEmail'},
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_email'", 'to': u"orm['rca.ResearchInnovationPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.researchinnovationpagecontactphone': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchInnovationPageContactPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_phone'", 'to': u"orm['rca.ResearchInnovationPage']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.researchinnovationpagecurrentresearch': {
            'Meta': {'object_name': 'ResearchInnovationPageCurrentResearch'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'current_research'", 'to': u"orm['rca.ResearchInnovationPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.researchinnovationpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchInnovationPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.ResearchInnovationPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.researchinnovationpageteaser': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchInnovationPageTeaser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'teasers'", 'to': u"orm['rca.ResearchInnovationPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'rca.researchitem': {
            'Meta': {'object_name': 'ResearchItem', '_ormbases': [u'wagtailcore.page']},
            'description': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'eprintid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'rca_content_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ref': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'research_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'work_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'work_type_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'rca.researchitemcarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchItemCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.ResearchItem']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.researchitemcreator': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchItemCreator'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manual_person_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'creator'", 'to': u"orm['rca.ResearchItem']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.researchitemlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchItemLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'links'", 'to': u"orm['rca.ResearchItem']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.researchstudentindex': {
            'Meta': {'object_name': 'ResearchStudentIndex', '_ormbases': [u'wagtailcore.page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.researchstudentindexad': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ResearchStudentIndexAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.ResearchStudentIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.reusabletextsnippet': {
            'Meta': {'object_name': 'ReusableTextSnippet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('wagtail.wagtailcore.fields.RichTextField', [], {})
        },
        u'rca.reusabletextsnippetplacement': {
            'Meta': {'object_name': 'ReusableTextSnippetPlacement'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'reusable_text_snippet_placements'", 'to': u"orm['wagtailcore.Page']"}),
            'reusable_text_snippet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.ReusableTextSnippet']"})
        },
        u'rca.reviewpage': {
            'Meta': {'object_name': 'ReviewPage', '_ormbases': [u'wagtailcore.page']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'middle_column_body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'strapline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.reviewpagead': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ReviewPageAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.ReviewPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.reviewpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ReviewPageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.ReviewPage']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.reviewpageimage': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ReviewPageImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'images'", 'to': u"orm['rca.ReviewPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.reviewpagequotation': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ReviewPageQuotation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'quotations'", 'to': u"orm['rca.ReviewPage']"}),
            'quotation': ('django.db.models.fields.TextField', [], {}),
            'quotee': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'quotee_job_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.reviewpagerelateddocument': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ReviewPageRelatedDocument'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'document_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'documents'", 'to': u"orm['rca.ReviewPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.reviewpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'ReviewPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.ReviewPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.schoolpage': {
            'Meta': {'object_name': 'SchoolPage', '_ormbases': [u'wagtailcore.page']},
            'background_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'contact_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'contact_link_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'head_of_research': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.StaffPage']"}),
            'head_of_research_link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'head_of_research_statement': ('wagtail.wagtailcore.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'head_of_school': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.StaffPage']"}),
            'head_of_school_link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'head_of_school_statement': ('wagtail.wagtailcore.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.schoolpagead': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'SchoolPageAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.SchoolPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.schoolpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'SchoolPageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.SchoolPage']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.schoolpagecontactemail': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'SchoolPageContactEmail'},
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_email'", 'to': u"orm['rca.SchoolPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.schoolpagecontactphone': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'SchoolPageContactPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_phone'", 'to': u"orm['rca.SchoolPage']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.schoolpagecontacttelemail': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'SchoolPageContactTelEmail'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_tel_email'", 'to': u"orm['rca.SchoolPage']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.schoolpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'SchoolPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.SchoolPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.staffindex': {
            'Meta': {'object_name': 'StaffIndex', '_ormbases': [u'wagtailcore.page']},
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.staffindexad': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StaffIndexAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.StaffIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.staffpage': {
            'Meta': {'object_name': 'StaffPage', '_ormbases': [u'wagtailcore.page']},
            'awards_and_grants': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'biography': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'current_recent_research': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'external_collaborations_placeholder': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'listing_intro': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'practice': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'profile_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'publications_exhibtions_and_other_outcomes_placeholder': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'rca_content_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'research_interests': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'show_on_programme_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'staff_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'supervised_student_other': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.staffpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StaffPageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.StaffPage']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.staffpagecollaborations': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StaffPageCollaborations'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'collaborations'", 'to': u"orm['rca.StaffPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.staffpagepublicationexhibition': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StaffPagePublicationExhibition'},
            'authors_collaborators': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'location_year': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'publications_exhibitions'", 'to': u"orm['rca.StaffPage']"}),
            'rca_content_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'typeof': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.staffpagerole': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StaffPageRole'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'roles'", 'to': u"orm['rca.StaffPage']"}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.standardindex': {
            'Meta': {'object_name': 'StandardIndex', '_ormbases': [u'wagtailcore.page']},
            'background_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'contact_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'contact_link_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'contact_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'events_feed_area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'intro_link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'news_carousel_area': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_events_feed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'strapline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'teasers_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.standardindexad': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardIndexAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.StandardIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardindexcarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardIndexCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.StandardIndex']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardindexcontactemail': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardIndexContactEmail'},
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_email'", 'to': u"orm['rca.StandardIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardindexcontactphone': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardIndexContactPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'contact_phone'", 'to': u"orm['rca.StandardIndex']"}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardindexcustomcontentmodules': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardIndexCustomContentModules'},
            'custom_content_module': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.CustomContentModule']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'custom_content_modules'", 'to': u"orm['rca.StandardIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardindexrelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardIndexRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.StandardIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardindexteaser': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardIndexTeaser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'teasers'", 'to': u"orm['rca.StandardIndex']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.standardpage': {
            'Meta': {'object_name': 'StandardPage', '_ormbases': [u'wagtailcore.page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'intro': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'middle_column_body': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'strapline': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.standardpagead': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageAd'},
            'ad': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.Advert']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'manual_adverts'", 'to': u"orm['rca.StandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.StandardPage']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardpageimage': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'images'", 'to': u"orm['rca.StandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardpagequotation': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageQuotation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'quotations'", 'to': u"orm['rca.StandardPage']"}),
            'quotation': ('django.db.models.fields.TextField', [], {}),
            'quotee': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'quotee_job_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardpagerelateddocument': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageRelatedDocument'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            'document_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'documents'", 'to': u"orm['rca.StandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardpagerelatedlink': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailcore.Page']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.StandardPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.standardpagereusabletextsnippet': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StandardPageReusableTextSnippet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'reusable_text_snippets'", 'to': u"orm['rca.StandardPage']"}),
            'reusable_text_snippet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['rca.ReusableTextSnippet']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.studentpage': {
            'Meta': {'object_name': 'StudentPage', '_ormbases': [u'wagtailcore.page']},
            'degree_qualification': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'degree_subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'degree_year': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'funding': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'profile_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'programme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rca_content_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'show_on_homepage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'social_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'social_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'specialism': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'statement': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'student_twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.StaffPage']"}),
            'twitter_feed': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'work_awards': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'work_description': ('wagtail.wagtailcore.fields.RichTextField', [], {'blank': 'True'}),
            'work_location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'work_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.studentpageawards': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageAwards'},
            'award': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'awards'", 'to': u"orm['rca.StudentPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.studentpagecarouselitem': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageCarouselItem'},
            'embedly_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'overlay_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.StudentPage']"}),
            'poster_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['rca.RcaImage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.studentpagecontactsemail': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageContactsEmail'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'email'", 'to': u"orm['rca.StudentPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.studentpagecontactsphone': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageContactsPhone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'phone'", 'to': u"orm['rca.StudentPage']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.studentpagecontactswebsite': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageContactsWebsite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'website'", 'to': u"orm['rca.StudentPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.studentpagedegree': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageDegree'},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'degrees'", 'to': u"orm['rca.StudentPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.studentpageexhibition': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageExhibition'},
            'exhibition': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'exhibitions'", 'to': u"orm['rca.StudentPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.studentpageexperience': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageExperience'},
            'experience': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'experiences'", 'to': u"orm['rca.StudentPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.studentpageworkcollaborator': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageWorkCollaborator'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'collaborators'", 'to': u"orm['rca.StudentPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rca.studentpageworksponsor': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'StudentPageWorkSponsor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'page': ('modelcluster.fields.ParentalKey', [], {'related_name': "'sponsor'", 'to': u"orm['rca.StudentPage']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        },
        u'wagtaildocs.document': {
            'Meta': {'object_name': 'Document'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'wagtailimages.filter': {
            'Meta': {'object_name': 'Filter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spec': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['rca']