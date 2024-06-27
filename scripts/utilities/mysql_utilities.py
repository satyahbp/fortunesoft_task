# library imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# custom imports
from scripts.logging.log_module import logger as log

class MySQLUtility:

    def __init__(
        self, 
        host: str, 
        port: str, 
        user: str, 
        password: str,
        db: str
    ) -> None:
        if port:
            engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}")
        else:
            engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")
        self.session = sessionmaker(bind=engine)


    def add_filter(self, filter_to_add, query):
        query = query.filter(filter_to_add)
        return query


    def fetch_all_data_with_join(
        self,
        table_list: tuple,
        conditions_list: tuple,
        sort = None
    ) -> list:
        current_session = self.session()
        final_result = list()
        try:
            query = current_session.query(*table_list)
            for each_condition in conditions_list:
                query = self.add_filter(each_condition, query)

            if sort:
                query = query.order_by(sort)

            final_result = query.all()
            
            return final_result
        except Exception as e:
            log.error("Error while querying join data: " + str(e))
        finally:
            current_session.close()
        
        return final_result