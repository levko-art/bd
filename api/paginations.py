from rest_framework.pagination import CursorPagination


class TransactionPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    ordering = '-created_at'


class TaskPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    ordering = '-created_at'
