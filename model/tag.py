from peewee import *
from database import db

class Tag(Model):
	__tablename__ = 'tags'
	
	name = CharField(unique=True)
	
	_items = None
	
	@staticmethod
	def get_tag(value):
		if Tag._items == None:
			Tag._items = {}
			tags = Tag.select()
			for tag in tags:
				Tag._items[tag.name] = tag
		
		if Tag._items.has_key(value):
			return Tag._items[value]
		else:
			tag = Tag(name = value)
			Tag._items[value] = tag
			tag.save()
			return tag

	class Meta:
		database = db
