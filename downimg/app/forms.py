from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
import os


# def check_if_int(value):
#     if type(value) is not int:
#         raise ValidationError(
#             '%(value)s is a number',
#             params = {'value': value},
#         )

class KeyVForm(forms.Form):
    first_key_column = forms.CharField(label = 'First Key Column:',
                                       widget = forms.TextInput(attrs = {'class': 'form-control'}))
    last_value_column = forms.CharField(label = 'Last Value Column:',
                                        widget = forms.TextInput(attrs = {'class': 'form-control'}))
    first_empty_column = forms.CharField(label = 'First Empty Column',
                                         widget = forms.TextInput(attrs = {'class': 'form-control'}))
    d_file = forms.FileField(label = 'Excel File:')
    
    def clean(self):
        all_clean_data = super(KeyVForm, self).clean()
        
        f_key_column = int(all_clean_data['first_key_column']) if all_clean_data[
            'first_key_column'].isnumeric() else None
        l_value_column = int(all_clean_data['last_value_column']) if all_clean_data[
            'last_value_column'].isnumeric() else None
        f_empty_column = int(all_clean_data['first_empty_column']) if all_clean_data[
            'first_empty_column'].isnumeric() else None
        
        if f_key_column is None:
            self.add_error('first_key_column', 'First-Key-Column needs to be number greater than 0.')
        else:
            if f_key_column == 0:
                self.add_error('first_key_column', 'First-Key-Column needs to be number greater than 0.')
            if l_value_column is not None:
                if not (l_value_column > f_key_column):
                    self.add_error('first_key_column',
                                   'First-Key-Column needs to be a grater number than Last-Value-Column.')
                    self.add_error('last_value_column',
                                   'First-Key-Column needs to be a grater number than Last-Value-Column.')
        if l_value_column is None:
            self.add_error('last_value_column', 'Last-Value-Column needs to be number greater than 0.')
        else:
            if l_value_column == 0:
                self.add_error('last_value_column', 'Last-Value-Column needs to be number greater than 0.')
            if f_empty_column is not None:
                if not (f_empty_column > l_value_column):
                    self.add_error('first_empty_column',
                                   'First-Empty-Column needs to be a grater number than Last-Value-Column ')
                    self.add_error('last_value_column',
                                   'First-Key-Column needs to be a grater number than Last-Value-Column.')
        
        if f_empty_column is None:
            self.add_error('first_empty_column', 'First-Empty-Column needs to be number greater than 0.')
        else:
            if f_empty_column == 0:
                self.add_error('first_empty_column', 'First-Empty-Column needs to be number greater than 0.')
        
        xl_file = all_clean_data["d_file"]
        extension = os.path.splitext(xl_file.name)[1]
        VALID_EXTENSION = '.xlsx'
        if extension.lower() != VALID_EXTENSION:
            self.add_error('d_file', 'The file has to be .XLSX')


class SplitForm(forms.Form):
    split_value = forms.CharField(label = 'Number of rows to split by:',
                                  widget = forms.TextInput(attrs = {'class': 'form-control'}))
    d_file = forms.FileField(label = 'Excel File:')
    
    def clean(self):
        all_clean_data = super(SplitForm, self).clean()
        
        if all_clean_data['split_value'].isnumeric() is False:
            self.add_error('split_value', 'The split value has to be number')
        else:
            if int(all_clean_data['split_value']) <= 1:
                self.add_error('split_value', 'The split value has to be grater than 1 (2 or grater)')
        
        xl_file = all_clean_data["d_file"]
        extension = os.path.splitext(xl_file.name)[1]
        VALID_EXTENSION = '.xlsx'
        
        if extension.lower() != VALID_EXTENSION:
            self.add_error('d_file', 'The file has to be .XLSX')
        
        return all_clean_data


class UploadForm(forms.Form):
    url_cell_start = forms.CharField(label = 'First column with URLs (numeric):',
                                     widget = forms.TextInput(attrs = {'class': 'form-control'}))
    
    url_cell_end = forms.CharField(label = 'Last column with URLs (numeric):',
                                   widget = forms.TextInput(attrs = {'class': 'form-control'}))
    write_cell_start = forms.CharField(label = 'First column to write image files (numeric):',
                                       widget = forms.TextInput(attrs = {'class': 'form-control'}))
    write_cell_end = forms.CharField(label = 'Last column to write image file (numeric):',
                                     widget = forms.TextInput(attrs = {'class': 'form-control'}))
    d_file = forms.FileField(label = 'Excel File:')
    
    def clean(self):
        all_clean_data = super(UploadForm, self).clean()
        
        url_c_start = int(all_clean_data['url_cell_start']) if all_clean_data['url_cell_start'].isnumeric() else None
        url_c_end = int(all_clean_data['url_cell_end']) if all_clean_data['url_cell_end'].isnumeric() else None
        write_c_start = int(all_clean_data['write_cell_start']) if all_clean_data[
            'write_cell_start'].isnumeric() else None
        write_c_end = int(all_clean_data['write_cell_end']) if all_clean_data['write_cell_end'].isnumeric() else None
        xl_file = all_clean_data["d_file"]
        extension = os.path.splitext(xl_file.name)[1]
        VALID_EXTENSION = '.xlsx'
        
        if url_c_start is None:
            self.add_error('url_cell_start', 'The URL Start column needs to be a number.')
        else:
            if not (url_c_start > 0):
                self.add_error('url_cell_start', 'The URL Start column needs to be a number grater than zero.')
        
        if url_c_end is None:
            self.add_error('url_cell_end', 'The URL End column needs to be a number.')
        else:
            if not (url_c_end > 0):
                self.add_error('url_cell_end', 'The URL End column needs to be a number grater than zero.')
            else:
                if url_c_start is not None:
                    if not (url_c_start <= url_c_end):
                        self.add_error('url_cell_end',
                                       'The URL-End column need to be a number grater or equal than URL Start')
        
        if write_c_start is None:
            self.add_error('write_cell_start', 'The URL column needs to be a number.')
        else:
            if not (write_c_start > 0):
                self.add_error('write_cell_start', 'The URL column needs to be a number grater than zero.')
            else:
                if url_c_end is not None:
                    if url_c_end > write_c_start:
                        self.add_error('write_cell_start',
                                       'The URL-Write-start column number needs to be a number grater than URL-cell-end')
        
        if write_c_end is None:
            self.add_error('write_cell_end', 'The URL column needs to be a number.')
        else:
            if not (write_c_end > 0):
                self.add_error('write_cell_end', 'The URL column needs to be a number grater than zero.')
            
            else:
                if write_c_start is not None:
                    if not (write_c_start <= write_c_end):
                        self.add_error('write_cell_end',
                                       'The URL-Write-end column number needs'
                                       ' to be a number grater or equal than URL-Write-start')
        
        if extension.lower() != VALID_EXTENSION:
            self.add_error('d_file', 'The file has to be .XLSX')
        
        return all_clean_data
