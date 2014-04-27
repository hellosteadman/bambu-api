Settings
========

``API_AUTH_BACKEND``
	The provider used to authenticate users through the API
	(default is 'bambu_api.auth.http.HTTPAuthentication')

``API_AUTH_REALM``
    The HTTP authentication realm (default is 'Restricted access')

``API_LOGIN_URL``
    The URL to redirect anonymous API users to (defaults to the result of reversing the URL name 'login')

``API_AUTH_ALLOW_REGISTRATION``
    When ``True``, this allows users to sign up via the API thus creating an ``auth.User`` object
    (defaults to ``False``)

``API_ALLOW_USER_MANAGEMENT``
    When ``True``, allows users to edit their login details via the API (defaults to ``False``)

``API_ALLOW_GROUP_MANAGEMENT``
    When ``True``, allows authenticated users to create, read, update and delete ``auth.Group`` objects
    (defaults to ``False``)

``API_CACHE_VARY_HEADERS``
    Which HTTP  headers are used to decide whether to cache content or not. Defaults to 'Cookie'

``API_THROTTLE_REQUESTS``
    The number of requests permitted in X minutes (where X is the value of ``API_THROTTLE_MINUTES``).
    The default is 60.

``API_THROTTLE_MINUTES``
    The number of minutes that defines how many requests to allow before throttling. The default
    is 1.

``API_REQUEST_LOGGER``
    The default request logger to use (the means by which throttling occurs). Specify the fully
    qualified module and class name of the logger. Defaults to
    'bambu_api.requestlogging.DatabaseRequestLogger'

Redis-specific settings
-----------------------

If using Redis to log the number of requests by a specific app for throttling, you can configure Bambu
API to use a specific host and database
    
``API_REDIS_HOST``
    The Redis host to use (defaults to 'localhost')

``API_REDIS_PORT``
    The Redis port to use (defaults to 6379)

``API_REDIS_DB``
    The index of the Redis database to use (defaults to 0)

``API_REDIS_PASSWORD``
    The password for the Redis database (defaults to '')