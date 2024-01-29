# Add AWP libraries to path
from sys import path
path.append("H:\Coding\Python\AWP_CJL\AWP-CJL\src\python_tools")

from Spacecraft import Spacecraft as SC
from planetary_data import earth

if __name__ == '__main__':
    # Keplerian classical orbital elements [semi-major axis, eccentricity, inclination, true anomaly, argument of periapsis, right ascension of ascending node]
	coes = [ earth[ 'radius' ] + 10000, 0.5, 0.0, 0.0, 0.0, 0.0 ]
	sc   = SC(
			{
			'coes'       : coes,
			'tspan'      : '1', 
			'dt'         : 100.0,
			'orbit_perts': { 'J2': True }
			} )
	sc.plot_3d()