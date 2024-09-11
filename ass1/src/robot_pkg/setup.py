from setuptools import setup
from glob import glob

package_name = 'robot_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    package_dir={package_name: 'robot_pkg'},
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email',
    description='Description of your package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'telemetry_node = robot_pkg.telemetry_node:main',  # Robot node
            'coordinator_node = robot_pkg.coordinator_node:main',  # Coordinator node
        ],
    },
)

