from rest_framework import serializers
from task.models import Task

class TaskSerializer( serializers.ModelSerializer ):
	"""
	Serializer to parse Task data
	"""

	class Meta:
		model = Task
		fields = ( 'title', 'completed', 'id' )