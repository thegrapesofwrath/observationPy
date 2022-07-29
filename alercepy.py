import requests

baseUrl = "http://api.alerce.online/ztf/v1/"

class AlerceObject:

    def __init__(self) -> None:
        self.url = baseUrl + 'objects'
    
    def singleObject(self,id: str = None) -> dict:
        try:
            if id is not None:
                response = requests.get(f"{self.url}/{id}")
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Object not found: {id}")
                    return None
            else:
                raise ValueError
        except ValueError:
            print(f"Is id null? id = {id}")
        except Exception as e:
            print(e)

    def objects(self) -> list:
        raise NotImplementedError

class Lightcurve:

    def __init__(self) -> None:
        self.url = baseUrl + 'lightcurve'
    
    def detections(self,id: str = None) -> dict:
        try:
            if id is not None:
                response = requests.get(f"{self.url}/{id}/detections")
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Object not found: {id}")
                    return None
            else:
                raise ValueError
        except ValueError:
            print(f"Is id null? id = {id}")
        except Exception as e:
            print(e)

    def lightcurve(self,id: str = None) -> dict:
        try:
            if id is not None:
                response = requests.get(f"{self.url}/{id}/lightcurve")
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Object not found: {id}")
                    return None
            else:
                raise ValueError
        except ValueError:
            print(f"Is id null? id = {id}")
        except Exception as e:
            print(e)

    def non_detections(self,id: str = None) -> dict:
        try:
            if id is not None:
                response = requests.get(f"{self.url}/{id}/non_detections")
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Object not found: {id}")
                    return None
            else:
                raise ValueError
        except ValueError:
            print(f"Is id null? id = {id}")
        except Exception as e:
            print(e)

class MagnitudeStatistics:

    def __init__(self) -> None:
        self.url = baseUrl + 'objects'
    
    def magstats(self,id: str = None) -> dict:
        try:
            if id is not None:
                response = requests.get(f"{self.url}/{id}/magstats")
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Object not found: {id}")
                    return None
            else:
                raise ValueError
        except ValueError:
            print(f"Is id null? id = {id}")
        except Exception as e:
            print(e)

class Probabilities:

    def __init__(self) -> None:
        self.url = baseUrl + 'objects'
    
    def probabilities(self,id: str = None) -> dict:
        try:
            if id is not None:
                response = requests.get(f"{self.url}/{id}/probabilities")
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Object not found: {id}")
                    return None
            else:
                raise ValueError
        except ValueError:
            print(f"Is id null? id = {id}")
        except Exception as e:
            print(e)

class Classifier:

    def __init__(self) -> None:
        self.url = baseUrl + 'classifiers'
    
    def classifiers(self,id: str = None) -> dict:
        try:
            if id is not None:
                response = requests.get(f"{self.url}")
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Object not found: {id}")
                    return None
            else:
                raise ValueError
        except ValueError:
            print(f"Is id null? id = {id}")
        except Exception as e:
            print(e)
    
    def classes(self):
        raise NotImplementedError

class Features:

    def __init__(self) -> None:
        self.url = baseUrl + 'objects'
    
    def features(self,id: str = None) -> dict:
        try:
            if id is not None:
                response = requests.get(f"{self.url}/{id}/features")
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Object not found: {id}")
                    return None
            else:
                raise ValueError
        except ValueError:
            print(f"Is id null? id = {id}")
        except Exception as e:
            print(e)
    
    def single_feature(self):
        raise NotImplementedError