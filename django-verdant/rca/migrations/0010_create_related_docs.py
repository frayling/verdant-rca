# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ("wagtaildocs", "0002_initial_data"),
    )

    def forwards(self, orm):
        # Adding model 'RelatedDocument'
        db.create_table(u'rca_relateddocument', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(related_name='related_documents', to=orm['wagtailcore.Page'])),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['wagtaildocs.Document'])),
        ))
        db.send_create_signal(u'rca', ['RelatedDocument'])


    def backwards(self, orm):
        # Deleting model 'RelatedDocument'
        db.delete_table(u'rca_relateddocument')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numchild': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'path': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'rca.authorpage': {
            'Meta': {'object_name': 'AuthorPage', '_ormbases': [u'rca.EditorialPage']},
            u'editorialpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['rca.EditorialPage']", 'unique': 'True', 'primary_key': 'True'}),
            'mugshot': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailimages.Image']"})
        },
        u'rca.authorsindex': {
            'Meta': {'object_name': 'AuthorsIndex', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'rca.editorialpage': {
            'Meta': {'object_name': 'EditorialPage', '_ormbases': [u'wagtailcore.page']},
            'body': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'rca.newsindex': {
            'Meta': {'object_name': 'NewsIndex', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'rca.newsitem': {
            'Meta': {'object_name': 'NewsItem', '_ormbases': [u'rca.EditorialPage']},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'news_items'", 'null': 'True', 'to': u"orm['rca.AuthorPage']"}),
            u'editorialpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['rca.EditorialPage']", 'unique': 'True', 'primary_key': 'True'}),
            'lead_image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailimages.Image']"})
        },
        u'rca.programmepage': {
            'Meta': {'object_name': 'ProgrammePage', '_ormbases': [u'wagtailcore.page']},
            'download_document_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'download_document_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'head_of_programme': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'head_of_programme_statement': ('wagtail.wagtailcore.fields.RichTextField', [], {}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'programme_video': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rca.programmepagecarouselitem': {
            'Meta': {'object_name': 'ProgrammePageCarouselItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailimages.Image']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carousel_items'", 'to': u"orm['rca.ProgrammePage']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagefacilities': {
            'Meta': {'object_name': 'ProgrammePageFacilities'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailimages.Image']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facilities'", 'to': u"orm['rca.ProgrammePage']"}),
            'text': ('wagtail.wagtailcore.fields.RichTextField', [], {})
        },
        u'rca.programmepageoursites': {
            'Meta': {'object_name': 'ProgrammePageOurSites'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailimages.Image']"}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'our_sites'", 'to': u"orm['rca.ProgrammePage']"}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagerelatedlink': {
            'Meta': {'object_name': 'ProgrammePageRelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_links'", 'to': u"orm['rca.ProgrammePage']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.programmepagestudentstory': {
            'Meta': {'object_name': 'ProgrammePageStudentStory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailimages.Image']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_stories'", 'to': u"orm['rca.ProgrammePage']"}),
            'text': ('wagtail.wagtailcore.fields.RichTextField', [], {})
        },
        u'rca.relateddocument': {
            'Meta': {'object_name': 'RelatedDocument'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtaildocs.Document']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'related_documents'", 'to': u"orm['wagtailcore.Page']"})
        },
        u'rca.relatedlink': {
            'Meta': {'object_name': 'RelatedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['wagtailimages.Image']"}),
            'link_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'generic_related_links'", 'to': u"orm['wagtailcore.Page']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rca.schoolpage': {
            'Meta': {'object_name': 'SchoolPage', '_ormbases': [u'wagtailcore.page']},
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['wagtailcore.Page']", 'unique': 'True', 'primary_key': 'True'})
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
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'wagtailimages.image': {
            'Meta': {'object_name': 'Image'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['rca']