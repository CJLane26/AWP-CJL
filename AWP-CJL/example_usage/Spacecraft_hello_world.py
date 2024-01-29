'''
AWP | Astrodynamics with Python by Alfonso Gonzalez
https://github.com/alfonsogonzalez/AWP
https://www.youtube.com/c/AlfonsoGonzalezSpaceEngineering

Hello world of Spacecraft class
Two-body propagation with J2 perturbation for 100 periods
'''

# Python standard libraries
# AWP libraries

# Add AWP libraries to path
from sys import path
path.append("H:\Coding\Python\AWP_CJL\AWP-CJL\src\python_tools")

from Spacecraft import Spacecraft as SC
from planetary_data import earth


if __name__ == '__main__':
	# Keplerian classical orbital elements [semi-major axis, eccentricity, inclination, true anomaly, argument of periapsis, right ascension of ascending node]
	coes = [ earth[ 'radius' ] + 1000, 0.05, 30.0, 0.0, 0.0, 0.0 ]
	sc   = SC(
			{
			'coes'       : coes,
			'tspan'      : '1', 
			'dt'         : 100.0,
			'orbit_perts': { 'J2': True }
			} )
	sc.plot_3d()