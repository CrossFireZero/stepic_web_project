def hello(env, start_response):
    '''
    Simple WSGI app
    '''
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    body = '\n'.join(env['QUERY_STRING'].split('&'))
    print(body)
    body = bytes(body, encoding='utf-8')
    print(body)
    start_response(status, headers)

    return [body]
