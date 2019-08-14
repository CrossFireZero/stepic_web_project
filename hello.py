def hello(env, start_response):
    '''
    Simple WSGI app
    '''
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]

    for item in env.items():
        print(item)

    start_response(status, headers)

    return body
