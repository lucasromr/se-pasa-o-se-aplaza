# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class CargoDao:

    def getCargos(self):

        cargoSQL = """
        SELECT id, descripcion
        FROM cargos
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cargoSQL)
            cargos = cur.fetchall()  # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': cargo[0], 'descripcion': cargo[1]} for cargo in cargos]

        except Exception as e:
            app.logger.error(f"Error al obtener todas los cargos: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getCargoById(self, id):

        cargoSQL = """
        SELECT id, descripcion
        FROM cargos WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(cargoSQL, (id,))
            cargoEncontrada = cur.fetchone()  # Obtener una sola fila
            if cargoEncontrada:
                return {
                        "id": cargoEncontrada[0],
                        "descripcion": cargoEncontrada[1]
                    }  # Retornar los datos
            else:
                return None  # Retornar None si no se encuentra cargo
        except Exception as e:
            app.logger.error(f"Error al obtener cargo {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarCargo(self, descripcion):

        insertCargoSQL = """
        INSERT INTO cargos(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertCargoSQL, (descripcion,))
            cargo_id = cur.fetchone()[0]
            con.commit()  # se confirma la insercion
            return cargo_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar cargo: {str(e)}")
            con.rollback()  # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateCargo(self, id, descripcion):

        updateCargoSQL = """
        UPDATE cargos
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateCargoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount  # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0  # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar cargo: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteCargo(self, id):

        deleteCargoSQL = """
        DELETE FROM cargos
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(deleteCargoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar cargo: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()