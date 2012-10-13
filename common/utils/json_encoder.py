# -*- coding:utf-8 -*-
# ------------------------------------------------------------------------------
from django.db.models import Model
from django.db.models.query import QuerySet
from django.utils.functional import Promise
from django.utils.translation import force_unicode
from django.utils.encoding import smart_unicode
from django.core.serializers.json import DjangoJSONEncoder

# ------------------------------------------------------------------------------
import types

class ModelJSONEncoder(DjangoJSONEncoder):
    fields = None

    def __init__(self, fields=None, *args, **kwargs):
        self.fields = fields
        super(ModelJSONEncoder, self).__init__(*args, **kwargs)

    """
    (simplejson) DjangoJSONEncoder subclass that knows how to encode fields.

    (adated from django.serializers, which, strangely, didn't
     factor out this part of the algorithm)
    """
    def handle_field(self, obj, field):
        return smart_unicode(getattr(obj, field.name), strings_only=True)

    def handle_fk_field(self, obj, field):
        related = getattr(obj, field.name)
        if related is not None:
            if field.rel.field_name == related._meta.pk.name:
                # Related to remote object via primary key
                related = related._get_pk_val()
            else:
                # Related to remote object via other field
                related = getattr(related, field.rel.field_name)
        return smart_unicode(related, strings_only=True)

    def handle_m2m_field(self, obj, field):
        if field.creates_table:
            return [
                smart_unicode(related._get_pk_val(), strings_only=True)
                for related
                in getattr(obj, field.name).iterator()
                ]


    def handle_list(self, obj_list):
        ret = []
        for obj in obj_list:
            ret.append(self.default(obj))
        return ret

    def handle_dict(self, dict):
        ret = {}
        for k,v in dict.items():
            ret[k] = self.default(v)
        return ret

    def handle_model(self, obj):
        dic = {}
        for field in obj._meta.local_fields:
            if self.fields is not None:
                if field.name not in self.fields:
                    continue
            if field.serialize or field.name in self.fields:
                if field.rel is None:
                    dic[field.name] = self.handle_field(obj, field)
                else:
                    dic[field.name] = self.handle_fk_field(obj, field)
        for field in obj._meta.many_to_many:
            if field.serialize:
                dic[field.name] = self.handle_m2m_field(obj, field)
        return dic

    def default(self, obj):
        if isinstance(obj, Model):
            return self.handle_model(obj)
        elif type(obj) is types.ListType or isinstance(obj, QuerySet):
            return self.handle_list(obj)
        elif type(obj) is types.DictType:
            self.handle_dict(obj)
        else:
            return super(ModelJSONEncoder, self).default(obj)

# ------------------------------------------------------------------------------
class LazyEncoder(ModelJSONEncoder):
    def default(self, o):
        if isinstance(o, Promise):
            return force_unicode(o)
        else:
            return super(LazyEncoder, self).default(o)