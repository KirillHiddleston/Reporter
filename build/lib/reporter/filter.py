def to_html_filter(data_frame):
    """
    Filter for jinja2 template, converting pandas DataFrame to html
    for make table
    Args:
        data_frame: pandas dataframe

    Returns:
        html

    """
    return data_frame.to_html()
