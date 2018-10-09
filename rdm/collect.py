from collections import defaultdict


def collect_snippets(lines, start_regex='RDOC', stop_regex='ENDRDOC'):
    rdoc_key = None
    rdoc_offset = None
    rdocs = defaultdict(list)
    for line in lines:
        if rdoc_key is None:
            start_token_offset = line.find(start_token)
            if start_token_offset != -1:
                rdoc_offset = start_token_offset
                rdoc_key = line[rdoc_offset + len(start_token):].strip()
                if rdoc_key == '':
                    raise ValueError('Empty snippet key on line:\n' + line)
                elif rdoc_key in rdocs:
                    msg = 'Multiple snippets with the key: "{}"'.format(rdoc_key)
                    raise ValueError(msg)
        else:
            stop_token_offset = line.find(stop_token)
            if stop_token_offset == rdoc_offset:
                rdoc_key = None
                rdoc_offset = None
            elif stop_token_offset != -1:
                msg = "End snippet offset doesn't match the start snippet offset on line:\n" + line
                raise ValueError(msg)
            else:
                rdocs[rdoc_key].append(line[rdoc_offset:])
    if rdoc_key is not None:
        raise ValueError('Missing a closing snippet token on line:\n' + line)
    return {k: ''.join(v) for k, v in rdocs.items()}
