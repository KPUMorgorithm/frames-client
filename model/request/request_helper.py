from client.model.request.request_landmark import RequestLandmark

class RequestHelper:  

    @staticmethod
    def requestLandmarkAndTemperature(resultQueue, config, landmark, temperature):
        RequestLandmark(resultQueue, config).requestLandmark(landmark,temperature)
        

