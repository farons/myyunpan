# -*- coding:UTF-8 -*-
# manage.py
# @author yanzhilong
# @description 启动app
# @created 20190425
from flask_script import Manager,Server
from flask_migrate import MigrateCommand

from app import create_app


app = create_app('backup')
manager = Manager(app)
manager.add_command('runserver', Server(host=app.config['SERVER_HOST'], 
                                        port=app.config['SERVER_PORT'],
                                        use_debugger=app.config['DEBUG']),
                                        threaded=True)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
