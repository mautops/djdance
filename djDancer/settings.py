import os

RUN_ENV = os.environ.get('RUN_ENV', 'DEVELOP')

if RUN_ENV == 'DEVELOP':
    from configs.develop import *   # noqa
elif RUN_ENV == 'PRODUCT':
    from configs.product import *   # noqa
else:
    from configs.develop import *   # noqa

DEFAULT_CHARSET = 'utf-8'
USE_TZ = True
