from django import forms
from django_ui_forms.utils.constants import FormsClassConstants


class BootstrapBaseUiForms:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            self.__update_attr__(field=field)

    @staticmethod
    def __update_attr__(field):
        field_type = field.widget.__class__.__name__
        if field_type == FormsClassConstants.CHECKBOX_INPUT.value:
            field.widget.attrs.update(
                {"class": FormsClassConstants.CHECKBOX_CLASS.value}
            )
        elif (
            field_type == FormsClassConstants.SELECT.value
            or field_type == FormsClassConstants.SELECT_MULTIPLE.value
        ):
            field.widget.attrs.update({"class": FormsClassConstants.FORM_SELECT.value})
        else:
            field.widget.attrs.update({"class": FormsClassConstants.FORM_CONTROL.value})
        field.widget.attrs.update({"placeholder": field.label})


class TailwindBaseUiForms:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            self.__update_attr__(field=field)

    @staticmethod
    def __update_attr__(field):
        field_type = field.widget.__class__.__name__
        if field_type == FormsClassConstants.CHECKBOX_INPUT.value:
            field.widget.attrs.update(
                {
                    "class": FormsClassConstants.TAILWIND_CHECKBOX_CLASS.value,
                }
            )
        elif (
            field_type == FormsClassConstants.SELECT.value
            or field_type == FormsClassConstants.SELECT_MULTIPLE.value
        ):
            field.widget.attrs.update(
                {
                    "class": FormsClassConstants.TAILWIND_SELECT_CLASS.value,
                }
            )
        else:
            field.widget.attrs.update(
                {
                    "class": FormsClassConstants.TAINWIND_BASE_CLASS.value,
                }
            )
        field.widget.attrs.update({"placeholder": ""})
