from django.db import models

class Task( models.Model ):
	"""
	Model for storing `tasks`
	"""

	# Whether this task is completed
	completed = models.BooleanField( default = False )

	# Task title
	title = models.CharField( max_length = 100 )
