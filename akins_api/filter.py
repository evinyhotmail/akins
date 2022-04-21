from rest_framework import filters


class DynamicDroneFilter(filters.SearchFilter):

    # overriding the method get_search_fields in order to be able
    # to the user can managment dinamic fields-
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


class DynamicCameraFilter(filters.SearchFilter):

    # overriding the method get_search_fields in order to be able
    # to the user can managment dinamic fields-
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
