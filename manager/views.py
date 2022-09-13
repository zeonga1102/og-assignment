from django.db.models import Avg, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status, permissions

from artist.models import Artist
from artist.models import Status

from artist.serializers import ArtistSerializer


class DashboardView(APIView):
    permission_classes = [permissions.IsAdminUser]

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "manager/dashboard.html"

    def get(self, request):
        """
        관리자 페이지의 대시보드를 보여줍니다.
        is_dashboard는 현재 보고있는 페이지가 대시보드라고 나타내는 플래그 용도로,
        현재 페이지에서 사용하지 않는 링크를 생성하지 않기 위해 전송합니다.
        """
        return Response({"is_dashboard": True}, status=status.HTTP_200_OK)


class RegisterListView(APIView):
    permission_classes = [permissions.IsAdminUser]

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "manager/register_list.html"

    def get(self, request):
        """
        작가 등록 신청자들의 목록을 보여줍니다.
        만약 검색을 한 것이라면 검색 결과를 보여줍니다.
        """
        keyword = request.GET.get("keyword", None)
        if keyword:
            artist_data = Artist.objects.filter(name__icontains=keyword).order_by("-signup_date")
        else:
            artist_data = Artist.objects.all().order_by("-signup_date")
        serialized_artist_data = ArtistSerializer(artist_data, many=True).data
        return Response({"artists": serialized_artist_data}, status=status.HTTP_200_OK)

    def put(self, request, new_status):
        """
        작가 등록 신청자들의 status를 변경합니다.
        new_status가 1이면 승인, 3이면 반려입니다.
        현재 대기 중인 상태의 신청자만 수정합니다.
        """
        artist_data = Artist.objects.select_related("status").filter(id__in=request.data.get("selectedArtists", None), status_id=2)

        try:
            new_status_data = Status.objects.get(id=new_status)
        except Status.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        for ad in artist_data:
            ad.status = new_status_data
            ad.save()

        return Response(status=status.HTTP_200_OK)


class StatisticsView(APIView):
    permission_classes = [permissions.IsAdminUser]

    renderer_classes = [TemplateHTMLRenderer]
    template_name = "manager/statistics.html"

    def get(self, request):
        """
        작가들의 통계를 보여줍니다.
        100호 이하 작품 수를 nuber_of_lte_100이라는 키값으로 하고,
        평균 가격을 avg_price라는 키값으로 하여 전송합니다.
        """
        artist_data = Artist.objects.prefetch_related("work_set").filter(status_id=1)
        for ad in artist_data:
            setattr(ad, "number_of_lte_100", ad.work_set.filter(size__lte=100).aggregate(number_of_lte_100=Count("size"))["number_of_lte_100"])
            avg_price = ad.work_set.all().aggregate(avg_price=Avg("price"))["avg_price"]
            if avg_price is None:
                avg_price = 0
            setattr(ad, "avg_price", avg_price)
        return Response({"artists": artist_data}, status=status.HTTP_200_OK)