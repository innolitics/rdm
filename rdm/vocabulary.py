from jinja2.ext import Extension
from jinja2.lexer import TOKEN_EOF


class VocabularyExtension(Extension):
    tags = set(['vocabulary'])

    def parse(self, parser):
        next(parser.stream) # skip past tag token

        # Parse, examine, and save remaining tokens
        tokens = []
        while parser.stream:
            token = next(parser.stream)
            examined_token = self.examine_token(token)
            if examined_token:
                tokens.append(token)

        # Make sure last token is end of file token
        eof_token = parser.stream.current
        tokens.append(eof_token)

        # Push the tokens back into the stream
        for token in tokens:
            parser.stream.push(token)

        # Pull first pushed token to be current token. Should be 'block_end' token.
        next(parser.stream)

        # Return empty list: no nodes have been generated.
        return []

    def examine_token(self, token):
        return token