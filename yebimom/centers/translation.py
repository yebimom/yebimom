from modeltranslation.translator import translator, TranslationOptions
from centers.models.center import Center


class CenterTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Center, CenterTranslationOptions)
