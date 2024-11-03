# route
import ipyleaflet
from ipyleaflet import Map, Marker

# map
map_plot_route = Map(center=[38, -98], zoom=4)

# route_locs = ['Los Angeles', 'Las Vegas', 'Denver', 'Chicago', 'Manhattan']
# can use list of lists or list of tuples
route_lats_longs = [[34.041008,-118.246653],
                    [36.169726,-115.143996], 
                    [39.739448,-104.992450], 
                    [41.878765,-87.643267], 
                    [40.782949,-73.969559]]

# add route to map
route = ipyleaflet.Polyline(locations=[route_lats_longs])
map_plot_route.add_layer(route)

# display map
map_plot_route