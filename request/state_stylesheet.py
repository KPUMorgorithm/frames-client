class StateStyleSheet(dict):

    def __init__(self):
        super().__init__()
        
        self[0] = """
                width: 100%;
                color: #FFFFFF;
                background-color: #719C70;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """
        self[1] = """
                width: 100%;
                color: #FFFFFF;
                background-color: #F24A33;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """
        self[2] = """
                width: 100%;
                color: #FFFFFF;
                background-color: #F24A33;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """
        self[3] = """
                width: 100%;
                color: #FFFFFF;
                background-color: #333333;
                font-weight: bold;
                font-size: 32px;
                margin: 0;
                """