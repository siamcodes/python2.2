#หาพื้นที่สามเหลี่ยม 1/2*ฐาน*สูง
def Triangle(base, height):
    area = 1/2*base*height
    #print("พื้นที่สามเหลี่ยม %.2f" % area)
    return area

print("พื้นที่สามเหลี่ยม %.2f" % Triangle(2,3))
print("พื้นที่สามเหลี่ยม %.2f" % Triangle(5,10))