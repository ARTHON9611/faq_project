from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)

    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def translate_text(self, text, lang):
        """Translate text dynamically and cache results"""
        cache_key = f"faq_translation_{self.id}_{lang}"
        cached_translation = cache.get(cache_key)
        
        if cached_translation:
            return cached_translation

        translated_text = translator.translate(text, dest=lang).text
        cache.set(cache_key, translated_text, timeout=86400)  # Cache for 1 day
        return translated_text

    def get_translation(self, lang):
        if lang == 'hi':
            return {
                'question': self.question_hi or self.translate_text(self.question, 'hi'),
                'answer': self.answer_hi or self.translate_text(self.answer, 'hi')
            }
        elif lang == 'bn':
            return {
                'question': self.question_bn or self.translate_text(self.question, 'bn'),
                'answer': self.answer_bn or self.translate_text(self.answer, 'bn')
            }
        return {'question': self.question, 'answer': self.answer}

    def save(self, *args, **kwargs):
        """Auto-translate FAQs during creation"""
        if not self.question_hi:
            self.question_hi = self.translate_text(self.question, 'hi')
        if not self.answer_hi:
            self.answer_hi = self.translate_text(self.answer, 'hi')
        if not self.question_bn:
            self.question_bn = self.translate_text(self.question, 'bn')
        if not self.answer_bn:
            self.answer_bn = self.translate_text(self.answer, 'bn')
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.question
