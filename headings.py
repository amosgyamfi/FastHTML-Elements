from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Div(
        H1('This is Heading 1'),
        H2('This is Heading 2'),
        H3('This is Heading 3'),
        H4('This is Heading 4'),
        H5('This is Heading 5'),
        H6('This is Heading 6'),
        Hr(),
        Hgroup(
            H2('Get inspired with CSS'),
            P('How to use CSS to add glam to your Website?')
        )
    )

serve()