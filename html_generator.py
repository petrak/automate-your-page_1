
def generate_concept_HTML(concept_title, concept_description):
# function generate_concept_html generates the HTML code for input title and description
# Function is a peace of code, that execute  certain functionality. When it is done, the developer can just use it 
# (execute it from other points of the program) and forget all the details about it (so he can focus on other things in the code). 
# It is written that the code is note repeated (is written only once). So the code is easy to read and change. 
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
# function make_HTML separates the title and description into different strings and gets output of function generate_concept_HTML (= HTML code)
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['Python', 'Python is a Programming Language'],
                             ['For Loop', 'For Loops allow you to iterate over lists'],
                             ['Lists', 'Lists are sequences of data'] ]


def make_HTML_for_many_concepts(list_of_concepts):
# function make_HTML_for_many_concepts for each sublist in list EXAMPLE_LIST_OF_CONCEPTS (=concept) executes function make_HTML and add output of function
# to output its own function (= HTML)
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

# execute function make_HTML_for_many_concepts (one execution of funcition)
# input for function is EXAMPLE_LIST_OF_CONCEPTS which includes many lists. Each list consists of 2 elements: elemant position 1 is title and element position 2 description
print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
