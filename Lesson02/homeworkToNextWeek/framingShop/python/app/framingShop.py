def getFramePrice(width:float, height:float):
    # validation of the inputs
    # TODO - add later

    # range check
    if(width < 30 or width > 60 or height < 30 or height > 100):
        return 0

    area = width * height

    if(area > 1600):
        return 3500
    else:
        return 3000
    
