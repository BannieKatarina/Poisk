def mashtab(toponym):
    # Нахождение размера объекта в градусной мере:
    toponym_lower = list(map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split(' ')))
    toponym_upper = list(map(float, toponym['boundedBy']['Envelope']['upperCorner'].split(' ')))
    toponym_spn = list(map(str, [toponym_upper[0] - toponym_lower[0], toponym_upper[1] - toponym_lower[1]]))
    return toponym_spn