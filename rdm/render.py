import os

import jinja2
import jinja2.ext
import yaml


def render_template(template_filename, data_filenames, output_file):
    environment = construct_environment()
    template = environment.get_template(template_filename)
    context = context_from_data_files(data_filenames)
    template.stream(**context).dump(output_file)


class FrontMatterExtension(jinja2.ext.Extension):
    def __init__(self, environment):
        environment._document_contexts = {}
        super().__init__(environment)
        
    def preprocess(self, raw_source, name, filename=None):
        source, document_data = extract_document_data(raw_source)
        print(document_data, name)
        if name not in self.environment._document_contexts:
            self.environment._document_contexts[name] = document_data
        else:
            raise ValueError('"{}" template has already been preprocessed'.format(name))
        return super().preprocess(source, name, filename)


class TemplateWithDocumentContext(jinja2.Template):
    '''
    Custom Jinja2 template class that keeps track of document data embedded as
    YAML front matter, similar to how Jekyll does it, except that we allow for
    multiple inheritance of templates.
    '''
    def _merge_document_data(self, context):
        document_data = self.environment._document_contexts[self.name]
        print(self.name, document_data)
        if document_data is not None:
            if "document" in context:
                context["document"].update(document_data.copy())
            else:
                context["document"] = document_data.copy()

    def render(self, *args, **kwargs):
        self._merge_document_data(kwargs)
        return super().render(*args, **kwargs)

    def generate(self, *args, **kwargs):
        self._merge_document_data(kwargs)
        return super().generate(*args, **kwargs)


def construct_environment():
    environment = jinja2.Environment(
        undefined=jinja2.StrictUndefined,
        extensions=[FrontMatterExtension]
    )
    environment.template_class = TemplateWithDocumentContext
    return environment


def context_from_data_files(data_filenames):
    context = {}
    for data_filename in data_filenames:
        key, _ = os.path.splitext(os.path.basename(data_filename))
        if key in context:
            raise ValueError('There is already data attached to the key "{}"'.format(key))
        with open(data_filename, 'r') as data_file:
            data_string = data_file.read()
        try:
            data = yaml.load(data_string)
        except yaml.YAMLError as e:
            raise ValueError('"{}" contains invalid YAML: {}'.format(data_filename, e))
        context[key] = data
    return context


def extract_document_data(raw_string):
    if not raw_string.startswith('---\n'):
        return raw_string, None
    parts = raw_string.split('---\n')
    if len(parts) != 3:
        raise ValueError('Invalid YAML front matter; expected a closing "---" on a newline')
    document_data_string = parts[1]
    template_string = parts[2]
    try:
        document_data = yaml.load(document_data_string)
    except yaml.YAMLError as e:
        raise ValueError('Invalid YAML front matter; improperly formatted YAML: {}'.format(e))
    return template_string, document_data
