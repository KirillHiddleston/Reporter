<div align="center">
<a href="">
  <img width="450" height="100" src="title.png">
<a href="">
<h3>Whole stuff for the model document report process</h4>
</div>

----
# Reporter

<div align="center">
<h3>Document </h3>
</div>

----
- [Description](#overview)
- [Install](#install)
- [Templates](#configs)
- [Use](#usage)
  - [filling report](#report)
  - [make_report](#make_template)
  - [description_template](#templates)
- [Changes (CHANGELOG)](./CHANGELOG.md)
----

<h2 id="overview">Description</h2>

reporter — is a tool for generating reports for ml training or ect.
Base on jinja2.


<h2 id="install">Install</h2>

```bash
pip install reporter 
```

<h2 id="configs">Templates</h2>
A template is a markdown “.md” format file, pre-labeled with jinja2 tags for further filling them in

Example:
```markdown
# {{ title }}

## Model
- model name - `{{ mleco_model_name }}`
- ID training = {{ mleco_training_id }}

## Contacts
- Telegram: [{{ contact_telegram }}](https://t.me/{{ contact_telegram }})
- Email: {{ contact_email }}
```


<h2 id="usage">Use</h2>
<h3 id="report">Filling report</h3>
To fill reports with so-called “context” you can use yaml/json or dict.
Where the key is the tag in the markdown template, the destination is the information that will be added to the report

Example:
``` yaml
# YAML
contacts:
  telegram: @name
  email: name@yandex.ru
```

``` dict
{"contacts": [
  "telegram": "@name",
  "email": "name@yandex.ru",
 ]}
```

Initialize Reporter

```python
from reporter import Reporter

# Initialize
# select the desired template
report = Reporter(
  templ_path='smart_vision/fieldnet.md',  # paths inside the lib to the template
  package_name='reporter',  # name pckg
  env_path='templates'  # dir withs templates
)
# filling report base yaml
report.report_config_content(
  context='path/config_test.yml',
  output_path='test_yaml.md',
)
# filling report base dict
report.report__content(
  context={'title': 'fieldnet report'},
  output_path='test_yaml.md',
)
```
- `templ_path` is the path to the template files for the report.
- `env_path` is the path to the dir with templates.
- `context` is the path to the file with the context to populate the template.
- `output_path` is the path to save the file, the format for saving the report is docx/pdf/md.

Templates are stored in the following path
```python
template_path = "/reporter/templates/"
```
```
templates/
    ├──base/
    │    ├──base.md
    │    ├──title.md
    │    ├──reproduce.md
    │    └──table.md
    ├──smart_vision/
    │    ├──fieldnet.md
    │    ├──rotator.md
    │    └──ocr_general.md
    └── 
```

<h3 id="make_template">Make template</h3>

To create a custom markdown template, it must be marked up using the jinja2 syntax
https://jinja.palletsprojects.com/en/3.1.x/templates/#base-template

Plus to the documentation above:
it is better to write tags by construction "| default('my_variable is not defined')"
```markdown
# example use tag in template
{{ contacts['telegram']|default('my_variable is not defined') }}
# this way we will not get an error when filling the template if this tag is not in the config.
```
If you need to parse a list to populate it in a template, not as a row, but as a 'column'

```python
classes = ['class1', 'class2']
```
```markdown
{% for class in classes %}
    {{ class }}
{% endfor %}

# output
class1
class2
```
If we use the yaml format to fill the report, then we need to use the key reference in the template
```markdown
{{ contacts['telegram'] }}
```
Example template for use with yaml
```markdown
# {{ title['title_report'] }}

## Model
- Model name - {{ title['mleco_model_name'] }}
- ID training = {{ title['mleco_training_id'] }}

## Contacts
- Telegram: [{{ title['contact_telegram'] }}](https://t.me/{{ title['contact_telegram'] }})
- email: {{ title['contact_email'] }}
```
Processing pandas DataFrame:
If you want to process a DataFrame, and add it to the template as a table, you need to add a tag for the dataframe.

Example:
```markdown
{{ table }} # tag in template
```
```python
data_table = pd.DataFrame({'User': ['Charlie', 'Dana'], 'Score': [8.7, 9.3]})
context = {'table':data_table}
```

After creating a template, it should be added to the `reporter/templates` directory - the path to the templates

<h3 id="templates">Description template</h3>
The current template structure is the “base template” and inheritance from it.
The base template of Jinja2, base.md, which includes various content blocks and is used to create other templates.
In turn, the “daughter” templates - fill empty blocks {% block ... %} with content:

base.md:
```markdown
{% include 'base/title.md' %}
{% include 'base/reproduce.md' %}
{% include 'base/table.md' %}
```
```
## Goals and objectives of the model
{% block model_goals %}
- goals and objectives;
- explicit definition of business indicators that will change as a result of applying the model in the business process defined below;
- a description of the expected mechanism of the model's impact on business indicators
{% endblock model_goals %}
...

```
where the '% include' tag is responsible for including the template in the base template.

Inheritance:
In the child template, the tag {% extends ... %} is the key tag. It tells the template engine that this template “extends” another template. When the Jinja2 template engine evaluates this template, it first finds the parent. The extends tag should be the first tag in the template.

**Example**:
```markdown
{% extends 'base.md' %} # base.md

{% block model_goals %} # inclusion of a special content block

# Anything below is already basic content to be filled in
This is part of the document recognition pipelines, where the model must find and classify a 
a set of the following field types:

{{ classes }}

The task of the model is to accurately and quickly segment these fields in photographs 
and scans of a document.

### Explicit definition of the business metrics that will change as a result of applying the model to a specific business process.
Key business indicators that will change:
...
```
You can also see a visual example of inheritance in the template fieldnet ```reporter/templates/smart_vision/fieldnet.md```
Additional documentation on inheritance
https://docs-python.ru/packages/modul-jinja2-python/nasledovanie-shablonov-jinja2/