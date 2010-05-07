"""
This is the application's core code.  Unless you know the "ins-and-outs" of
The Cement CLI Application Framework, you probably should not modify the 
main() function of this file.

"""

import sys
from pkg_resources import get_distribution

from cement.core.exc import CementArgumentError, CementConfigError, \
                            CementRuntimeError
from cement.core.log import get_logger
from cement.core.app_setup import lay_cement
from cement.core.configuration import ensure_api_compat
from cement.core.command import run_command

from helloworld.core.config import default_config
from helloworld.core.exc import helloworldArgumentError, helloworldConfigError, \
                                 helloworldRuntimeError

REQUIRED_CEMENT_API = '0.7-0.8:20100210'
VERSION = get_distribution('helloworld').version
BANNER = """
helloworld version %s, built on Cement (api:%s)
""" % (VERSION, REQUIRED_CEMENT_API)

def main():
    try:
        ensure_api_compat(__name__, REQUIRED_CEMENT_API)    
        lay_cement(config=default_config, banner=BANNER)
    
        log = get_logger(__name__)
        log.debug("Cement Framework Initialized!")

        if not len(sys.argv) > 1:
            sys.argv.append('default')
        
        run_command(sys.argv[1])
            
    except CementArgumentError, e:
        print("CementArgumentError > %s" % e)
        sys.exit(e.code)
    except CementConfigError, e:
        print("CementConfigError > %s" % e)
        sys.exit(e.code)
    except CementRuntimeError, e:
        print("CementRuntimeError > %s" % e)
        sys.exit(e.code)
    except helloworldArgumentError, e:
        print("helloworldArgumentError > %s" % e)
        sys.exit(e.code)
    except helloworldConfigError, e:
        print("helloworldConfigError > %s" % e)
        sys.exit(e.code)
    except helloworldRuntimeError, e:
        print("helloworldRuntimeError > %s" % e)
        sys.exit(e.code)
    sys.exit(0)
        
if __name__ == '__main__':
    main()
    