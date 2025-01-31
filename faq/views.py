from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request):
        lang = request.GET.get('lang', 'en')
        faqs = FAQ.objects.all()
        data = [
            {
                'id': faq.id,
                'question': faq.get_translation(lang)['question'],
                'answer': faq.get_translation(lang)['answer'],
            }
            for faq in faqs
        ]
        return Response(data)
