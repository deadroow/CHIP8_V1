class Rom:
    @staticmethod
    def create(path,data:str):
        with open (file=path,mode ="wb")as fp:
            binary_data=bytes.fromhex(data)
            fp.write(binary_data)