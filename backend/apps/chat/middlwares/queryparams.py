from urllib.parse import parse_qs

from channels.middleware import BaseMiddleware


class QueryParamsMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        scope = dict(scope)

        scope['query_params'] = parse_qs(scope['query_string'].decode())

        return await super().__call__(scope, receive, send)
