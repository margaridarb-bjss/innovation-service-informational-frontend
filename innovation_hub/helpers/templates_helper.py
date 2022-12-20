import re

from django.utils.text import slugify


def add_heading_elements_id(html, heading_levels_regexp=r'1-6'):

    return re.sub(rf'<h([{heading_levels_regexp}])([^>]*)>((\n|.)+?)</h\1>', __add_heading_elements_id, html)


def heading_elements_ids_list(html, heading_levels_regexp=r'1-6'):

    matches = re.findall(
        rf'<h([{heading_levels_regexp}])([^>]*)>((\n|.)+?)</h\1>',
        html)

    return list(map(lambda x: {'label': x[2], 'slug': slugify(x[2])}, matches))


def __add_heading_elements_id(match):
    """
        This is a regexp replacement function that takes
        in the above regex match results, and then turns:
            <h1>some text</h1>
        Into:
            <h1><a id="some-text"></a><a href="#some-text">some text</a></h1>
        where the id attribute value is generated by running
        the heading text through Django's slugify() function.
        """
    element_h_number = match.group(1)
    element_attributes = match.group(2)
    element_content = match.group(3)
    element_id = slugify(element_content)

    return f'<h{element_h_number} id="{element_id}"{element_attributes}>{ element_content }</h{element_h_number}>'
