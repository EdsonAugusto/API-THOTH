import pyodbc
from paramiko import SSHClient, AutoAddPolicy

class Manager_SQL_Server:
    def __init__(self, serverSQL, portSQL, userSQL, passwordSQL, DB_SQL):
          self.serverSQL = serverSQL
          self.portSQL = portSQL
          self.userSQL = userSQL
          self.passwordSQL = passwordSQL
          self.DB_SQL = DB_SQL
    def connection_sql(self):
          """Method for SQL Server database connection."""
          connection = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={self.serverSQL},{self.portSQL};'
            f'DATABASE={self.DB_SQL};UID={self.userSQL};PWD={self.passwordSQL}')
          return connection.cursor()
    
    def query_sql(self, command):
        """Method for querying (read) SQL Server database."""
        sql = self.connection_sql()
        return list(sql.execute(command))
    
    def commit_sql(self, command):
        """Method for commit (create/update) SQL Server database."""
        sql = self.connection_sql()
        sql.execute(command)
        sql.commit()
        return True
    
class Macro_SQL:
    def __init__(self, command, servers):
        self.command = command
        self.servers = servers

    def macro_sql_query(self):
        """Macro query for multiple DBs."""
        result_query = {}
        if len(self.servers) > 0:
            for server in self.servers:
                connection = Manager_SQL_Server(
                serverSQL=self.servers[server]['serverSQL'],
                portSQL=self.servers[server]['portSQL'],
                userSQL=self.servers[server]['userSQL'],
                passwordSQL=self.servers[server]['passwordSQL'],
                DB_SQL=self.servers[server]['DB_SQL'],
                )
                result_query[server] = connection.query_sql(self.command)
            return result_query
        else:
            return None
        
        
def macro_sql_commit(self):
    """Macro commit for multiple DBs."""
    result_query = {}
    if len(self.servers) > 0:
        for server in self.servers:
            connection = Manager_SQL_Server(
            serverSQL=self.servers[server]['serverSQL'],
            portSQL=self.servers[server]['portSQL'],
            userSQL=self.servers[server]['userSQL'],
            passwordSQL=self.servers[server]['passwordSQL'],
            DB_SQL=self.servers[server]['DB_SQL'],
            )
            result_query[server] = connection.commit_sql(self.command)
        return result_query
    else:
        return None
