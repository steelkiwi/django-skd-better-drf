from rest_framework.schemas import SchemaGenerator


class SchemaGenerator(SchemaGenerator):
    def get_link(self, path, method, view):
        data_link = super(SchemaGenerator, self).get_link(path, method, view)

        data_link._responses_docs = self.get_response_docs(path, method, view)
        data_link._parameters_docs = self.get_parameters_docs(path, method, view)
        data_link._view_method = getattr(view, 'action', None)

        return data_link

    def get_response_docs(self, path, method, view):
        return view.responses_docs if hasattr(view, 'responses_docs') else {'200': {
            'description': 'No response docs definition found.'}
        }

    def get_parameters_docs(self, path, method, view):
        return view.parameters_docs if hasattr(view, 'parameters_docs') else None
