CONFIG = {                                                                                                                                                              
    'mode': 'wsgi',                                                                                                                                                   
    'working_dir': '/home/box/web/',                                                                                                                                   
    'python': '/usr/bin/python', 
    #pythonpath="path"
    'args': (                                                                                                                                                           
        '--bind=0.0.0.0:8080',                                                                                                                                      
        '--workers=16',                                                                                                                                                 
        '--timeout=60',                                                                                                                                                 
        'app.module',                                                                                                                                                   
    ),                                                                                                                                                                  
}     
