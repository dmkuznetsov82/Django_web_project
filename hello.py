import urlparse
def application(env, start_response):
    params = urlparse.parse_qs(env['QUERY_STRING'])
    body = ""
    for key,value in params.items():
        body = body + str(key)+"="+str(value)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [body]   
