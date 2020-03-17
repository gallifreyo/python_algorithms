
def verify(v):
    for x in range(len(v)):
        while x < len(v):
            if v[x] < v[x+1]:
                return print("True")
            return print("False")

vet = [1,2,3,4,5]
verify(vet)

    
'''

def maior(a,b):
    if a > b:
        return print("True")
    return print("False")

maior(3,4)

'''
