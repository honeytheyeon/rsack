class DeviceIDError():
    def __init__(self, message: str):
        self.message = message

    def __str__(self) -> str:
        return self.message