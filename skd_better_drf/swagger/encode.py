from collections import OrderedDict
from coreapi.compat import urlparse
from openapi_codec.utils import get_method, get_encoding, get_links_from_document


class AbstractCodec:
    def _generate_swagger_object(self, document):
        parsed_url = urlparse.urlparse(document.url)

        swagger = OrderedDict()

        swagger['swagger'] = '2.0'
        swagger['info'] = OrderedDict()
        swagger['info']['title'] = document.title
        swagger['info']['version'] = ''  # Required by the spec

        if parsed_url.netloc:
            swagger['host'] = parsed_url.netloc
        if parsed_url.scheme:
            swagger['schemes'] = [parsed_url.scheme]

        swagger['paths'] = self._get_paths_object(document)

        return swagger

    def _get_paths_object(self, document):
        paths = OrderedDict()

        links = self._get_links(document)

        for operation_id, link, tags in links:
            if link.url not in paths:
                paths[link.url] = OrderedDict()

            method = get_method(link)
            operation = self._get_operation(operation_id, link, tags)
            paths[link.url].update({method: operation})

        return paths

    def _get_operation(self, operation_id, link, tags):
        encoding = get_encoding(link)
        description = link.description.strip()
        summary = description.splitlines()[0] if description else None

        operation = {
            'operationId': operation_id,
            'responses': self._get_responses(link),
            'parameters': self._get_parameters(link, encoding)
        }

        if description:
            operation['description'] = description
        if summary:
            operation['summary'] = summary
        if encoding:
            operation['consumes'] = [encoding]
        if tags:
            operation['tags'] = tags
        return operation

    def _get_responses(self, link):
        if isinstance(link._responses_docs, dict):
            return link._responses_docs.get(
                '{}'.format(link.action),
                link._responses_docs
            )

    def _get_parameters(self, link, encoding):
        if isinstance(link._parameters_docs, dict):
            parameters_doc = link._parameters_docs.get(
                '{}'.format(link.action), None)
        else:
            parameters_doc = None
        if parameters_doc is not None:
            params = []
            for prameter in parameters_doc:
                params.append(prameter)
            return params

    def _get_links(self, document):
        """
        Return a list of (operation_id, link, [tags])
        """
        # Extract all the links from the first or second level of the document.
        links = []
        for keys, link in get_links_from_document(document):
            if len(keys) > 1:
                operation_id = '_'.join(keys[1:])
                tags = [keys[0]]
            else:
                operation_id = keys[0]
                tags = []
            links.append((operation_id, link, tags))

        # Determine if the operation ids each have unique names or not.
        operation_ids = [item[0] for item in links]
        unique = len(set(operation_ids)) == len(links)

        # If the operation ids are not unique, then prefix them with the tag.
        if not unique:
            return [self._add_tag_prefix(item) for item in links]

        return links

    def _add_tag_prefix(self, item):
        operation_id, link, tags = item
        if tags:
            operation_id = tags[0] + '_' + operation_id
        return (operation_id, link, tags)
