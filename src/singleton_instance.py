class SingletonInstane(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonInstane, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
