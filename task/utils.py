def context_proc(request):
    from django.conf import settings
    return {'settings': settings }

class SqlRequests(object):
    def process_response(self, request, response):
        import re
        from django.db import connection
        queries = connection.queries
        query_time = 0
        query_count = 0
        for query in queries:
            query_time += float(query['time'])
            query_count += int(1)
            
        res = '<p align="center">Query time: ' + str(query_time) + '<br />Query count: ' + str(query_count) + '</p>\n</body>'    
        response.content = response.content.replace('</body>', res)
        return response