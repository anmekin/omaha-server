# coding: utf8

"""
This software is licensed under the Apache 2 license, quoted below.

Copyright 2014 Crystalnix Limited

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.
"""

from django import forms
from django.forms import widgets
from django.core.files.uploadedfile import UploadedFile


from suit.widgets import LinkedSelect
from suit_redactor.widgets import RedactorWidget

from sparkle.models import SparkleVersion


__all__ = ['SparkleVersionAdminForm']


class SparkleVersionAdminForm(forms.ModelForm):
    class Meta:
        model = SparkleVersion
        exclude = []
        widgets = {
            'app': LinkedSelect,
            'release_notes': RedactorWidget(editor_options={'lang': 'en',
                                                            'minHeight': 150}),
            'file_size': widgets.TextInput(attrs=dict(disabled='disabled')),
        }

    def clean_file_size(self):
        file = self.cleaned_data["file"]
        if isinstance(file, UploadedFile):
            return file.size
        return self.initial["file_size"]
