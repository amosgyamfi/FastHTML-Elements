from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Div(
        H1('Inline Text Elements'),
        P(
            'This is an abbreviation:',
            Abbr('HTML', title='Hypertext Markup Language')
        ),
        P(
            'This is bold text using',
            Strong('strong'),
            'and',
            B('b'),
            'tags'
        ),
        P(
            'This is italic text using',
            I('i'),
            ',',
            Em('em'),
            ', and',
            Cite('cite'),
            'tags'
        ),
        P(
            'This is',
            Del('deleted text')
        ),
        P(
            'This is',
            Ins('inserted text')
        ),
        P(
            'To save your document, press',
            Kbd('Ctrl + S')
        ),
        P(
            'This is',
            Mark('highlighted text')
        ),
        P(
            'This is',
            S('strikethrough text')
        ),
        P(
            'This is',
            Small('small text')
        ),
        P(
            'This is text with a subscript: H',
            Sub('2'),
            'O'
        ),
        P(
            'This is text with a superscript: E = mc',
            Sup('2')
        ),
        P(
            'This is',
            U('underlined text')
        )
    )

serve()