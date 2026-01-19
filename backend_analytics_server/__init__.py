import pymysql

# Esto engaña a Django para que crea que PyMySQL es mysqlclient
pymysql.install_as_MySQLdb()

# ESTA ES LA PARTE NUEVA PARA EVITAR EL ERROR DE VERSIÓN:
pymysql.version_info = (2, 2, 1, "final", 0)