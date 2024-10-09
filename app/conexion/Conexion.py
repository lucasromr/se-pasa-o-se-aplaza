import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        # https://www.psycopg.org/docs/extensions.html#psycopg2.extensions.parse_dsn
        dbname = "veterinaria-db"
        password = "8686"
        user = "postgres"
        host = "127.0.0.1"
        port = 5433
        #self.con = psycopg2.connect("dbname=veterinaria-db user=juandba host=localhost password=admin")
        self.con = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    """getConexion

        retorna la instancia de la base de datos
    """
    def getConexion(self):
        return self.con