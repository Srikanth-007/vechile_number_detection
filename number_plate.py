import code as vc
numPlate = vc.NumberPlateRecognizer('paste image path here...')
number = numPlate.Retrieve_Number_plate()
number = number.upper()