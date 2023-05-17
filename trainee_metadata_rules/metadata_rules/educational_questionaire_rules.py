from edc_metadata_rules import CrfRule, CrfRuleGroup, register,P
from edc_constants.constants import YES
from edc_metadata import NOT_REQUIRED, REQUIRED


app_label = 'trainee_subject'


@register()
class EducationalQuestionaireRuleGroup(CrfRuleGroup):

    working = CrfRule(
        predicate = P('working','eq',YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models = [f'{app_label}.communityengagement']
    )


    class Meta:
        app_label = app_label
        source_model = f'{app_label}.educationalquestionaire'
