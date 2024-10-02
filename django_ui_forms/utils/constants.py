from enum import Enum


class FormsClassConstants(Enum):
    CHECKBOX_INPUT = "CheckboxInput"
    SELECT = "Select"
    SELECT_MULTIPLE = "SelectMultiple"
    FORM_CONTROL = "form-control"
    CHECKBOX_CLASS = "form-check-input"
    FORM_SELECT = "form-select"
    TAILWIND_CHECKBOX_CLASS = (
        "w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500"
    )
    TAILWIND_SELECT_CLASS = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
    TAINWIND_BASE_CLASS = "block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-blue-600 peer"
