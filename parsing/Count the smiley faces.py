def count_smileys(arr):
    #the number of valid smiley faces in array/list
    smiley_faces = []
    for i in [':',';']:
        for j in ['','-','~']:
            for k in [')','D']:
                smiley_faces.append(i+j+k)
    count = sum(1 for p in arr if p in smiley_faces)
    return count
