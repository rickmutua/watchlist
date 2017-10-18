from app import create_app
from flask_script import Manager, Server

app = create_app('development')

manager = Manager(app)

manager.add_command('server',Server)


@manager.command
def test():
    '''
    run unittest
    :return:
    '''

    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


manager = Manager(app)
if __name__ == '__main__':
    manager.run()