from app import create_app,db
from app.models import Admin,Patient,Doctor,Talks,Doctor_details
from  flask_migrate import Migrate, MigrateCommand
from flask_socketio import SocketIO,emit



from flask_script import Manager,Server
# from app.models import User, Role, Comment,Pitch

#creating an app instance  
app = create_app('development')  
socketio = SocketIO(app)

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,Admin=Admin,Patient=Patient,Doctor=Doctor,Talks=Talks,Doctor_details=Doctor_details   )

@socketio.on('my event')
def handle_my_custom_event( json ):
    print("recived somthng" + str(json))
    socketio.emit('my response', json )

if __name__ == '__main__':
    socketio.run(app)