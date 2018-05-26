from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	)
# from accounts.api.serializers import UserDetailSerializer
# from comments.api.serializers import CommentSerializer
# from comments.models import Comment
from pipeline.models import Pipeline


class PipelineUpdateSerializer(ModelSerializer):
	class Meta:
		model = Pipeline
		fields = ['is_damaged','damage_grade']

pipeline_detail_url = HyperlinkedIdentityField(
	view_name = 'pipeline-api:detail',
	lookup_field = 'slug',
	)
class PipelineDetailSerializer(ModelSerializer):
	url = pipeline_detail_url
	class Meta:
		model = Pipeline
		fields = ['id','user', 'name','url','longitude','latitude','is_damaged','damage_grade','updated']

	def get_html(self, obj):
		return obj.get_markdown()


	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image

	def get_comments(self, obj):
		content_type = obj.get_content_type
		object_id = obj.id
		comment_queryset= Comment.objects.filter_by_instance(obj)
		comments = CommentSerializer(comment_queryset, many=True).data
		return comments

	# def get_url(self,obj):
	# 	return obj.get_absolute_url()


class PipelineListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name = 'pipeline-api:detail',
		lookup_field = 'slug',
		)
	# user = UserDetailSerializer(read_only=True)
	class Meta:
		model = Pipeline
		fields = ['id','user', 'name','slug','url','longitude','latitude','is_damaged','damage_grade','updated']

