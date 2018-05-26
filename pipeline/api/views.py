from django.db.models import Q
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	UpdateAPIView,
	)


from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from pipeline.models import Pipeline
from .serializers import (
						PipelineListSerializer,
						PipelineDetailSerializer,
						PipelineUpdateSerializer,
						)

from .pagination import PipelineLimitOffsetPagination,PipelinePageNumberPagination
from .permissions import IsOwnerOrReadOnly



# class PipelineCreateAPIView(CreateAPIView):
# 	queryset = Pipeline.objects.all()
# 	serializer_class = PipelineCreateUpdateSerializer	
# 	# permission_classes = [IsAuthenticated]
# 	# lookup_field = 'slug'

# 	def perform_create(self, serialiser):
# 		serialiser.save(user=self.request.user)


class PipelineDetailAPIView(RetrieveAPIView):
	queryset = Pipeline.objects.all()
	serializer_class = PipelineDetailSerializer	
	permission_classes = [IsAuthenticated]
	lookup_field = 'slug'


class PipelineDeleteAPIView(DestroyAPIView):
	queryset = Pipeline.objects.all()
	serializer_class = PipelineDetailSerializer	
	permission_classes = [IsOwnerOrReadOnly]
	lookup_field = 'slug'


class PipelineUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Pipeline.objects.all()
	serializer_class = PipelineUpdateSerializer	
	# permission_classes = [AllowAny]
	lookup_field = 'slug'

class PipelineListAPIView(ListAPIView):
	serializer_class = PipelineListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ["name"]
	pagination_class = PipelinePageNumberPagination #PipelineLimitOffsetPagination
	permission_classes = [AllowAny]


	def get_queryset(self, *args, **kwargs):
		# queryset_list = super(PipelineListAPIView, self).get_queryset(*args, **kwargs)
		queryset_list = Pipeline.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
					Q(name__icontains=query)|
					Q(location__icontains=query)|
					Q(user__first_name__icontains=query) |
					Q(user__last_name__icontains=query)|
					Q(is_damaged__icontains=query)
					).distinct()
		return queryset_list