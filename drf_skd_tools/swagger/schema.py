from rest_framework.schemas import AutoSchema

class CustomViewSchema(AutoSchema):
    """
    class get_link set data with request and responce json schema to link
    """
    def get_link(self, path, method, base_url):
        link = super().get_link(path, method, base_url)
        link._responses_docs = self.get_response_docs()
        link._parameters_docs = self.get_parameters_docs()
        link._view_method = getattr(self.view, 'action', None)
        return link


    def get_response_docs(self):
        return self.view.responses_docs if hasattr(self.view, 'responses_docs') else {'200': {
            'description': 'No response docs definition found.'}
        }

    def get_parameters_docs(self):
        return self.view.parameters_docs if hasattr(self.view, 'parameters_docs') else None


class BaseJsonSchema:
    """
    provide ability to use swagger doc from responses_docs and parameters_docs attributes
    """
    responses_docs = {}
    parameters_docs = {}
    schema = CustomViewSchema()
    
