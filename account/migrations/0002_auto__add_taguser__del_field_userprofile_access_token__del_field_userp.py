# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TagUser'
        db.create_table('account_taguser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.UserProfile'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tags.Tag'])),
        ))
        db.send_create_signal('account', ['TagUser'])

        # Deleting field 'UserProfile.access_token'
        db.delete_column('account_userprofile', 'access_token')

        # Deleting field 'UserProfile.gravatar_url'
        db.delete_column('account_userprofile', 'gravatar_url')

        # Deleting field 'UserProfile.facebook_id'
        db.delete_column('account_userprofile', 'facebook_id')

        # Adding field 'UserProfile.position'
        db.add_column('account_userprofile', 'position',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.phone'
        db.add_column('account_userprofile', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.adress'
        db.add_column('account_userprofile', 'adress',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.how_long_time_in_aeisec'
        db.add_column('account_userprofile', 'how_long_time_in_aeisec',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'UserProfile.university'
        db.add_column('account_userprofile', 'university',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TagUser'
        db.delete_table('account_taguser')

        # Adding field 'UserProfile.access_token'
        db.add_column('account_userprofile', 'access_token',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=150),
                      keep_default=False)

        # Adding field 'UserProfile.gravatar_url'
        db.add_column('account_userprofile', 'gravatar_url',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=100),
                      keep_default=False)

        # Adding field 'UserProfile.facebook_id'
        db.add_column('account_userprofile', 'facebook_id',
                      self.gf('django.db.models.fields.BigIntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'UserProfile.position'
        db.delete_column('account_userprofile', 'position')

        # Deleting field 'UserProfile.phone'
        db.delete_column('account_userprofile', 'phone')

        # Deleting field 'UserProfile.adress'
        db.delete_column('account_userprofile', 'adress')

        # Deleting field 'UserProfile.how_long_time_in_aeisec'
        db.delete_column('account_userprofile', 'how_long_time_in_aeisec')

        # Deleting field 'UserProfile.university'
        db.delete_column('account_userprofile', 'university')


    models = {
        'account.taguser': {
            'Meta': {'object_name': 'TagUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tags.Tag']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.UserProfile']"})
        },
        'account.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'how_long_time_in_aeisec': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'tag': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tags.Tag']", 'through': "orm['account.TagUser']", 'symmetrical': 'False'}),
            'university': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'discussion.discussion': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Discussion'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'discussion.post': {
            'Meta': {'ordering': "('-time',)", 'object_name': 'Post'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'discussion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discussion.Discussion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'tags.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'post': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['discussion.Post']", 'null': 'True', 'through': "orm['tags.TagsPost']", 'symmetrical': 'False'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tags.TagPriority']"}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'null': 'True', 'through': "orm['tags.TagsUser']", 'symmetrical': 'False'})
        },
        'tags.tagpriority': {
            'Meta': {'object_name': 'TagPriority'},
            'color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFF'", 'max_length': '25'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3'})
        },
        'tags.tagspost': {
            'Meta': {'object_name': 'TagsPost'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['discussion.Post']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tags.Tag']"})
        },
        'tags.tagsuser': {
            'Meta': {'object_name': 'TagsUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tags.Tag']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['account']