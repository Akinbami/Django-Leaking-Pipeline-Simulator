from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)

class PipelineLimitOffsetPagination(LimitOffsetPagination):
	default_limit = 2
	max_limit = 10


class PipelinePageNumberPagination(PageNumberPagination):
	page_size = 10
