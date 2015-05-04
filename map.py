import pygmaps

mymap = pygmaps.maps(37.428, -122.145, 16)

mymap.setgrids(37.42, 37.43, 0.001, -122.15, -122.14, 0.001)

mymap.addpoint(37.427, -122.145, "#0000FF")

mymap.addradpoint(37.429, -122.145, 95, '#FF0000')
		
mymap.draw('./mymap.html')

